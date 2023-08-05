"""Anyscale connect implementation.

Here's an overview of how a connect call works. It goes through a few steps:
    1. Detecting the project and comparing build_id and compute_template_id
    2. Getting or creating a cluster if necessary.
    3. Acquiring a cluster lock via the Ray client (when not in multiclients mode)

Detecting the project: The project may be specified explicitly or
autodetected based on an initialized anyscale project in the
current working directory or one of its ancestor directories.
Otherwise the default project for the organization will be used.

Getting or creating a cluster: If a cluster name is passed in, anyscale
will start a cluster with that name unless the cluster is already running.
If the cluster is already running we compare the new cluster env build_id and
compute_template_id with the new cluster, if they match we connect, if they do
not match, we fail and require explicitly updating the cluster.

Acquiring a cluster lock via the Ray client: To avoid multiple clients from
connecting to the same cluster, by default we acquire an exclusive lock on
the cluster. This is done by checking that "num_clients" == 1 in the
returned connection info object, which means that we are the first client.
You can also allow multiple clients to connect to one cluster by passing
ANYSCALE_ALLOW_MULTIPLE_CLIENTS=1
"""

import copy
from datetime import datetime, timezone
import inspect
import json
import os
from pathlib import Path
import re
import shlex
import subprocess
import sys
import time
from types import ModuleType
from typing import Any, cast, Dict, List, Optional, Tuple, Union
from urllib.parse import parse_qs, urlparse
import uuid

from packaging import version
import requests
import yaml

from anyscale.api import configure_open_api_client_headers
from anyscale.authenticate import AuthenticationBlock, get_auth_api_client
from anyscale.background.job_context import BackgroundJobContext
from anyscale.cli_logger import _ConsoleLog
from anyscale.client.openapi_client.models.app_config import AppConfig
from anyscale.client.openapi_client.models.build import Build
from anyscale.client.openapi_client.models.session import Session
from anyscale.cloud import get_cloud_id_and_name
from anyscale.controllers.exec_controller import ExecController
from anyscale.controllers.session_controller import SessionController
from anyscale.links import DOCS_CLUSTER
import anyscale.project
from anyscale.sdk.anyscale_client import (
    ComputeTemplateConfig,
    ComputeTemplateQuery,
    CreateCluster,
    CreateComputeTemplate,
    StartClusterOptions,
    UpdateCluster,
)
from anyscale.sdk.anyscale_client.models.cloud import Cloud
from anyscale.sdk.anyscale_client.sdk import AnyscaleSDK
from anyscale.shared_anyscale_utils.util import slugify
from anyscale.util import get_endpoint, wait_for_session_start
from anyscale.utils.connect_helpers import (
    AnyscaleClientConnectResponse,
    AnyscaleClientContext,
    find_project_id,
    get_cluster,
    list_entities,
)
from anyscale.utils.ray_version_checker import (
    check_required_ray_version,
    detect_python_minor_version,
)


# Max number of auto created clusters.
MAX_CLUSTERS = 40

# Default minutes for autosuspend.
DEFAULT_AUTOSUSPEND_TIMEOUT = 120

# The paths to exclude when syncing the working directory in runtime env.
EXCLUDE_DIRS = [".git", "__pycache__", "venv"]
EXCLUDE_PATHS = [".anyscale.yaml", "session-default.yaml"]

# The type of the dict that can be passed to create a cluster env.
# e.g., {"base_image": "anyscale/ray-ml:1.1.0-gpu"}
CLUSTER_ENV_DICT_TYPE = Dict[str, Union[str, List[str]]]

# The cluster compute type. It can either be a string, eg my_template or a dict,
# eg, {"cloud_id": "id-123" ...}
CLUSTER_COMPUTE_DICT_TYPE = Dict[str, Any]

# Commands used to build Ray from source. Note that intermediate stages will
# be cached by the app config builder.
BUILD_STEPS = [
    "git clone https://github.com/ray-project/ray.git",
    "curl -fsSL https://bazel.build/bazel-release.pub.gpg | gpg --dearmor > bazel.gpg",
    "sudo mv bazel.gpg /etc/apt/trusted.gpg.d/",
    'echo "deb [arch=amd64] https://storage.googleapis.com/bazel-apt stable jdk1.8" | sudo tee /etc/apt/sources.list.d/bazel.list',
    "sudo apt-get update && sudo apt-get install -y bazel=3.2.0",
    'cd ray/python && sudo env "PATH=$PATH" python setup.py develop',
    "pip uninstall -y ray",
]

# Minimum default Ray version to return when a user either asks for `anyscale.connect required_ray_version`
# or when a Default Cluster Env is used
# TODO(ilr/nikita) Convert this to a backend call for the most recent Ray Version in the Dataplane!
MINIMUM_RAY_VERSION = "1.4.0"


# Default docker images to use for connect clusters.
def _get_base_image(image: str, ray_version: str, cpu_or_gpu: str) -> str:
    py_version = "".join(str(x) for x in sys.version_info[0:2])
    if py_version not in ["36", "37", "38"]:
        raise ValueError("No default docker image for py{}".format(py_version))
    return "anyscale/{}:{}-py{}-{}".format(image, ray_version, py_version, cpu_or_gpu)


def _get_interactive_shell_frame(frames: Optional[List[Any]] = None) -> Optional[Any]:
    # TODO(nikita): This method has been moved to anyscale.connect_utils.start_interactive_session.
    # Remove and import from there.
    if frames is None:
        frames = inspect.getouterframes(inspect.currentframe())

    first_non_anyscale = None

    for i, frame in enumerate(frames):
        if "anyscale" not in frame.filename and "ray" not in frame.filename:
            first_non_anyscale = i
            break

    if first_non_anyscale is None:
        return None

    return frames[first_non_anyscale]


def _is_in_shell(frames: Optional[List[Any]] = None) -> bool:
    """
    Determines whether we are in a Notebook / shell.
    This is done by inspecting the first non-Anyscale related frame.
    If this is from an interactive terminal it will be either STDIN or IPython's Input.
    If connect() is being run from a file (like python myscript.py), frame.filename will equal "myscript.py".
    """
    fr = _get_interactive_shell_frame(frames)

    if fr is None:
        return False

    is_ipython = fr.filename.startswith("<ipython-input") and fr.filename.endswith(">")
    is_regular_python_shell: bool = fr.filename == "<stdin>"
    return is_regular_python_shell or is_ipython


def _is_running_on_anyscale_cluster() -> bool:
    return "ANYSCALE_SESSION_ID" in os.environ


class ClientBuilder:
    """This class lets you set cluster options and connect to Anyscale.

    It should not be constructed directly, but instead via ray.init("anyscale://") arguments
    exported at the package level.

    Examples:
        >>> # Raw client, creates new cluster on behalf of user
        >>> ray.init("anyscale://")

        >>> # Get or create a named cluster
        >>> ray.init("anyscale://my_named_cluster")

        >>> # Specify a previously created cluster environment
        >>> ray.init(
        ...   "anyscale://<cluster-name>?cluster_compute=compute:1",
        ...   cluster_env="prev_created_config:2",
        ...   autosuspend="2h")

        >>> # Create new cluster from local env / from scratch
        >>> ray.init("anyscale://<cluster-name>",
        ...   runtime_env={"working_dir": "~/dev/my-project-folder"}
        ... )

        >>> # Ray client connect is setup automatically
        >>> @ray.remote
        ... def my_func(value):
        ...   return value ** 2

        >>> # Remote functions are executed in the Anyscale cluster
        >>> print(ray.get([my_func.remote(x) for x in range(5)]))
        >>> [0, 1, 4, 9, 16]
    """

    def __init__(
        self,
        address: Optional[str] = None,
        anyscale_sdk: AnyscaleSDK = None,
        subprocess: ModuleType = subprocess,
        requests: ModuleType = requests,
        _ray: Optional[ModuleType] = None,
        log: Any = _ConsoleLog(),
        _os: ModuleType = os,
        _ignore_version_check: bool = False,
        auth_api_client: Optional[AuthenticationBlock] = None,
    ) -> None:

        # Class dependencies.
        self._anyscale_sdk: AnyscaleSDK = None
        self._credentials = None
        if auth_api_client is None:
            auth_api_client = get_auth_api_client()
        self._log = log
        self._log.open_block("Output")
        if anyscale_sdk:
            self._anyscale_sdk = anyscale_sdk
        else:
            self._credentials = auth_api_client.credentials
            self._log.debug(
                "Using host {}".format(
                    anyscale.shared_anyscale_utils.conf.ANYSCALE_HOST
                )
            )
            self._log.debug("Using credentials {}".format(self._credentials[:6]))
            self._anyscale_sdk = AnyscaleSDK(
                self._credentials,
                anyscale.shared_anyscale_utils.conf.ANYSCALE_HOST + "/ext",
            )
            configure_open_api_client_headers(self._anyscale_sdk.api_client, "connect")
        api_client = auth_api_client.api_client
        configure_open_api_client_headers(api_client.api_client, "connect")
        anyscale_api_client = auth_api_client.anyscale_api_client
        self._api_client = api_client
        self._anyscale_api_client = anyscale_api_client
        if not _ray:
            try:
                import ray
            except ModuleNotFoundError:
                raise RuntimeError(
                    "Ray is not installed. Please install with: \n"
                    "pip install -U --force-reinstall `python -m anyscale.connect required_ray_version`"
                )
            _ray = ray
        self._ray: Any = _ray
        self._subprocess: Any = subprocess
        self._os: Any = _os
        self._requests: Any = requests
        self._in_shell = _is_in_shell()
        self._session_controller = SessionController()
        self._exec_controller = ExecController()

        # Environment variables
        # If we are running in an anyscale cluster, or IGNORE_VERSION_CHECK is set,
        # skip the pinned versions
        if "IGNORE_VERSION_CHECK" in os.environ or _is_running_on_anyscale_cluster():
            _ignore_version_check = True
        self._ignore_version_check = _ignore_version_check

        s3_caching = os.environ.get("ANYSCALE_ENABLE_S3_CACHING")
        if s3_caching is not None and s3_caching == "1":
            self._log.debug("Using s3 caching to start cluster.")
            from anyscale.utils.runtime_env import (
                runtime_env_setup as s3_runtime_env_setup,
            )

            s3_runtime_env_setup()
            anyscale.utils.runtime_env.logger = log

        if os.environ.get("ANYSCALE_COMPUTE_CONFIG") == "1":
            self._log.info(
                "All anyscale.connect clusters will be started with compute configs so "
                "ANYSCALE_COMPUTE_CONFIG=1 no longer needs to be specified."
            )

        # Determines whether the gRPC connection the server will be over SSL.
        self._secure: bool = os.environ.get("ANYSCALE_CONNECT_SECURE") != "0"
        if not self._secure:
            self._log.warning(
                "The connection between your machine and the cluster is *NOT* encrypted "
                "because the environment variable `ANYSCALE_CONNECT_SECURE=0` was specified. "
                "This is not recommended and will be deprecated in the near future."
            )

        # Builder args.
        self._project_dir: Optional[str] = None
        self._project_name: Optional[str] = None
        self._cloud_name: Optional[str] = None
        self._cluster_name: Optional[str] = None
        self._requirements: Optional[str] = None
        self._cluster_compute_name: Optional[str] = None
        self._cluster_compute_dict: Optional[CLUSTER_COMPUTE_DICT_TYPE] = None
        self._cluster_env_name: Optional[str] = None
        self._cluster_env_dict: Optional[CLUSTER_ENV_DICT_TYPE] = None
        self._cluster_env_revision: Optional[int] = None
        self._initial_scale: List[Dict[str, float]] = []
        # Will be overwritten to DEFAULT_AUTOSUSPEND_TIMEOUT if not set by user.
        self._autosuspend_timeout: Optional[int] = None
        self._run_mode: Optional[str] = None
        self._build_commit: Optional[str] = None
        self._build_pr: Optional[int] = None
        self._force_rebuild: bool = False
        self._job_config = self._ray.job_config.JobConfig()
        self._user_runtime_env: Dict[str, Any] = {}
        self._allow_public_internet_traffic: Optional[bool] = None
        self._ray_init_kwargs: Dict[str, Any] = {}
        # Override default run mode.
        if "ANYSCALE_BACKGROUND" in os.environ:
            self._run_mode = "background"
            self._log.debug(
                "Using `run_mode=background` since ANYSCALE_BACKGROUND is set"
            )
        elif "ANYSCALE_LOCAL_DOCKER" in os.environ:
            self._run_mode = "local_docker"
            self._log.debug(
                "Using `run_mode=local_docker` since ANYSCALE_LOCAL_DOCKER is set"
            )

        # Whether to update the cluster when connecting to a fixed cluster.
        self._needs_update: bool = True
        self._parse_address(address)

    def _parse_address(self, address: Optional[str]) -> None:
        """
        DEPRECATED, should be removed after deprecating the client builder.
        Parses the anyscale address and sets parameters on this builder.
        Eg, address="<cluster-name>?cluster_compute=my_template&autosuspend=5&cluster_env=bla:1&update=True
        """

        # The supported parameters that we can provide in the url.
        # e.g url="anyscale://ameer?param1=val1&param2=val2"
        CONNECT_URL_PARAMS = ["cluster_compute", "cluster_env", "autosuspend", "update"]

        if address is None or not address:
            return
        parsed_result = urlparse(address)

        # Parse the cluster name. e.g., what is before the question mark in the url.
        cluster_name = parsed_result.path
        if cluster_name:
            self.session(cluster_name)

        # parse the parameters (what comes after the question mark)
        # parsed_result.query here looks like "param1=val1&param2=val2"
        # params_dict looks like:
        # {'cluster_compute': ['my_template'], 'autosuspend': ['5'], 'cluster_env': ['bla:1']}.
        params_dict: Dict[str, Any] = parse_qs(parsed_result.query)
        for key, val in params_dict.items():
            if key == "autosuspend":
                self.autosuspend(minutes=int(val[0]))
            elif key == "cluster_env":
                self.cluster_env(val[0])
            elif key == "cluster_compute":
                self.cluster_compute(val[0])
            elif key == "update":
                self._needs_update = val[0] == "True" or val[0] == "true"
            else:
                raise ValueError(
                    "Provided parameter in the anyscale address is "
                    f"{key}. The supported parameters are: {CONNECT_URL_PARAMS}."
                )

    def _init_args(self, **kwargs) -> "ClientBuilder":  # noqa: C901
        """
        Accepts arguments from ray.init when called with anyscale protocol,
        i.e. ray.init("anyscale://someCluster", arg1="thing", arg2="other").
        Ignores and raises a warning on unknown argument names.

        Arguments are set directly with method calls in _parse_arg_as_method.
        """
        unknown = []

        # request_resources arguments
        request_resources_cpus = kwargs.pop("request_cpus", None)
        request_resources_gpus = kwargs.pop("request_gpus", None)
        request_resources_bundles = kwargs.pop("request_bundles", None)

        # build_from_source arguments
        build_from_source_commit = kwargs.pop("git_commit", None)
        build_from_source_pr_id = kwargs.pop("github_pr_id", None)
        force_rebuild = kwargs.pop("force_rebuild", False)

        # project_dir arguments
        project_dir = kwargs.pop("project_dir", None)
        project_name = kwargs.pop("project_name", None)

        for arg_name, value in kwargs.items():
            if self._parse_arg_as_method(arg_name, value):
                continue
            elif arg_name == "autosuspend":
                self._parse_autosuspend(value)
            elif arg_name == "update":
                if not isinstance(value, bool):
                    # Extra cautious check -- make sure users don't pass
                    # None/"false" in
                    raise RuntimeError(
                        "The value passed for the `update` argument should "
                        f"be a boolean. Found {type(value)} instead."
                    )
                self._needs_update = value
            # Explicitly error on `num_cpus` and `num_gpus`, since it's likely
            # user confused with `request_cpus` and `request_gpus`
            elif arg_name == "num_cpus":
                raise RuntimeError(
                    "Invalid argument `num_cpus` for anyscale client. Did "
                    "you mean `request_cpus`?"
                )
            elif arg_name == "num_gpus":
                raise RuntimeError(
                    "Invalid argument `num_gpus` for anyscale client. Did "
                    "you mean `request_gpus`?"
                )
            elif arg_name == "allow_public_internet_traffic":
                if not isinstance(value, bool):
                    raise RuntimeError(
                        "The value passed for the `allow_public_internet_traffic` argument should "
                        f"be a boolean. Found {type(value)} instead."
                    )
                self._allow_public_internet_traffic = value
            elif self._forward_argument(arg_name, value):
                continue
            else:
                unknown.append(arg_name)

        if unknown:
            unknown_str = ", ".join(unknown)
            self._log.warning(
                f"Ignored, unsupported argument(s): {unknown_str}. This argument may not be "
                f"supported on ray {self._ray.__version__}. Try upgrading to a newer ray version "
                "or checking if this is a valid argument."
            )

        if (
            request_resources_cpus
            or request_resources_gpus
            or request_resources_bundles
        ):
            self.request_resources(
                num_cpus=request_resources_cpus,
                num_gpus=request_resources_gpus,
                bundles=request_resources_bundles,
            )

        if build_from_source_commit or build_from_source_pr_id:
            self.build_from_source(
                git_commit=build_from_source_commit,
                github_pr_id=build_from_source_pr_id,
                force_rebuild=force_rebuild,
            )

        if (
            self._user_runtime_env is None
            or self._user_runtime_env.get("working_dir") is None
        ):
            # This needs to be a warning message to not break users current usecases.
            # https://groups.google.com/a/anyscale.com/g/field-eng/c/4dAdqw4ORwU/m/eLYCCWZICAAJ?utm_medium=email&utm_source=footer&pli=1
            self._log.warning(
                "WARNING: No working_dir specified! Files will only be uploaded to the cluster if a working_dir is provided or a project is detected. In the future, files will only be uploaded if working_dir is provided. "
                "To ensure files continue being imported going forward, set the working_dir in your runtime environment. "
                "See https://docs.ray.io/en/latest/handling-dependencies.html#runtime-environments."
            )

        if project_dir:
            self._log.warning(
                "The project_dir argument is deprecated. Instead, use the "
                "working_dir argument in a runtime environment. "
                "See https://docs.ray.io/en/latest/handling-dependencies.html#runtime-environments. "
                """Replace

                  ray.init("anyscale://...", project_dir=directory, ...)

                with

                  ray.init("anyscale://...", runtime_env={"working_dir": directory}, ...)
                """
            )
            self.project_dir(local_dir=project_dir, name=project_name)

        return self

    def _parse_autosuspend(self, value: Union[str, int]) -> None:
        """parses the value of autosuspend provided by the user.

        Autosuspend can be int interpreted as minutes or str -> "15m"/"2h" for 15 mins/2 hours.
        This function exists because self.autosuspend is used in the deprecated client builder
        (e.g., ray.client().autosuspend(...).connect()) and cannot be modified directly.
        Once we completely deprecate the client builder the old self.autosuspend can be updated.
        """
        if isinstance(value, str):
            # Autosuspend can take strings like "15" (minutes), "15m", and "2h"
            if value.endswith("m"):
                self.autosuspend(minutes=int(value[:-1]))
            elif value.endswith("h"):
                self.autosuspend(hours=int(value[:-1]))
            elif value == "-1":  # Setting autosuspend to "-1" disables it.
                self.autosuspend(enabled=False)
            else:
                self.autosuspend(minutes=int(value))
        else:
            if value == -1:  # Setting autosuspend to -1 disables it.
                self.autosuspend(enabled=False)
            else:
                self.autosuspend(minutes=value)

    def _parse_arg_as_method(self, argument_name: str, argument_value: Any) -> bool:
        """
        Handle keyword arguments to ray.init that can be handled directly as
        a method call. For example, init(cloud="value") can be handled
        directly by self.cloud("value").

        Args:
            argument_name (str): Name of the argument (i.e. "cloud",
                "autosuspend")
            argument_value (Any): Corresponding value to the argument,
                (i.e. "anyscale_default", "8h")

        Returns:
            True if the argument can be handled directly by a method, False
            otherwise
        """
        if argument_name not in {
            "cloud",
            "cluster_compute",
            "cluster_env",
            "job_name",
            "namespace",
            "runtime_env",
            "run_mode",
        }:
            return False
        # convert argname: runtime_env -> env
        # We want to use the `env` function here for backwards compatibility,
        # but use `runtime_env` as the argument name since it's more clear
        # and consistent with ray's APIs.
        if argument_name == "runtime_env":
            argument_name = "env"
        getattr(self, argument_name)(argument_value)
        return True

    def _forward_argument(self, arg_name: str, value: Any) -> bool:
        """
        Fills self._ray_init_kwargs with any kwargs that match the signature of
        the current ray version's ray.init method.

        Returns True if the argument can be forwarded, false otherwise
        """
        connect_sig = inspect.signature(self._ray.util.connect)
        if "ray_init_kwargs" not in connect_sig.parameters:
            # Installed version of ray doesn't support forward init args
            # through connect
            return False

        init_sig = inspect.signature(self._ray.init)
        if arg_name in init_sig.parameters:
            self._ray_init_kwargs[arg_name] = value
            return True
        return False

    def env(self, runtime_env: Dict[str, Any]) -> "ClientBuilder":
        """Sets the custom user specified runtime environment dict.

        Args:
            runtime_env (Dict[str, Any]): a python dictionary with runtime environment
                specifications.

        Examples:
            >>> ray.init("anyscale://cluster_name", runtime_env={"pip": "./requirements.txt"})
            >>> ray.init("anyscale://cluster_name",
            ...     runtime_env={"working_dir": "/tmp/bla", "pip": ["chess"]})
            >>> ray.init("anyscale://cluster_name", runtime_env={"conda": "conda.yaml"})
        """
        if not isinstance(runtime_env, dict):
            raise TypeError("runtime_env argument type should be dict.")
        self._user_runtime_env = copy.deepcopy(runtime_env)
        return self

    def namespace(self, namespace: str) -> "ClientBuilder":
        """Sets the namespace in the job config of the started job.

        Args:
            namespace (str): the name of to give to this namespace.

        Example:
            >> ray.init("anyscale://cluster_name", namespace="training_namespace")
        """
        self._job_config.set_ray_namespace(namespace)
        return self

    def job_name(self, job_name: Optional[str] = None) -> "ClientBuilder":
        """Sets the job_name so the user can identify it in the UI.
        This name is only used for display purposes in the UI.

        Args:
            job_name (str): the name of this job, which will be shown in the UI.

        Example:
            >>> ray.init("anyscale://cluster_name", job_name="production_job")
        """
        current_time_str = datetime.now(timezone.utc).strftime("%m-%d-%Y_%H:%M:%S")
        if not job_name:
            script_name = sys.argv[0]
            if script_name:
                job_name = f"{os.path.basename(script_name)}_{current_time_str}"
            else:
                job_name = f"Job_{current_time_str}"
        self._job_config.set_metadata("job_name", job_name)
        return self

    def _set_runtime_env_in_job_config(self, project_dir: Optional[str]) -> None:
        """Configures the runtime env inside self._job_config.
        project_dir is None if using the default project.
        """

        runtime_env = copy.deepcopy(self._user_runtime_env)

        # There's no need to exclude files like ".anyscale.yaml"
        # if using the default project.
        project_dir_excludes = (
            [os.path.join(project_dir, path) for path in EXCLUDE_PATHS]
            if project_dir
            else []
        )

        if "working_dir" not in runtime_env:
            if project_dir:
                runtime_env["working_dir"] = project_dir
        if "excludes" not in runtime_env:
            runtime_env["excludes"] = []
        runtime_env["excludes"] = (
            EXCLUDE_DIRS + runtime_env["excludes"] + project_dir_excludes
        )

        # Patch for https://github.com/ray-project/ray/issues/20876
        # If local pip or conda files are specified, read them here and rewrite
        # the runtime env to prevent FileNotFoundError in the Ray Client server.
        if "pip" in runtime_env and isinstance(runtime_env["pip"], str):
            # We have been given a path to a requirements.txt file.
            pip_file = Path(runtime_env["pip"])
            if not pip_file.is_file():
                raise ValueError(f"{pip_file} is not a valid file")
            runtime_env["pip"] = pip_file.read_text().strip().split("\n")
        if "conda" in runtime_env and isinstance(runtime_env["conda"], str):
            yaml_file = Path(runtime_env["conda"])
            if yaml_file.suffix in (".yaml", ".yml"):
                if not yaml_file.is_file():
                    raise ValueError(f"Can't find conda YAML file {yaml_file}.")
                try:
                    runtime_env["conda"] = yaml.safe_load(yaml_file.read_text())
                except Exception as e:
                    raise ValueError(f"Failed to read conda file {yaml_file}: {e}.")

        self._job_config.set_runtime_env(runtime_env)

    def _set_metadata_in_job_config(self, creator_id: Optional[str] = None) -> None:
        """
        Specify creator_id in job config. This is needed so the job
        can correctly be created in the database. Specify default job name
        if not user provided. This will be displayed in the UI.
        """
        # TODO(nikita): A customer can spoof this value and pretend to be someone else.
        # Fix this once we have a plan for verification.
        if creator_id is None:
            user = self._api_client.get_user_info_api_v2_userinfo_get().result
            creator_id = user.id

        self._job_config.set_metadata("creator_id", creator_id)
        if "job_name" not in self._job_config.metadata:
            self.job_name()

    def _build_cluster_env_if_needed(self, project_id: str):
        """
        TODO(nikita): This method has been moved to anyscale.connect_utils.prepare_cluster.
        Call create_prepare_cluster_block and delete this method from connect.py.

        Builds a new cluster env on the fly if a cluster env dict is provided by the user
        or if the user wants to build ray from source."""
        if self._build_pr or self._build_commit:
            self._cluster_env_name = self._build_app_config_from_source(project_id)

        if self._cluster_env_dict:
            self._log.info("building new docker image for the provided cluster env ...")
            # Replacing ":" with "-" because the cluster env name cannot include ":"
            self._cluster_env_name = (
                self._cluster_env_name
                or "anonymous_cluster_env-{}".format(
                    datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                )
            )
            self._anyscale_sdk.create_app_config(
                {
                    "name": self._cluster_env_name,
                    "project_id": project_id,
                    "config_json": self._cluster_env_dict,
                }
            )

    def _get_cloud_id(self, project_id: str) -> str:
        """
        TODO(nikita): This method has been moved to anyscale.connect_utils.prepare_cluster.
        Call create_prepare_cluster_block and delete this method from connect.py.

        Returns the cloud id from cloud name.
        If cloud name is not provided, returns the default cloud name if exists in organization.
        If default cloud name does not exist returns last used cloud.
        """
        cloud_name = self._cloud_name

        if cloud_name is None:
            default_cloud_name = self._get_organization_default_cloud()
            if default_cloud_name:
                cloud_name = default_cloud_name
            else:
                cloud_name = self._get_last_used_cloud(project_id)
        cloud_id, _ = get_cloud_id_and_name(self._api_client, cloud_name=cloud_name)
        return cloud_id

    def _cluster_needs_up(self, project_id: str) -> bool:
        """Returns True if the cluster needs to be started/update or else returns False.

        Returns False only when the cluster is currently running and the user did not
        explicitly pass an update request (`.cluster_env(..., update=True)`).
        """

        if self._cluster_name:
            sess = get_cluster(self._anyscale_sdk, project_id, self._cluster_name)
            if not sess:
                # Unconditionally create the cluster if it isn't up.
                needs_up = True
                self._log.info(
                    f"cluster {self._cluster_name} does not exist, this will start a new cluster."
                )
            elif sess.state != "Running":
                # Unconditionally create the cluster if it isn't up.
                needs_up = True
                self._log.info(
                    f"cluster {self._cluster_name} exists but not running, this will restart cluster {self._cluster_name}."
                )
            else:
                needs_up = self._needs_update
                if needs_up:
                    self._log.info(
                        f"cluster {self._cluster_name} is currently running, but update=True was provided in `ray.init()`, "
                        f"this will restart cluster {self._cluster_name} if any of the cluster configurations changed. "
                        "Note that update does not work on AIOA or GCP."
                    )
                else:
                    self._log.info(
                        f"cluster {self._cluster_name} is currently running, the cluster will not be restarted."
                    )

        else:
            needs_up = True

        return needs_up

    def _is_equal_cluster_compute(
        self, cluster_compute_1_id: str, cluster_compute_2_id: str,
    ) -> bool:
        """
        TODO(nikita): This method has been moved to anyscale.connect_utils.prepare_cluster.
        Call create_prepare_cluster_block and delete this method from connect.py.

        Compares config fields of two ComputeTemplate objects.
        """
        try:
            cluster_compute_1 = self._anyscale_sdk.get_compute_template(
                cluster_compute_1_id
            ).result.config
            cluster_compute_2 = self._anyscale_sdk.get_compute_template(
                cluster_compute_2_id
            ).result.config
            return bool(cluster_compute_1 == cluster_compute_2)
        except Exception as e:
            self._log.debug(f"Error comparing cluster compute: {e}")
            return False

    def _get_default_cluster_env_build(self) -> Build:
        """
        TODO(nikita): This method has been moved to anyscale.connect_utils.prepare_cluster.
        Call create_prepare_cluster_block and delete this method from connect.py.
        """
        py_version = "".join(str(x) for x in sys.version_info[0:2])
        if py_version not in ["36", "37", "38"]:
            raise ValueError(
                "No default cluster env for py{}. Please use a version of python between 3.6 and 3.8.".format(
                    py_version
                )
            )
        ray_version = self._ray.__version__
        if version.parse(ray_version) < version.parse(MINIMUM_RAY_VERSION):
            raise ValueError(
                f"No default cluster env for Ray version {ray_version}. Please upgrade "
                f"to a version >= {MINIMUM_RAY_VERSION}."
            )
        if "dev0" in ray_version:
            raise ValueError(
                f"Your locally installed Ray version is {ray_version}. "
                "There is no default cluster environments for nightly versions of Ray."
            )
        try:
            build = self._api_client.get_default_cluster_env_build_api_v2_builds_default_py_version_ray_version_get(
                f"py{py_version}", ray_version
            ).result
            return build
        except Exception:
            raise RuntimeError(
                f"Failed to get default cluster env for Ray: {ray_version} on Python: py{py_version}"
            )

    def _get_cluster_build_id(self, project_id: str) -> Build:
        """
        TODO(nikita): This method has been moved to anyscale.connect_utils.prepare_cluster.
        Call create_prepare_cluster_block and delete this method from connect.py.

        Returns the build id of the cluster to be created.

        By default we return the default cluster env. Unless the user overrides.
        """
        # get cluster env build id
        if self._cluster_env_name:
            build = self._get_cluster_env_build(
                project_id, self._cluster_env_name, self._cluster_env_revision
            )
        else:
            try:
                build = self._get_default_cluster_env_build()
            except ValueError as e:
                # A default cluster env was not found
                raise ValueError(
                    "Because you did not specify a cluster environment, we "
                    "attempted to use a default cluster environment but could "
                    "not find one that matches your requirements. "
                    "To specify a cluster environment, use the cluster_env "
                    "argument to ray.init() or the ANYSCALE_CLUSTER_ENV environment variable. "
                    "If one does not already exist, you can create a new cluster environment "
                    f"with your dependencies by following these instructions: {DOCS_CLUSTER}."
                ) from e

        return build

    def _get_cluster_compute_id(self, project_id: str) -> str:
        """
        TODO(nikita): This method has been moved to anyscale.connect_utils.prepare_cluster.
        Call create_prepare_cluster_block and delete this method from connect.py.

        Returns the compute template ids of the cluster to be created.

        By default we return the default cluster compute. Unless the user overrides.
        """
        # get cluster compute template
        if self._cluster_compute_name:
            compute_template_id = self._get_cluster_compute_id_from_name(
                project_id, self._cluster_compute_name
            )
        else:
            # If the user specifies _cluster_compute_dict use it, otherwise
            # use the default cluster compute template.
            if self._cluster_compute_dict:
                cluster_compute_class = ComputeTemplateConfig(
                    **self._cluster_compute_dict
                )
                config_object = cluster_compute_class
            else:
                cloud_id = self._get_cloud_id(project_id)
                config_object = self._anyscale_sdk.get_default_compute_config(
                    cloud_id
                ).result
            compute_template_id = self._register_compute_template(
                project_id, config_object
            )
        return compute_template_id

    def _validate_new_cluster_compute_and_env_match_existing_cluster(
        self, project_id: str, cluster_name: str, print_warnings: bool = True
    ) -> bool:
        """
        TODO(nikita): This method has been moved to anyscale.connect_utils.prepare_cluster.
        Call create_prepare_cluster_block and delete this method from connect.py.
        """
        update_required = False
        running_cluster = self._get_cluster_or_die(project_id, cluster_name)
        if self._cluster_env_name:
            overriding_build = self._get_cluster_build_id(project_id)
            if overriding_build.id != running_cluster.build_id:
                current_cluster_build = self._anyscale_sdk.get_build(
                    running_cluster.build_id
                ).result
                current_cluster_env = self._anyscale_sdk.get_app_config(
                    current_cluster_build.application_template_id
                ).result
                if print_warnings:
                    self._log.warning(
                        f"The cluster is currently using {current_cluster_env.name}:{current_cluster_build.revision} as the cluster env, "
                        f"yet {self._cluster_env_name}:{self._cluster_env_revision} was provided. The cluster will not be updated and will "
                        f"still use {current_cluster_env.name}:{current_cluster_build.revision} as the cluster env. To update the cluster, "
                        "please specify `update=True` in the anyscale address, e.g.: "
                        f'`ray.init("anyscale://{cluster_name}", cluster_env="{self._cluster_env_name}:{self._cluster_env_revision}", update=True)`'
                    )
                update_required = True
        if self._cluster_compute_name:
            overriding_compute = self._get_cluster_compute_id(project_id)
            if not self._is_equal_cluster_compute(
                overriding_compute, running_cluster.compute_template_id
            ):
                cluster_compute = self._anyscale_sdk.get_compute_template(
                    running_cluster.compute_template_id
                ).result
                if print_warnings:
                    self._log.warning(
                        f"The cluster is currently using {cluster_compute.name} as the cluster compute, "
                        f"yet {self._cluster_compute_name} was provided. The cluster will not be updated and will "
                        f"still use {cluster_compute.name} as the cluster compute. To update the cluster, please specify "
                        "`update=True` in the anyscale address, e.g.: "
                        f'`ray.init("anyscale://{cluster_name}", cluster_compute="{self._cluster_compute_name}", update=True")`'
                    )
                update_required = True
        if self._cluster_env_dict or self._cluster_compute_dict:
            self._log.warning(
                f"The cluster {cluster_name} is already active. To update the cluster please "
                "specify `update=True` in the anyscale address."
            )
            update_required = True

        if (
            self._allow_public_internet_traffic is not None
            and self._allow_public_internet_traffic
            != running_cluster.allow_public_internet_traffic
        ):
            if print_warnings:
                self._log.warning(
                    f"The cluster currently {'allows' if running_cluster.allow_public_internet_traffic else 'does not allow'} "
                    f"public internet traffic to the Serve endpoints, yet `allow_public_internet_traffic={self._allow_public_internet_traffic}` "
                    f"was specified. The cluster will not be updated and will continue {'allowing' if running_cluster.allow_public_internet_traffic else 'not allowing'} "
                    "public internet traffic to the Serve endpoints. To update the cluster, please specify `update=True` in the anyscale "
                    "address, e.g.: "
                    f'`ray.init("anyscale://{cluster_name}", update=True, allow_public_internet_traffic={self._allow_public_internet_traffic})`'
                )
            update_required = True

        return update_required

    def _fill_config_from_env(self, config_name: str) -> None:
        """
        Check if an environment variable corresponding to config_name is set,
        and if so try to configure the connection using that value. For
        example, if config_name is "job_name", then checks if the env var
        ANYSCALE_JOB_NAME is set. If it is, the calls self.job_name() on the
        value set for in the environment variable.
        """
        env_var_name = f"ANYSCALE_{config_name.upper()}"
        if env_var_name in os.environ:
            value = os.environ[env_var_name]
            self._log.info(
                f'Using "{value}" set in environment variable {env_var_name} to configure `{config_name}`.'
            )
            if config_name == "autosuspend":
                self._parse_autosuspend(value)
            else:
                getattr(self, config_name)(value)

    def _fill_unset_configs_from_env(self) -> None:
        """
        Fill unset configurations from environment variables. Currently
        supports the following configs: cloud, cluster_compute, cluster_env,
        job_name, and namespace.
        """
        if self._cloud_name is None:
            self._fill_config_from_env("cloud")

        # Only fill cluster_compute from environment if neither a name nor
        # a dict was passed
        cluster_compute_unset = (
            self._cluster_compute_name is None and self._cluster_compute_dict is None
        )
        if cluster_compute_unset:
            self._fill_config_from_env("cluster_compute")

        # Only fill cluster_env if neither a name nor a dict was passed
        cluster_env_unset = (
            self._cluster_env_name is None and self._cluster_env_dict is None
        )
        if cluster_env_unset:
            self._fill_config_from_env("cluster_env")

        if self._autosuspend_timeout is None:
            # set to default autosuspend timeout
            self._autosuspend_timeout = DEFAULT_AUTOSUSPEND_TIMEOUT
            # override to env variable if available
            self._fill_config_from_env("autosuspend")

        if "job_name" not in self._job_config.metadata:
            self._fill_config_from_env("job_name")

        if self._job_config.ray_namespace is None:
            self._fill_config_from_env("namespace")

    def _bg_set_outer_overwritable(self) -> None:
        self._job_config.set_metadata("inherit_from_child", "1")

    def _bg_connect(self) -> Any:
        """
        Implementation of anyscale.connect background mode. Assumes we are currently running on the head node.
        Connect to the current ray cluster, and set runtime env and metadata from env context
        """
        # This context is set from the outer job
        context = BackgroundJobContext.load_from_env()
        namespace = None
        if context:
            self._set_metadata_in_job_config(context.creator_db_id)
            self._job_config.set_metadata("original_command", context.original_command)
            self._job_config.set_metadata(
                "parent_ray_job_id", context.parent_ray_job_id
            )
            self._bg_set_runtime_env_in_job_config(context)
            namespace = context.namespace
        else:
            # The user has directly called "ray.init(address="anyscale://...")
            # on the head node, so there is no outer job and no context.
            # We can still support this, but we need to pass the runtime env
            # in the job config just like in the ordinary anyscale.connect().
            self._job_config.set_runtime_env(self._user_runtime_env)

        # RAY_ADDRESS is set to anyscale://
        # We don't want the below ray.init to call into anyscale.connect
        del os.environ["RAY_ADDRESS"]
        return self._ray.init(  # This is a ClientContext object
            address="auto", job_config=self._job_config, namespace=namespace
        )

    def _bg_set_runtime_env_in_job_config(self, context: BackgroundJobContext) -> None:
        """Configures the runtime env inside self._job_config for background mode
        This assumes that we want to use the same working dir for the inner and outer job
        """

        runtime_env = copy.deepcopy(self._user_runtime_env)

        # Don't allow overriding the internal working directory
        if "working_dir" in runtime_env:
            del runtime_env["working_dir"]

        runtime_env = {
            **runtime_env,
            "uris": context.runtime_env_uris,
            "_skip_uploading": 1,
        }
        self._job_config.set_runtime_env(runtime_env)

    def _set_serve_root_url_runtime_env(self, cluster: Session) -> None:
        # Sets SERVE_ROOT_URL_ENV_KEY to be the cluster's Serve URL. This will allow
        # users to pass the URL for Serve deployments with `DeploymentClass.url`
        # TODO(nikita): Update documentation once Ray 1.7 is released
        try:
            from ray.serve.constants import SERVE_ROOT_URL_ENV_KEY
        except ImportError:
            SERVE_ROOT_URL_ENV_KEY = "RAY_SERVE_ROOT_URL"

        try:
            # Like "https://session-xxx.anyscaleuserdata.com"
            base_url = cluster.host_name
            # Like "https://serve-session-xxx.anyscaleuserdata.com". Insert "serve"
            # after "https://" (which has length of 8)
            serve_url = (
                base_url[: base_url.index("https://") + 8]
                + "serve-"
                + base_url[base_url.index("https://") + 8 :]
            )
            self._user_runtime_env.setdefault("env_vars", {}).setdefault(
                SERVE_ROOT_URL_ENV_KEY, serve_url
            )
        except Exception:
            self._log.warning(
                f"Unable to set {SERVE_ROOT_URL_ENV_KEY} in runtime environment. Please specify "
                "full Serve session URL for Serve deployments."
            )

    def _start_cluster_if_needed(self) -> Tuple[str, str]:
        """
        Ensures cluster is running and updated with the correct information based on the
        address passed in to the ClientBuilder. This should be called before attempting
        to connect to a cluster.

        Note: This method is also used by other parts of the anyscale CLI so please
        don't add functionality not related to starting a cluster here.
        """

        # NOTE: Don't move this call. This fills any unset configs from the env
        # based on their default value (usually None), which might get
        # overwritten by logic farther down (project_dir automatically set to
        # cwd, job_name automatically generated if missing, etc...)
        self._fill_unset_configs_from_env()

        # TODO(ilr) Make this import from self._ray

        # TODO(ekl) check for duplicate connections
        self._log.zero_time()

        # Re-exec in the docker container.
        if self._run_mode == "local_docker":
            self._exec_self_in_local_docker()

        # Autodetect or use a default project.
        if self._project_dir is None:
            self._project_dir = anyscale.project.find_project_root(os.getcwd())
        if self._project_dir:
            project_id, project_name = self._ensure_project_setup_at_dir(
                self._project_dir, self._project_name
            )
        else:
            # Default project case
            default_project = self._anyscale_sdk.get_default_project().result
            project_id = default_project.id
            project_name = default_project.name

        self._set_metadata_in_job_config()
        if self._project_dir:
            self._log.info(
                f"Using project (name: {project_name}, project_dir: {self._project_dir}, id: {project_id})."
            )
        else:
            self._log.info(f"Using default project, id: {project_id}.")

        needs_up = self._cluster_needs_up(project_id)
        # create the cluster if terminated or does not exist.
        if needs_up:
            existing_terminated_cluster = (
                None
                if self._cluster_name is None
                else get_cluster(self._anyscale_sdk, project_id, self._cluster_name)
            )

            self._build_cluster_env_if_needed(
                project_id
            )  # updates self._cluster_env_name

            # If the cluster build is not explicitly provided by the user
            # then we use the existing cluster's build id (if the cluster
            # already exists). Otherwise, we get the default build ID.
            if self._cluster_env_name or existing_terminated_cluster is None:
                build_id = self._get_cluster_build_id(project_id).id
            else:
                build_id = existing_terminated_cluster.build_id

            cloud_id = self._get_cloud_id(project_id)
            if (
                (existing_terminated_cluster is not None)
                and (existing_terminated_cluster.cloud_id is not None)
                and (self._cloud_name is not None)  # user explicitly passed cloud var.
                and (
                    cloud_id != existing_terminated_cluster.cloud_id
                )  # cloud_id is the id of self._cloud_name
            ):
                raise ValueError(
                    "Error: current cluster already has a cloud. Changing it to a new cloud is not allowed. If you need a new cloud, please create a new cluster."
                )

            # If the user explicitly passes a cluster compute (dict or name),
            # Or if the cluster does not exist,
            # Or if the cluster already exist but the user is changing clouds,
            # Then get the updated cluster compute.
            # Otherwise, get the compute template of the existing terminated cluster.
            if (
                self._cluster_compute_name
                or self._cluster_compute_dict
                or existing_terminated_cluster is None
                or (
                    self._cloud_name is not None  # user explicitly passed cloud var.
                    and cloud_id
                    != existing_terminated_cluster.cloud_id  # cloud_id is the id of self._cloud_name
                )
            ):
                compute_template_id = self._get_cluster_compute_id(project_id)
            else:
                compute_template_id = existing_terminated_cluster.compute_template_id

            self._wait_for_app_build(project_id, build_id)

            self._cluster_name = self._create_cluster(
                project_id=project_id,
                build_id=build_id,
                compute_template_id=compute_template_id,
                cluster_name=self._cluster_name,
            )
        else:
            # `self._cluster_name` should always exist if `needs_up==False` based on the logic of
            # `_cluster_needs_up`, which returns True only when the cluster already exists.
            # Adding an assert for mypy.
            assert self._cluster_name
            self._validate_new_cluster_compute_and_env_match_existing_cluster(
                project_id, self._cluster_name
            )
        return project_id, self._cluster_name

    def connect(self) -> AnyscaleClientContext:  # noqa
        """Connect to Anyscale using previously specified options.

        Examples:
            >>> ray.init("anyscale://cluster_name")

        WARNING: using a new cluster_compute/cluster_env when connecting to an
        active cluster will not work unless the user passes `update=True`. e.g.:
            >>> ray.init("anyscale://cluster_name?update=True")
        """
        from ray.autoscaler import sdk as ray_autoscaler_sdk

        _allow_multiple_clients = (
            os.environ.get("ANYSCALE_ALLOW_MULTIPLE_CLIENTS") == "1"
        )
        if _allow_multiple_clients:
            if not self._cluster_name:
                self._log.warning(
                    "`ANYSCALE_ALLOW_MULTIPLE_CLIENTS` only works when a cluster_name is specified"
                )
            else:
                self._log.info(
                    "`ANYSCALE_ALLOW_MULTIPLE_CLIENTS` is set, multiple clients will be allowed to connect to one cluster."
                )

        if self._ray.util.client.ray.is_connected():
            raise RuntimeError(
                "Already connected to a Ray cluster, please "
                "run anyscale.connect in a new Python process."
            )

        # Allow the script to be run on an Anyscale cluster node as well.
        if _is_running_on_anyscale_cluster():
            # TODO(mattweber): Make background mode work with default projects.
            # This is a RayClientContext instead of an AnyscaleContext since we are connecting to the local cluster
            return self._bg_connect()  # type: ignore

        project_id, _ = self._start_cluster_if_needed()

        assert self._cluster_name  # appeases mypy
        cluster = self._get_cluster_or_die(project_id, self._cluster_name)
        self._set_serve_root_url_runtime_env(cluster)

        self._set_runtime_env_in_job_config(self._project_dir)
        # Need to re-acquire the connection after the update.
        connection_info = self._acquire_session_lock(
            cluster,
            connection_retries=10,
            job_config=self._job_config,
            allow_multiple_clients=_allow_multiple_clients,
        )

        # Check that we are connected to the Server.
        self._check_connection(project_id, self._cluster_name)

        # Issue request resources call.
        if self._initial_scale:
            self._log.debug("Calling request_resources({})".format(self._initial_scale))
            ray_autoscaler_sdk.request_resources(bundles=self._initial_scale)

        # Define ray in the notebook automatically for convenience.
        try:
            fr = _get_interactive_shell_frame()
            if self._in_shell and fr is not None and "ray" not in fr.frame.f_globals:
                self._log.debug("Auto importing Ray into the notebook.")
                fr.frame.f_globals["ray"] = self._ray
        except Exception as e:
            self._log.error("Failed to auto define `ray` in notebook", e)

        # If in background mode, execute the job in the remote session.
        if self._run_mode == "background":
            self._exec_self_in_head_node()

        anyscale_client_context = AnyscaleClientContext(
            anyscale_cluster_info=AnyscaleClientConnectResponse(cluster_id=cluster.id),
            dashboard_url=cluster.ray_dashboard_url,
            python_version=connection_info.get("python_version"),
            ray_version=connection_info.get("ray_version"),
            ray_commit=connection_info.get("ray_commit"),
            protocol_version=connection_info.get("protocol_version"),
            _num_clients=connection_info.get("num_clients"),
        )
        return anyscale_client_context

    def cloud(self, cloud_name: str) -> "ClientBuilder":
        """Set the name of the cloud to be used.

        This sets the name of the cloud that your connect cluster will be started
        in by default. This is completely ignored if you pass in a cluster compute config.

        Args:
            cloud_name (str): Name of the cloud to start the cluster in.

        Examples:
            >>> ray.init("anyscale://cluster_name", cloud="aws_test_account")
        """
        self._cloud_name = cloud_name
        return self

    def project_dir(
        self, local_dir: str, name: Optional[str] = None
    ) -> "ClientBuilder":
        """DEPRECATED. project_dir should not be set by an argument,
        but it's okay for it to be set within this class for other reasons.

        Set the project directory path on the user's laptop.

        This sets the project code directory. If not specified, the project
        directory will be autodetected based on the current working directory.
        If no Anyscale project is found, the organization's default project will be used.
        In general the project directory will be synced to all nodes in the
        cluster as required by Ray, except for when the user passes
        "working_dir" in `.env()` in which case we sync the latter instead.

        Args:
            local_dir (str): path to the project directory.
            name (str): optional name to use if the project doesn't exist.

        Examples:
            >>> ray.init("anyscale://cluster_name", project_dir="~/my-proj-dir")
        """
        self._project_dir = os.path.abspath(os.path.expanduser(local_dir))
        self._project_name = name
        return self

    def session(self, cluster_name: str, update: bool = False) -> "ClientBuilder":
        """Set a fixed cluster name.

        Setting a fixed cluster name will create a new cluster if a cluster
        with cluster_name does not exist. Otherwise it will reconnect to an existing
        cluster.

        Args:
            cluster_name (str): fixed name of the cluster.
            update (bool): whether to update cluster configurations when
                connecting to an existing cluster. Note that this may restart
                the Ray runtime. By default update is set to False.

        Examples:
            >>> anyscale.session("prod_deployment", update=True).connect()
        """
        slugified_name = slugify(cluster_name)
        if slugified_name != cluster_name:
            self._log.error(
                f"Using `{slugified_name}` as the cluster name (instead of `{cluster_name}`)"
            )

        self._needs_update = update
        self._cluster_name = slugified_name

        return self

    def run_mode(self, run_mode: Optional[str] = None) -> "ClientBuilder":
        """Re-exec the driver program in the remote cluster or local docker.

        By setting ``run_mode("background")``, you can tell Anyscale
        to run the program driver remotely in the head node instead of executing
        locally. This allows you to e.g., close your laptop during development
        and have the program continue executing in the cluster.

        By setting ``run_mode("local_docker")``, you can tell Anyscale
        to re-exec the program driver in a local docker image, ensuring the
        driver environment will exactly match that of the remote cluster.

        You can also change the run mode by setting the ANYSCALE_BACKGROUND=1
        or ANYSCALE_LOCAL_DOCKER=1 environment variables. Changing the run mode
        is only supported for script execution. Attempting to change the run
        mode in a notebook or Python shell will raise an error.

        Args:
            run_mode (str): either None, "background", or "local_docker".

        Examples:
            >>> ray.init("anyscale://cluster_name", run_mode="background")
        """
        if run_mode not in [None, "background", "local_docker"]:
            raise ValueError("Unknown run mode {}".format(run_mode))
        if self._in_shell:
            if run_mode == "background":
                raise ValueError("Background mode is not supported in Python shells.")
            if run_mode == "local_docker":
                raise ValueError("Local docker mode is not supported in Python shells.")
        self._run_mode = run_mode
        return self

    def base_docker_image(self, image_name: str) -> None:
        """[DEPRECATED] Set the docker image to use for the cluster.
        IMPORTANT: the Python minor version of the manually specified docker
        image must match the local Python version.
        Args:
            image_name (str): docker image name.
        Examples:
            >>> anyscale.base_docker_image("anyscale/ray-ml:latest").connect()
        """
        raise ValueError(
            "Anyscale connect doesn't support starting clusters with base docker images. "
            "Please specify a cluster_env instead. For example: "
            '`ray.init("anyscale://cluster_name?cluster_env=name:1")`'
        )

    def require(self, requirements: Union[str, List[str]]) -> None:
        """[DEPRECATED] Set the Python requirements for the cluster.
        Args:
            requirements: either be a list of pip library specifications, or
            the path to a requirements.txt file.
        Examples:
            >>> anyscale.require("~/proj/requirements.txt").connect()
            >>> anyscale.require(["gym", "torch>=1.4.0"]).connect()
        """
        raise ValueError(
            "Anyscale connect no longer accepts the `.require()` argument."
            "Please specify these requirements in your runtime env instead."
            'For example `ray.init("anyscale://my_cluster", runtime_env({"pip":["chess"'
            ',"xgboost"]})`.'
        )

    def cluster_compute(
        self, cluster_compute: Union[str, CLUSTER_COMPUTE_DICT_TYPE]
    ) -> "ClientBuilder":
        """Set the Anyscale cluster compute to use for the cluster.

        Args:
            cluster_compute: Name of the cluster compute
                or a dictionary to build a new cluster compute.
                For example "my-cluster-compute".


        Examples:
            >>> ray.init("anyscale://cluster_name?cluster_compute=my_cluster_compute")
            >>> ray.init("anyscale://cluster_name", cluster_compute="my_cluster_compute")
            >>> ray.init("anyscale://cluster_name", cluster_compute={"cloud_id": "1234", ... })

        WARNING:
            If you want to pass a dictionary cluster_compute please pass it using
            the `cluster_compute` argument. Passing it in the URL format will not work.
        """
        if isinstance(cluster_compute, str):
            self._cluster_compute_name = cluster_compute  # type: ignore
        elif isinstance(cluster_compute, dict):
            self._cluster_compute_dict = copy.deepcopy(cluster_compute)  # type: ignore
        else:
            raise TypeError(
                "cluster_compute should either be Dict[str, Any] or a string."
            )
        return self

    def cluster_env(
        self, cluster_env: Union[str, CLUSTER_ENV_DICT_TYPE]
    ) -> "ClientBuilder":
        """TODO(ameer): remove app_config below after a few releases.
        Set the Anyscale cluster environment to use for the cluster.

        IMPORTANT: the Python minor version of the manually specified cluster
        environment must match the local Python version, and the Ray version must
        also be compatible with the one on the client. for example, if your local
        laptop environment is using ray 1.4 and python 3.8, then the cluster environment
        ray version must be 1.4 and python version must be 3.8.

        Args:
            cluster_env: Name (and optionally revision) of
                the cluster environment or a dictionary to build a new cluster environment.
                For example "my_cluster_env:2" where the revision would be 2.
                If no revision is specified, use the latest revision.
                NOTE: if you pass a dictionary it will always rebuild a new cluster environment
                before starting the cluster.

        Examples:
            >>> ray.init("anyscale://cluster_name?cluster_env=prev_created_cluster_env:2")
            >>> ray.init("anyscale://cluster_name", cluster_env="prev_created_cluster_env:2")
            >>> ray.init("anyscale://cluster_name", cluster_env={"base_image": "anyscale/ray-ml:1.1.0-gpu"})

        WARNING:
            If you want to pass a dictionary cluster environment please pass it using
            the `cluster_env` argument. Passing it in the URL format will not work.
        """
        self.app_config(cluster_env)
        return self

    def app_config(
        self, cluster_env: Union[str, CLUSTER_ENV_DICT_TYPE],
    ) -> "ClientBuilder":
        """Set the Anyscale app config to use for the session.

        IMPORTANT: the Python minor version of the manually specified app
        config must match the local Python version, and the Ray version must
        also be compatible with the one on the client.

        Args:
            cluster_env: Name (and optionally revision) of
            the cluster environment or a dictionary to build a new cluster environment.
            For example "my_cluster_env:2" where the revision would be 2.
            If no revision is specified, use the latest revision.

        Examples:
            >>> anyscale.app_config("prev_created_config:2").connect()
        """

        if self._build_commit or self._build_pr:
            raise ValueError("app_config() conflicts with build_from_source()")
        if isinstance(cluster_env, str):
            components = cluster_env.rsplit(":", 1)  # type: ignore
            self._cluster_env_name = components[0]
            if len(components) == 1:
                self._cluster_env_revision = None
            else:
                self._cluster_env_revision = int(components[1])
        elif isinstance(cluster_env, dict):
            cluster_env_copy: CLUSTER_ENV_DICT_TYPE = copy.deepcopy(cluster_env)  # type: ignore
            self._cluster_env_name = cluster_env_copy.pop("name", None)  # type: ignore
            self._cluster_env_dict = cluster_env_copy
        else:
            raise TypeError("The type of cluster_env must be either a str or a dict.")
        return self

    def download_results(self, *, remote_dir: str, local_dir: str) -> None:
        """Specify a directory to sync down from the cluster head node.

        IMPORTANT: the data is downloaded immediately after this call.
            `download_results` must not be called with `.connect()`. See examples below.

        Args:
            remote_dir (str): the result dir on the head node.
            local_dir (str): the local path to download the results to.

        Examples:
            >>> ray.client("anyscale://cluster_name")
            ...   .download_results(
            ...       local_dir="~/ray_results", remote_dir="/home/ray/proj_output")
            >>> ray.client("anyscale://").download_results(
            ...       local_dir="~/ray_results", remote_dir="/home/ray/proj_output")
            >>> anyscale.download_results(
            ...       local_dir="~/ray_results", remote_dir="/home/ray/proj_output")
        """
        if not self._ray.util.client.ray.is_connected():
            raise RuntimeError(
                "Not connected to cluster. Please re-run this after "
                'to a cluster via ray.client("anyscale://...").connect()'
            )

        self._download_results(remote_dir, local_dir)

    def autosuspend(
        self,
        enabled: bool = True,
        *,
        hours: Optional[int] = None,
        minutes: Optional[int] = None,
    ) -> "ClientBuilder":
        """Configure or disable cluster autosuspend behavior.

        The cluster will be autosuspend after the specified time period. By
        default, cluster auto terminate after one hour of idle.

        Args:
            enabled (bool): whether autosuspend is enabled.
            hours (int): specify idle time in hours.
            minutes (int): specify idle time in minutes. This is added to the
                idle time in hours.

        Examples:
            >>> ray.init("anyscale://cluster_name", autosuspend=-1) # to disable
            >>> ray.init("anyscale://cluster_name", autosuspend="2h")
        """
        if enabled:
            if hours is None and minutes is None:
                timeout = DEFAULT_AUTOSUSPEND_TIMEOUT
            else:
                timeout = 0
                if hours is not None:
                    timeout += hours * 60
                if minutes is not None:
                    timeout += minutes
        else:
            timeout = -1
        self._autosuspend_timeout = timeout
        return self

    def allow_public_internet_traffic(self, enabled: bool = False) -> "ClientBuilder":
        """Enable or disable public internet trafic for Serve deployments.

        Disabling public internet traffic causes the Serve deployments running on this cluster
        to be put behind an authentication proxy. By default, clusters will be started with
        Serve deployments rejecting internet traffic unless an authentication token is included
        in the cookies.

        Args:
            enabled (bool): whether public internet traffic is accepted for Serve deployments

        Examples:
            >>> ray.init("anyscale://cluster_name", allow_public_internet_traffic=True)
        """
        self._allow_public_internet_traffic = enabled
        return self

    def build_from_source(
        self,
        *,
        git_commit: Optional[str] = None,
        github_pr_id: Optional[int] = None,
        force_rebuild: bool = False,
    ) -> "ClientBuilder":
        """Build Ray from source for the cluster runtime.

        This is an experimental feature.

        Note that the first build for a new base image might take upwards of
        half an hour. Subsequent builds will have cached compilation stages.

        Args:
            git_commit (Optional[str]): If specified, try to checkout the exact
                git commit from the Ray master branch. If pull_request_id is
                also specified, the commit may be from the PR branch as well.
            github_pr_id (Optional[int]): Specify the pull request id to use.
                If no git commit is specified, the latest commit from the pr
                will be used.
            force_rebuild (bool): Force rebuild of the app config.

        Examples:
            >>> anyscale
            ...   .build_from_source(git_commit="f1e293c", github_pr_id=12345)
            ...   .connect()
        """
        if self._cluster_env_name:
            raise ValueError("cluster_env() conflicts with build_from_source()")
        self._build_commit = git_commit
        self._build_pr = github_pr_id
        self._force_rebuild = force_rebuild
        return self

    def request_resources(
        self,
        *,
        num_cpus: Optional[int] = None,
        num_gpus: Optional[int] = None,
        bundles: Optional[List[Dict[str, float]]] = None,
    ) -> "ClientBuilder":
        """Configure the initial resources to scale to.

        The cluster will immediately attempt to scale to accomodate the
        requested resources, bypassing normal upscaling speed constraints.
        The requested resources are pinned and exempt from downscaling.

        Args:
            num_cpus (int): number of cpus to request.
            num_gpus (int): number of gpus to request.
            bundles (List[Dict[str, float]): resource bundles to
                request. Each bundle is a dict of resource_name to quantity
                that can be allocated on a single machine. Note that the
                ``num_cpus`` and ``num_gpus`` args simply desugar into
                ``[{"CPU": 1}] * num_cpus`` and ``[{"GPU": 1}] * num_gpus``
                respectively.

        Examples:
            >>> ray.init("anyscale://cluster_name", request_cpus=200, request_gpus=30)
            >>> ray.init("anyscale://cluster_name", request_cpus=8,
            ...     request_bundles=[{"GPU": 8}, {"GPU": 8}, {"GPU": 1}],
            ... )
        """
        to_request: List[Dict[str, float]] = []
        if num_cpus:
            to_request += [{"CPU": 1}] * num_cpus
        if num_gpus:
            to_request += [{"GPU": 1}] * num_gpus
        if bundles:
            to_request += bundles
        self._initial_scale = to_request
        return self

    def _download_results(self, remote_dir: str, local_dir: str) -> None:
        # Determine the cluster's cluster ID by querying for the Anyscale Environment Variable
        # that is set on cluster startup. We achieve this by running a remote function against the cluster
        # using Ray Client.
        try:
            ray_id = self._ray.remote(
                lambda: os.environ.get("ANYSCALE_SESSION_ID")
            ).remote()
            cluster_id = self._ray.get(ray_id)
            cluster_name = self._anyscale_sdk.get_session(cluster_id).result.name
        except Exception as e:
            self._log.error(f"Failed to get ClusterID with error: {e}")
            raise RuntimeError(
                "Unable to get ClusterID for `download_results`!"
            ) from None
        self._session_controller.pull(cluster_name, source=remote_dir, target=local_dir)

    def _ensure_project_setup_at_dir(
        self, project_dir: str, project_name: Optional[str]
    ) -> Tuple[str, str]:
        """
        TODO(nikita): This method has been moved to anyscale.connect_utils.ProjectBlock.
        Call create_project_block and delete this method from connect.py.

        Get or create an Anyscale project rooted at the given dir.

        Returns:
        The project id and project name of the project being used.
        """
        os.makedirs(project_dir, exist_ok=True)
        if project_name is None:
            project_name = os.path.basename(project_dir)

        # If the project yaml exists, assume we're already setup.
        project_yaml = os.path.join(project_dir, ".anyscale.yaml")
        if os.path.exists(project_yaml):
            proj_def = anyscale.project.ProjectDefinition(project_dir)
            project_id: Optional[str] = anyscale.project.get_project_id(proj_def.root)
            project_response = self._anyscale_sdk.get_project(project_id)
            assert project_id
            self._log.info(
                ".anyscale.yaml found in project_dir. Directory is attached to a project."
            )
            return project_id, project_response.result.name

        project_id = find_project_id(self._anyscale_sdk, project_name)
        if project_id is None:
            self._log.info(
                f"Creating new project named {project_name} for local dir {project_dir}"
            )
            project_response = self._anyscale_sdk.create_project(
                {
                    "name": project_name,
                    "description": "Automatically created by Anyscale Connect",
                }
            )
            project_id = project_response.result.id
        else:
            self._log.info(
                f"Connecting local dir {project_dir} to project", project_name
            )

        if not os.path.exists(project_yaml):
            with open(project_yaml, "w+") as f:
                f.write(yaml.dump({"project_id": project_id}))

        return project_id, project_name

    def _log_cluster_configs(
        self, cluster_name: str, build_id: str, compute_template_id: str, url: str
    ) -> None:
        """Prints cluster name/env/compute to the user of the newly launched cluster."""

        cluster_env = self._anyscale_sdk.get_build(build_id).result
        # The SDK uses application_template_id but this is really just the cluster_env_name.
        cluster_env_name = (
            cluster_env.application_template_id + ":" + str(cluster_env.revision)
        )

        cluster_compute_name = self._anyscale_sdk.get_compute_template(
            compute_template_id
        ).result.name
        self._log.info(
            f"Starting cluster {cluster_name} with cluster_env={cluster_env_name} and cluster_compute={cluster_compute_name}. View at {url}"
        )

    def _start_session(
        self,
        project_id: str,
        cluster_name: str,
        build_id: str,
        compute_template_id: str,
    ) -> None:
        """
        TODO(nikita): This method has been moved to anyscale.connect_utils.prepare_cluster.
        Call create_prepare_cluster_block and delete this method from connect.py.

        Start cluster from sdk. Create/update the cluster if required."""
        session, start_required = self._create_or_update_session_data(
            cluster_name,
            project_id,
            build_id,
            compute_template_id,
            self._autosuspend_timeout,
            bool(self._allow_public_internet_traffic),
        )

        url = get_endpoint(f"/projects/{project_id}/clusters/{session.id}")

        if start_required:
            self._log_cluster_configs(
                cluster_name=cluster_name,
                build_id=build_id,
                compute_template_id=compute_template_id,
                url=url,
            )
            self._anyscale_sdk.start_cluster(
                session.id,
                StartClusterOptions(
                    cluster_environment_build_id=build_id,
                    cluster_compute_id=compute_template_id,
                    allow_public_internet_traffic=self._allow_public_internet_traffic,
                ),
            )

            wait_for_session_start(project_id, cluster_name, self._api_client)
            self._log.debug(f"Cluster {cluster_name} finished starting. View at {url}")
        else:
            self._log.info(
                f"Cluster {cluster_name} does not need to be restarted. Connecting to {url}"
            )

    def _create_or_update_session_data(
        self,
        cluster_name: str,
        project_id: str,
        build_id: str,
        compute_template_id: str,
        idle_timeout: Optional[int],
        allow_public_internet_traffic: bool = False,
    ) -> Session:
        """
        TODO(nikita): This method has been moved to anyscale.connect_utils.prepare_cluster.
        Call create_prepare_cluster_block and delete this method from connect.py.

        Creates new cluster with cluster env if cluster with `cluster_name` doesn't
        already exist. Otherwise, update the `idle_timeout` of the existing
        cluster if provided.
        """

        start_required = True
        cluster_list = self._api_client.list_sessions_api_v2_sessions_get(
            project_id=project_id, active_only=False, name=cluster_name
        ).results

        cluster_exists = len(cluster_list) > 0
        if not cluster_exists:
            # Create a new cluster if there is no existing cluster with the given cluster_name
            create_cluster_data = CreateCluster(
                name=cluster_name,
                project_id=project_id,
                cluster_environment_build_id=build_id,
                cluster_compute_id=compute_template_id,
                idle_timeout_minutes=idle_timeout,
                allow_public_internet_traffic=allow_public_internet_traffic,
            )
            cluster = self._anyscale_sdk.create_cluster(create_cluster_data).result
        else:
            # Get the existing cluster and update the idle_timeout if required
            cluster = cluster_list[0]
            if cluster.state == "Running":
                start_required = self._validate_new_cluster_compute_and_env_match_existing_cluster(
                    project_id, cluster_name, print_warnings=False
                )
            if idle_timeout:
                self._anyscale_sdk.update_cluster(
                    cluster.id, UpdateCluster(idle_timeout_minutes=idle_timeout)
                )

        return cluster, start_required

    def _get_organization_default_cloud(self) -> Optional[str]:
        """
        TODO(nikita): This method has been moved to anyscale.connect_utils.prepare_cluster.
        Call create_prepare_cluster_block and delete this method from connect.py.

        Return default cloud name for organization if it exists and
        if user has correct permissions for it.

        Returns:
            Name of default cloud name for organization if it exists and
            if user has correct permissions for it.
        """
        user = self._api_client.get_user_info_api_v2_userinfo_get().result
        organization = user.organizations[0]  # Each user only has one org
        if organization.default_cloud_id:
            try:
                # Check permissions
                _, cloud_name = get_cloud_id_and_name(
                    self._api_client, cloud_id=organization.default_cloud_id
                )
                return str(cloud_name)
            except Exception:
                return None
        return None

    def _get_all_clouds(self) -> List[Cloud]:
        """
        TODO(nikita): This method has been moved to anyscale.connect_utils.prepare_cluster.
        Call create_prepare_cluster_block and delete this method from connect.py.

        Fetches all Clouds the user has access to.

        Returns:
            List of all Clouds the user has access to.
        """

        cloud_list_response = self._anyscale_sdk.search_clouds(
            {"paging": {"count": 50}}
        )
        all_clouds = cloud_list_response.results
        next_paging_token = cloud_list_response.metadata.next_paging_token

        while next_paging_token:
            cloud_list_response = self._anyscale_sdk.search_clouds(
                {"paging": {"count": 50, "paging_token": next_paging_token}}
            )
            next_paging_token = cloud_list_response.metadata.next_paging_token
            all_clouds.extend(cloud_list_response.results)

        return all_clouds  # type: ignore

    def _get_last_used_cloud(self, project_id: str) -> str:
        """
        TODO(nikita): This method has been moved to anyscale.connect_utils.prepare_cluster.
        Call create_prepare_cluster_block and delete this method from connect.py.

        Return the name of the cloud last used in the project.

        Args:
            project_id (str): The project to get the last used cloud for.

        Returns:
            Name of the cloud last used in this project.
        """
        # TODO(pcm): Get rid of this and the below API call in the common case where
        # we can determine the cloud to use in the backend.
        cloud_id = self._anyscale_sdk.get_project(project_id).result.last_used_cloud_id
        if cloud_id:
            try:
                cloud = self._anyscale_sdk.get_cloud(cloud_id).result
            except Exception as e:
                msg = f"Failed to fetch Cloud with id: {cloud_id}."
                self._log.error(msg)
                self._log.debug(e)
                raise RuntimeError(msg)
        else:
            clouds = self._get_all_clouds()
            if len(clouds) > 0:
                # Clouds are sorted in descending order, pick the oldest one as default.
                cloud = clouds[-1]
            else:
                msg = "No cloud configured, please set up a cloud with 'anyscale cloud setup'."
                self._log.error(msg)
                raise RuntimeError(msg)

        cloud_name = cloud.name
        self._log.debug(
            (
                f"Using last active cloud '{cloud_name}'. "
                "Call anyscale.cloud('...').connect() to overwrite."
            )
        )
        return cast(str, cloud_name)

    def _create_cluster(  # noqa: C901
        self,
        project_id: str,
        build_id: str,
        compute_template_id: str,
        cluster_name: Optional[str],
    ) -> str:
        """
        TODO(nikita): This method has been moved to anyscale.connect_utils.prepare_cluster.
        Call create_prepare_cluster_block and delete this method from connect.py.

        Create/start a terminated (or does not exist) cluster.

        Args:
            project_id (str): The project to use.
            build_id (str): Build to start cluster with.
            compute_template_id (str): Compute template to start cluster with
            cluster_name (Optional[str]): If specified, the given cluster
                will be created or updated as needed. Otherwise the cluster
                name will be picked automatically.

        Returns:
            The name of the cluster to connect to.
        """
        ray_cli = self._ray.util.client.ray
        if not cluster_name:
            results = self._list_sessions(project_id=project_id)
            self._log.debug("-> Starting a new cluster")
            used_names = [s.name for s in results]
            for i in range(MAX_CLUSTERS):
                name = "cluster-{}".format(i)
                if name not in used_names:
                    cluster_name = name
                    self._log.debug("Starting cluster", cluster_name)
                    break

        # Should not happen.
        if cluster_name is None:
            raise RuntimeError(
                "Could not create new cluster to connect to. "
                "We automatically generate cluster names cluster-1, cluster-2, ..., "
                f"cluster-{MAX_CLUSTERS}. Consider providing an explicit "
                'cluster name e.g., ray.init("anyscale://cluster_name") or deleting some of these clusters.'
            )

        self._log.debug(
            f"Updating {cluster_name} to use build id {build_id} and compute template id {compute_template_id}"
        )
        # TODO(ekl): race condition here since "up" breaks the lock.
        if ray_cli.is_connected():
            self._ray.util.disconnect()
        # Update cluster.
        self._log.debug("Starting cluster with sdk and compute config.")
        self._start_session(
            project_id=project_id,
            cluster_name=cluster_name,
            build_id=build_id,
            compute_template_id=compute_template_id,
        )

        return cluster_name

    def _acquire_session_lock(
        self,
        session_meta: Session,
        connection_retries: int,
        job_config: Optional[Any] = None,
        allow_multiple_clients: bool = False,
    ) -> Dict[str, Any]:
        """
        TODO(nikita): This method has been moved to anyscale.connect_utils.start_interactive_session.
        Call start_interactive_session_block and delete this method from connect.py.

        Connect to and acquire a lock on the cluster.

        The cluster lock is released by calling disconnect() on the returned
        Ray connection. This function also checks for Python version
        compatibility, it will not acquire the lock on version mismatch.

        """
        try:
            session_url, secure, metadata = self._get_connect_params(session_meta)
            if connection_retries > 0:
                self._log.debug("Beginning connection attempts")
            # Disable retries when acquiring cluster lock for fast failure.
            self._log.debug(
                "Info: ", session_url, secure, metadata, connection_retries, job_config,
            )
            if job_config is not None:
                self._log.debug("RuntimeEnv", job_config.runtime_env)
            connect_kwargs = {
                "secure": secure,
                "metadata": metadata,
                "connection_retries": connection_retries,
                "job_config": job_config,
                "ignore_version": True,
            }
            if self._ray_init_kwargs:
                connect_kwargs["ray_init_kwargs"] = self._ray_init_kwargs

            # Connect without job config first to get version info. Ray 1.7's
            # job config implementation hangs on Ray 1.6, and Ray 1.8 runtime
            # envs are incompatible with 1.7.
            without_job_config = dict(connect_kwargs)
            del without_job_config["job_config"]
            info = self._ray.util.connect(session_url, **without_job_config)
            self._ray.util.disconnect()  # Disconnect to drop session lock
            self._dynamic_check(info)

            # If dynamic version check passes, then reconnect with the job_config
            info = self._ray.util.connect(session_url, **connect_kwargs)
            self._log.debug("Connected server info: ", info)
        except Exception as connection_exception:
            self._log.debug(
                "Connection error after {} retries".format(connection_retries)
            )
            ray_info = None
            try:
                self._log.info(
                    "Connection Failed! Attempting to get Debug Information!"
                )
                py_command = """import ray; import json; print(json.dumps({"ray_commit" : ray.__commit__, "ray_version" :ray.__version__}))"""
                output = self._subprocess.check_output(
                    [
                        "anyscale",
                        "exec",
                        "--session-name",
                        self._cluster_name,
                        "--",
                        "python",
                        "-c",
                        shlex.quote(py_command),
                    ],
                    stderr=subprocess.DEVNULL,
                )
                re_match = re.search("{.*}", output.decode())
                if re_match:
                    ray_info = json.loads(re_match.group(0))
            except Exception as inner_exception:
                self._log.debug(f"Failed to get debug info: {inner_exception}")

            if ray_info is not None:
                check_required_ray_version(
                    self._log,
                    self._ray.__version__,
                    self._ray.__commit__,
                    ray_info["ray_version"],
                    ray_info["ray_commit"],
                    self._ignore_version_check,
                )

            raise connection_exception

        if info["num_clients"] > 1 and (not allow_multiple_clients):
            self._log.debug(
                "Failed to acquire lock due to too many connections: ",
                info["num_clients"],
            )
            self._ray.util.disconnect()
        return info

    def _check_connection(self, project_id: str, cluster_name: str) -> None:
        """Check the connected cluster to make sure it's good"""
        # TODO(nikita): This method has been moved to anyscale.connect_utils.start_interactive_session.
        # Call start_interactive_session_block and delete this method from connect.py.
        if not self._ray.util.client.ray.is_connected():
            raise RuntimeError("Failed to acquire cluster we created")
        cluster_found = self._get_cluster_or_die(project_id, cluster_name)

        def func() -> str:
            return "Connected!"

        f_remote = self._ray.remote(func)
        ray_ref = f_remote.remote()
        self._log.debug(self._ray.get(ray_ref))
        self._log.info(
            "Connected to {}, see: {}".format(
                cluster_name,
                get_endpoint(f"/projects/{project_id}/clusters/{cluster_found.id}"),
            )
        )
        host_name = None
        try:
            host_name = cluster_found.host_name
            # like "https://session-fqsx0p3pzfna71xxxxxxx.anyscaleuserdata.com"
        except AttributeError:
            pass
        if not host_name:
            jupyter_notebook_url = cluster_found.jupyter_notebook_url
            if jupyter_notebook_url:
                # TODO(aguo): Delete this code... eventually. Once majority of sessions have host_name in the DB
                host_name = "https://{}".format(
                    jupyter_notebook_url.split("/")[2].lower()
                )
        if host_name:
            self._log.info("URL for head node of cluster: {}".format(host_name))

    def _get_cluster_or_die(self, project_id: str, session_name: str) -> Session:
        """Query Anyscale for the given cluster's metadata."""
        cluster_found = get_cluster(self._anyscale_sdk, project_id, session_name)
        if not cluster_found:
            raise RuntimeError("Failed to locate cluster: {}".format(session_name))
        return cluster_found

    def _get_connect_params(self, session_meta: Session) -> Tuple[str, bool, Any]:
        """Get the params from the cluster needed to use Ray client."""
        # TODO(nikita): This method has been moved to anyscale.connect_utils.start_interactive_session.
        # Call start_interactive_session_block and delete this method from connect.py.
        connect_url = None
        metadata = [("cookie", "anyscale-token=" + session_meta.access_token)]
        if session_meta.connect_url:
            url_components = session_meta.connect_url.split("?port=")
            metadata += [("port", url_components[1])] if len(url_components) > 1 else []
            connect_url = url_components[0]
        else:
            # This code path can go away once all sessions use session_meta.connect_url:
            # TODO(nikita): Use the service_proxy_url once it is fixed for anyscale up with file mounts.
            full_url = session_meta.jupyter_notebook_url
            assert (
                full_url is not None
            ), f"Unable to determine URL for Session: {session_meta.name}, please retry shortly or try a different session."
            # like "session-fqsx0p3pzfna71xxxxxxx.anyscaleuserdata.com"
            connect_url = full_url.split("/")[2].lower() + ":8081"
            metadata += [("port", "10001")]

        if self._secure:
            connect_url = connect_url.replace(":8081", "")

        return connect_url, self._secure, metadata

    def _get_cluster_compute_id_from_name(
        self, project_id: str, cluster_compute_name: str
    ) -> str:
        """
        TODO(nikita): This method has been moved to anyscale.connect_utils.prepare_cluster.
        Call create_prepare_cluster_block and delete this method from connect.py.

        Gets the cluster compute id given a cluster name.
        """
        cluster_computes = self._api_client.search_compute_templates_api_v2_compute_templates_search_post(
            ComputeTemplateQuery(
                orgwide=True,
                name={"equals": cluster_compute_name},
                include_anonymous=True,
            )
        ).results
        if len(cluster_computes) == 0:
            raise ValueError(
                f"The cluster compute template {cluster_compute_name}"
                " is not registered."
            )
        return cluster_computes[0].id

    def _register_compute_template(
        self, project_id: str, config_object: ComputeTemplateConfig
    ) -> str:
        """
        TODO(nikita): This method has been moved to anyscale.connect_utils.prepare_cluster.
        Call create_prepare_cluster_block and delete this method from connect.py.

        Register compute template with a default name and return the compute template id.
        """
        created_template = self._api_client.create_compute_template_api_v2_compute_templates_post(
            create_compute_template=CreateComputeTemplate(
                name="connect-autogenerated-config-{}".format(
                    datetime.now().isoformat()
                ),
                project_id=project_id,
                config=config_object,
                anonymous=True,
            )
        ).result
        compute_template_id = str(created_template.id)
        return compute_template_id

    def _wait_for_app_build(self, project_id: str, build_id: str) -> Build:
        """
        TODO(nikita): This method has been moved to anyscale.connect_utils.prepare_cluster.
        Call create_prepare_cluster_block and delete this method from connect.py.
        """
        has_logged = False
        while True:
            build = self._anyscale_sdk.get_build(build_id).result
            if build.status in ["pending", "in_progress"]:
                if not has_logged:
                    url = get_endpoint(
                        f"projects/{project_id}/app-config-details/{build_id}"
                    )
                    self._log.info(
                        f"Waiting for cluster env to be built (see {url} for progress)..."
                    )
                    has_logged = True
                time.sleep(10.0)
            elif build.status in ["failed", "pending_cancellation", "canceled"]:
                raise RuntimeError(
                    "Cluster env status is '{}', please select another revision!".format(
                        build.status
                    )
                )
            else:
                assert build.status == "succeeded"
                return build

    def _get_cluster_env_build(
        self, project_id: str, cluster_env_name: str, clust_env_revision: Optional[int]
    ) -> Build:
        """
        TODO(nikita): This method has been moved to anyscale.connect_utils.prepare_cluster.
        Call create_prepare_cluster_block and delete this method from connect.py.
        """
        app_template_id = None
        cluster_environments = self._list_app_configs(name_contains=cluster_env_name)
        for cluster_env in cluster_environments:
            if cluster_env.name == cluster_env_name:
                app_template_id = cluster_env.id
        if not app_template_id:
            cluster_environments = self._list_app_configs()
            if len(cluster_environments) < 10:
                cluster_envs_error_message = "Available cluster environments: {}".format(
                    ", ".join(c.name for c in cluster_environments)
                )
            else:
                cluster_envs_error_message = "See environments at {}".format(
                    get_endpoint("/configurations/?tab=cluster-env")
                )
            raise RuntimeError(
                "Cluster Environment '{}' not found. ".format(cluster_env_name)
                + cluster_envs_error_message
            )
        builds = self._list_builds(app_template_id)

        build_to_use = None
        if clust_env_revision:
            for build in builds:
                if build.revision == clust_env_revision:
                    build_to_use = build

            if not build_to_use:
                raise RuntimeError(
                    "Revision {} of cluster environment '{}' not found.".format(
                        clust_env_revision, cluster_env_name
                    )
                )
        else:
            latest_build_revision = -1
            for build in builds:
                if build.revision > latest_build_revision:
                    latest_build_revision = build.revision
                    build_to_use = build
            self._log.debug(
                "Using latest revision {} of {}".format(
                    latest_build_revision, cluster_env_name
                )
            )
        assert build_to_use  # for mypy
        return build_to_use

    def _build_app_config_from_source(self, project_id: str) -> str:
        """
        TODO(nikita): This method has been moved to anyscale.connect_utils.prepare_cluster.
        Call create_prepare_cluster_block and delete this method from connect.py.
        """

        config_name = "ray-build-{}-{}".format(self._build_pr, self._build_commit)
        # Force creation of a unique app config.
        if self._force_rebuild:
            config_name += "-{}".format(int(time.time()))
        app_templates = self._list_app_configs(name_contains=config_name)
        found = any(a.name == config_name for a in app_templates)
        if not found:
            build_steps = BUILD_STEPS.copy()
            # Add a unique command to bust the Makisu cache if needed.
            # Otherwise we could end up caching a previous fetch.
            build_steps.append("echo UNIQUE_ID={}".format(config_name))
            if self._build_pr:
                build_steps.append(
                    "cd ray && git fetch origin pull/{}/head:target && "
                    "git checkout target".format(self._build_pr)
                )
            if self._build_commit:
                build_steps.append(
                    "cd ray && git checkout {}".format(self._build_commit)
                )
            build_steps.append(
                'cd ray/python && sudo env "PATH=$PATH" python setup.py develop'
            )
            self._anyscale_sdk.create_app_config(
                {
                    "name": config_name,
                    "project_id": project_id,
                    "config_json": {
                        "base_image": _get_base_image("ray", "nightly", "cpu"),
                        "debian_packages": ["curl", "unzip", "zip", "gnupg"],
                        "post_build_cmds": build_steps,
                    },
                }
            )
        return config_name

    def _exec_self_in_head_node(self) -> None:
        """Run the current main file in the head node."""
        cur_file = os.path.abspath(sys.argv[0])
        # TODO(ekl) it would be nice to support keeping the original file name,
        # but "anyscale push" isn't escaping e.g., spaces correctly.
        tmp_file = "/tmp/anyscale-connect-{}.py".format(uuid.uuid4().hex)
        cur_dir = os.getcwd()
        try:
            assert self._project_dir is not None
            os.chdir(self._project_dir)

            self._session_controller.push(
                self._cluster_name,
                source=cur_file,
                target=tmp_file,
                config=None,
                all_nodes=False,
            )

            self._exec_controller.anyscale_exec(
                self._cluster_name,  # type: ignore
                screen=False,
                tmux=False,
                port_forward=(),  # type: ignore
                sync=False,
                stop=False,
                terminate=False,
                commands=["python", tmp_file] + sys.argv[1:],
            )
        finally:
            os.chdir(cur_dir)
        self._os._exit(0)

    def _exec_self_in_local_docker(self) -> None:
        """Run the current main file in a local docker image."""
        cur_file = os.path.abspath(sys.argv[0])
        docker_image = _get_base_image("ray-ml", MINIMUM_RAY_VERSION, "cpu")
        command = [
            "docker",
            "run",
            "--env",
            "ANYSCALE_HOST={}".format(
                anyscale.shared_anyscale_utils.conf.ANYSCALE_HOST
            ),
            "--env",
            "ANYSCALE_CLI_TOKEN={}".format(self._credentials),
            "-v",
            "{}:/user_main.py".format(cur_file),
            "--entrypoint=/bin/bash",
            docker_image,
            "-c",
            "python /user_main.py {}".format(
                " ".join([shlex.quote(x) for x in sys.argv[1:]])
            ),
        ]
        self._log.debug("Running", command)
        self._subprocess.check_call(command)
        self._os._exit(0)

    def _list_sessions(self, project_id: str) -> List[Session]:
        return list_entities(self._anyscale_sdk.list_sessions, project_id)

    def _list_app_configs(
        self, project_id: Optional[str] = None, name_contains: Optional[str] = None
    ) -> List[AppConfig]:
        entities = []
        has_more = True
        paging_token = None
        while has_more:
            resp = self._anyscale_sdk.list_app_configs(
                project_id=project_id,
                name_contains=name_contains,
                count=50,
                paging_token=paging_token,
            )
            entities.extend(resp.results)
            paging_token = resp.metadata.next_paging_token
            has_more = paging_token is not None
        return entities

    def _list_builds(self, application_template_id: str) -> List[Build]:
        return list_entities(self._anyscale_sdk.list_builds, application_template_id)

    def _dynamic_check(self, info: Dict[str, str]) -> None:
        # TODO(nikita): This method has been moved to anyscale.connect_utils.start_interactive_session.
        # Call start_interactive_session_block and delete this method from connect.py.
        check_required_ray_version(
            self._log,
            self._ray.__version__,
            self._ray.__commit__,
            info["ray_version"],
            info["ray_commit"],
            self._ignore_version_check,
        )

        # NOTE: This check should not be gated with IGNORE_VERSION_CHECK, because this is
        # replacing Ray Client's internal check.
        local_major_minor = detect_python_minor_version()
        client_version = f"{local_major_minor}.{sys.version_info[2]}"
        server_version = info["python_version"]
        assert server_version.startswith(
            local_major_minor
        ), f"Python minor versions differ between client ({client_version}) and server ({server_version}). Please ensure that they match."


# This implements the following utility function for users:
# $ pip install -U `python -m anyscale.connect required_ray_version`
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "required_ray_version":
        # TODO(ilr/nikita) Make this >= MINIMUM VERSION when we derive MINIMUM VERSION
        # from the backend.
        print(f"ray=={MINIMUM_RAY_VERSION}")
    else:
        raise ValueError("Unsupported argument.")
