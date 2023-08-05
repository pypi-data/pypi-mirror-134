from datetime import datetime
import inspect
import logging
import os
from pathlib import Path
import platform
import sys
from typing import Any, Callable, Dict, List, Optional, Tuple
from unittest.mock import ANY, call, Mock, patch

from packaging import version
import pytest
import ray
import requests
import yaml

import anyscale
from anyscale.client.openapi_client import SessionListResponse
from anyscale.client.openapi_client.models.app_config import AppConfig
from anyscale.client.openapi_client.models.build import Build
from anyscale.client.openapi_client.models.project import Project
from anyscale.client.openapi_client.models.project_response import ProjectResponse
from anyscale.client.openapi_client.models.session import Session
from anyscale.connect import (
    _is_in_shell,
    AnyscaleClientConnectResponse,
    AnyscaleClientContext,
    ClientBuilder,
)
from anyscale.sdk.anyscale_client import (
    ComputeTemplateConfig,
    StartClusterOptions,
    UpdateCluster,
)
from anyscale.sdk.anyscale_client.models import ListResponseMetadata
from anyscale.sdk.anyscale_client.models.cloud_list_response import CloudListResponse
from anyscale.sdk.anyscale_client.models.cloud_response import CloudResponse
from anyscale.util import get_wheel_url
import anyscale.utils.runtime_env


RAY_VERSION = "1.6.0"
RAY_COMMIT = "7916500c43de46721c51e6b95fb51cfa2c6078ba"


def _make_session(i: int, state: str, cloud_id: str = None) -> Session:
    sess = Session(
        id="session_id",
        name="cluster-{}".format(i),
        created_at=datetime.now(),
        ray_dashboard_url="https://fake_dashboard.com",
        snapshots_history=[],
        idle_timeout=120,
        tensorboard_available=False,
        project_id="project_id",
        state=state,
        cloud_id=cloud_id,
        service_proxy_url="http://session-{}.userdata.com/auth?token=value&bar".format(
            i
        ),
        connect_url="session-{}.userdata.com:8081?port=10001".format(i),
        jupyter_notebook_url="http://session-{}.userdata.com/jupyter/lab?token=value".format(
            i
        ),
        access_token="value",
        host_name="https://session-{}.userdata.com".format(i),
    )
    sess.build_id = "build_id"
    sess.compute_template_id = "mock_compute_template_id"
    return sess


def _make_app_template() -> AppConfig:
    return AppConfig(
        project_id="project_id",
        id="application_template_id",
        name="test-app-config",
        creator_id="creator_id",
        organization_id="organization_id",
        created_at=datetime.now(),
        last_modified_at=datetime.now(),
    )


def _make_build() -> Build:
    return Build(
        id="build_id",
        revision=0,
        application_template_id="application_template_id",
        config_json="",
        creator_id="creator_id",
        status="succeeded",
        created_at=datetime.now(),
        last_modified_at=datetime.now(),
        docker_image_name="docker_image_name",
    )


def _make_compute_template_config() -> ComputeTemplateConfig:

    return ComputeTemplateConfig(
        **{
            "cloud_id": "fake-cloud-id",
            "region": "fake-region",
            "allowed_azs": ["fake-az1"],
            "head_node_type": {
                "name": "head-node-name",
                "instance_type": "fake-head-instance-type",
                "resources": {
                    "cpu": 3,
                    "object_store_memory": 5,
                    "custom_resources": {
                        "custom_resource_1": 10,
                        "custom_resource_2": 12,
                    },
                },
            },
            "worker_node_types": [
                {
                    "name": "worker-node-name",
                    "instance_type": "fake-worker-instance-type",
                    "min_workers": 0,
                    "max_workers": 10,
                    "use_spot": True,
                    "resources": {"cpu": 7, "memory": 11},
                }
            ],
            "aws": {
                "SubnetId": "fake-subnet-id",
                "SecurityGroupIds": ["fake-security-group-id"],
                "IamInstanceProfile": {"Arn": "fake-iam-arn"},
                "TagSpecifications": [
                    {
                        "ResourceType": "instance",
                        "Tags": [{"Key": "fake-key", "Value": "fake-value"}],
                    },
                ],
            },
        }
    )


def _connected(ray: Mock, ret: Dict[str, Any],) -> Callable[[Any, Any], Dict[str, Any]]:
    def connected(*a: Any, **kw: Any) -> Dict[str, Any]:
        ray.util.client.ray.is_connected.return_value = True
        returnable = {
            "num_clients": 1,
            "ray_version": RAY_VERSION,
            "ray_commit": RAY_COMMIT,
            "python_version": platform.python_version(),
            "protocol_version": "fake_version",
        }
        returnable.update(**ret)
        return returnable

    return connected


@pytest.fixture()
def mock_auth_api_client(
    base_mock_api_client: Mock, base_mock_anyscale_api_client: Mock
):
    mock_auth_api_client = Mock(
        api_client=base_mock_api_client,
        anyscale_api_client=base_mock_anyscale_api_client,
    )
    with patch.multiple(
        "anyscale.controllers.base_controller",
        get_auth_api_client=Mock(return_value=mock_auth_api_client),
    ):
        yield


def _make_test_builder(
    tmp_path: Path,
    session_states: Optional[List[str]] = None,
    setup_project_dir: bool = True,
    create_build: bool = True,
    cloud_id: str = None,
) -> Tuple[Any, Any, Any, Any]:
    if session_states is None:
        session_states = ["Running"]

    scratch = tmp_path / "scratch"
    sdk = Mock()
    sess_resp = Mock()
    ray = Mock()

    ray.__commit__ = RAY_COMMIT
    ray.__version__ = RAY_VERSION
    ray.util.client.ray.is_connected.return_value = False
    anyscale.utils.runtime_env.runtime_env_setup = Mock()

    def disconnected(*a: Any, **kw: Any) -> None:
        ray.util.client.ray.is_connected.return_value = False

    # Emulate session lock failure.
    ray.util.connect.side_effect = _connected(ray, {"num_clients": 1})
    ray.util.disconnect.side_effect = disconnected
    job_config_mock = Mock()
    job_config_mock.runtime_env = {}
    job_config_mock.set_runtime_env.return_value = Mock()
    job_config_mock.metadata = {}
    ray.job_config.JobConfig.return_value = job_config_mock
    sess_resp.results = [
        _make_session(i, state, cloud_id) for i, state in enumerate(session_states)
    ]
    sess_resp.metadata.next_paging_token = None
    sdk.list_sessions.return_value = sess_resp
    sdk.search_sessions.return_value = sess_resp
    proj_resp = Mock()
    proj_resp.result.name = "scratch"
    sdk.get_project.return_value = proj_resp
    sdk.get_build = Mock(return_value=Mock(result=_make_build()))
    subprocess = Mock()
    _os = Mock()
    _api_client = Mock()
    _api_client.get_user_info_api_v2_userinfo_get.return_value.result = Mock(
        organizations=[Mock(default_cloud_id=None)]
    )
    _api_client.get_default_cluster_env_build_api_v2_builds_default_py_version_ray_version_get = Mock(
        return_value=Mock(result=_make_build())
    )
    _anyscale_api_client = Mock()
    _auth_api_client = Mock(
        api_client=_api_client, anyscale_api_client=_anyscale_api_client
    )
    with patch.multiple(
        "anyscale.controllers.base_controller",
        get_auth_api_client=Mock(return_value=_auth_api_client),
    ):
        builder = ClientBuilder(
            anyscale_sdk=sdk,
            subprocess=subprocess,
            _ray=ray,
            _os=_os,
            _ignore_version_check=False,
            auth_api_client=_auth_api_client,
        )
    builder._exec_controller.api_client = _api_client
    builder._exec_controller.anyscale_api_client = _anyscale_api_client
    builder._session_controller.api_client = _api_client
    builder._session_controller.anyscale_api_client = _anyscale_api_client
    if setup_project_dir:
        builder.project_dir(scratch.absolute().as_posix())
    else:
        builder._in_shell = True
    sdk.search_projects = lambda _: SessionListResponse(results=[])
    builder._find_project_id = lambda _: None  # type: ignore

    def create_session(*a: Any, **kw: Any) -> None:
        sess_resp.results = sess_resp.results + [
            _make_session(len(sess_resp.results), "Running")
        ]
        sdk.list_sessions.return_value = sess_resp

    setattr(builder, "_start_session", Mock())
    builder._start_session.side_effect = create_session  # type: ignore
    builder._register_compute_template = Mock(return_value="mock_compute_template_id")  # type: ignore

    setattr(
        builder, "_get_last_used_cloud", Mock(return_value="anyscale_default_cloud")
    )

    if create_build:
        _make_app_template()
        mock_build = _make_build()
        builder._get_cluster_env_build = Mock(return_value=mock_build)  # type: ignore

    return builder, sdk, subprocess, ray


def test_parse_address(mock_auth_api_client) -> None:
    """Tests ClientBuilder._parse_address which parses the anyscale address."""

    sdk = Mock()
    _api_client = Mock()
    connect_instance = ClientBuilder(
        anyscale_sdk=sdk,
        auth_api_client=Mock(api_client=_api_client, anyscale_api_client=Mock()),
    )

    connect_instance._parse_address(None)
    assert connect_instance._cluster_name is None
    assert connect_instance._autosuspend_timeout is None
    assert connect_instance._cluster_compute_name is None
    assert connect_instance._cluster_env_name is None

    connect_instance._parse_address("")
    assert connect_instance._cluster_name is None
    assert connect_instance._autosuspend_timeout is None
    assert connect_instance._cluster_compute_name is None
    assert connect_instance._cluster_env_name is None

    connect_instance._parse_address("cluster_name")
    assert connect_instance._cluster_name == "cluster_name"
    assert connect_instance._autosuspend_timeout is None
    assert connect_instance._cluster_compute_name is None
    assert connect_instance._cluster_env_name is None

    connect_instance._parse_address(
        "my_cluster?cluster_compute=my_template&autosuspend=5&cluster_env=bla:1&update=True"
    )
    assert connect_instance._cluster_name == "my_cluster"
    assert connect_instance._autosuspend_timeout == 5
    assert connect_instance._cluster_compute_name == "my_template"
    assert connect_instance._cluster_env_name == "bla"
    assert connect_instance._needs_update

    with pytest.raises(ValueError):
        # we only support cluster_compute, cluster_env, autosuspend
        connect_instance._parse_address("my_cluster?random=5")


def test_cloud_from_env(mock_auth_api_client) -> None:
    unconfigured_builder = ClientBuilder(
        anyscale_sdk=Mock(),
        auth_api_client=Mock(api_client=Mock(), anyscale_api_client=Mock()),
    )
    configured_builder = ClientBuilder(
        anyscale_sdk=Mock(),
        auth_api_client=Mock(api_client=Mock(), anyscale_api_client=Mock()),
    )
    configured_builder.cloud("explicit_cloud")

    with patch.dict(os.environ, {"ANYSCALE_CLOUD": "env_cloud"}):
        unconfigured_builder._fill_unset_configs_from_env()
        assert unconfigured_builder._cloud_name == "env_cloud"
        configured_builder._fill_unset_configs_from_env()
        assert configured_builder._cloud_name == "explicit_cloud"


def test_autosuspend_init_args(mock_auth_api_client) -> None:
    builder = ClientBuilder(
        anyscale_sdk=Mock(),
        auth_api_client=Mock(api_client=Mock(), anyscale_api_client=Mock()),
    )
    builder._init_args()
    assert builder._autosuspend_timeout is None
    builder._init_args(autosuspend="20")
    assert builder._autosuspend_timeout == 20
    builder._init_args(autosuspend=20)
    assert builder._autosuspend_timeout == 20  # 20 minutes
    builder._init_args(autosuspend="20m")
    assert builder._autosuspend_timeout == 20
    builder._init_args(autosuspend="3h")
    assert builder._autosuspend_timeout == 180  # 3 hours
    builder._init_args(autosuspend="-1")
    assert builder._autosuspend_timeout == -1  # disabled
    builder._init_args(autosuspend=-1)
    assert builder._autosuspend_timeout == -1  # disabled


def test_autosuspend_from_env(mock_auth_api_client) -> None:
    unconfigured_builder = ClientBuilder(
        anyscale_sdk=Mock(),
        auth_api_client=Mock(api_client=Mock(), anyscale_api_client=Mock()),
    )
    unconfigured_builder._fill_unset_configs_from_env()
    assert unconfigured_builder._autosuspend_timeout == 120  # default

    unconfigured_builder = ClientBuilder(
        anyscale_sdk=Mock(),
        auth_api_client=Mock(api_client=Mock(), anyscale_api_client=Mock()),
    )
    configured_builder = ClientBuilder(
        anyscale_sdk=Mock(),
        auth_api_client=Mock(api_client=Mock(), anyscale_api_client=Mock()),
    )
    configured_builder._parse_autosuspend(-1)

    with patch.dict(os.environ, {"ANYSCALE_AUTOSUSPEND": "20"}):
        unconfigured_builder._fill_unset_configs_from_env()
        assert unconfigured_builder._autosuspend_timeout == 20
        configured_builder._fill_unset_configs_from_env()
        assert configured_builder._autosuspend_timeout == -1

    unconfigured_builder = ClientBuilder(
        anyscale_sdk=Mock(),
        auth_api_client=Mock(api_client=Mock(), anyscale_api_client=Mock()),
    )
    with patch.dict(os.environ, {"ANYSCALE_AUTOSUSPEND": "10h"}):
        unconfigured_builder._fill_unset_configs_from_env()
        assert unconfigured_builder._autosuspend_timeout == 600  # 600 mins

    unconfigured_builder = ClientBuilder(
        anyscale_sdk=Mock(),
        auth_api_client=Mock(api_client=Mock(), anyscale_api_client=Mock()),
    )
    with patch.dict(os.environ, {"ANYSCALE_AUTOSUSPEND": "10m"}):
        unconfigured_builder._fill_unset_configs_from_env()
        assert unconfigured_builder._autosuspend_timeout == 10  # 10 mins

    unconfigured_builder = ClientBuilder(
        anyscale_sdk=Mock(),
        auth_api_client=Mock(api_client=Mock(), anyscale_api_client=Mock()),
    )
    with patch.dict(os.environ, {"ANYSCALE_AUTOSUSPEND": "-1"}):
        unconfigured_builder._fill_unset_configs_from_env()
        assert unconfigured_builder._autosuspend_timeout == -1  # disabled


def test_cluster_compute_from_env(mock_auth_api_client) -> None:
    unconfigured_builder = ClientBuilder(
        anyscale_sdk=Mock(),
        auth_api_client=Mock(api_client=Mock(), anyscale_api_client=Mock()),
    )
    configured_builder = ClientBuilder(
        anyscale_sdk=Mock(),
        auth_api_client=Mock(api_client=Mock(), anyscale_api_client=Mock()),
    )
    configured_builder.cluster_compute("explicit_compute")

    # cluster compute can be explicitly configured with either dict or string
    configured_builder_2 = ClientBuilder(
        anyscale_sdk=Mock(),
        auth_api_client=Mock(api_client=Mock(), anyscale_api_client=Mock()),
    )
    configured_builder_2.cluster_compute({"cloud_id": "123"})

    with patch.dict(os.environ, {"ANYSCALE_CLUSTER_COMPUTE": "env_compute"}):
        unconfigured_builder._fill_unset_configs_from_env()
        assert unconfigured_builder._cluster_compute_name == "env_compute"
        assert unconfigured_builder._cluster_compute_dict is None
        configured_builder._fill_unset_configs_from_env()
        assert configured_builder._cluster_compute_name == "explicit_compute"
        assert configured_builder._cluster_compute_dict is None
        configured_builder_2._fill_unset_configs_from_env()
        assert configured_builder_2._cluster_compute_name is None
        assert configured_builder_2._cluster_compute_dict == {"cloud_id": "123"}


def test_cluster_env_from_env(mock_auth_api_client) -> None:
    unconfigured_builder = ClientBuilder(
        anyscale_sdk=Mock(),
        auth_api_client=Mock(api_client=Mock(), anyscale_api_client=Mock()),
    )
    configured_builder = ClientBuilder(
        anyscale_sdk=Mock(),
        auth_api_client=Mock(api_client=Mock(), anyscale_api_client=Mock()),
    )
    configured_builder.cluster_env("explicit_env")

    # cluster env can be explicitly configured with either dict or string
    configured_builder_2 = ClientBuilder(
        anyscale_sdk=Mock(),
        auth_api_client=Mock(api_client=Mock(), anyscale_api_client=Mock()),
    )
    configured_builder_2.cluster_env({"base_image": "some/image"})

    with patch.dict(os.environ, {"ANYSCALE_CLUSTER_ENV": "env_cluster_env"}):
        unconfigured_builder._fill_unset_configs_from_env()
        assert unconfigured_builder._cluster_env_name == "env_cluster_env"
        assert unconfigured_builder._cluster_env_dict is None
        configured_builder._fill_unset_configs_from_env()
        assert configured_builder._cluster_env_name == "explicit_env"
        assert configured_builder._cluster_env_dict is None
        configured_builder_2._fill_unset_configs_from_env()
        assert configured_builder_2._cluster_env_name is None
        assert configured_builder_2._cluster_env_dict == {"base_image": "some/image"}


def test_job_name_from_env(mock_auth_api_client) -> None:
    unconfigured_builder = ClientBuilder(
        anyscale_sdk=Mock(),
        auth_api_client=Mock(api_client=Mock(), anyscale_api_client=Mock()),
    )
    configured_builder = ClientBuilder(
        anyscale_sdk=Mock(),
        auth_api_client=Mock(api_client=Mock(), anyscale_api_client=Mock()),
    )
    configured_builder.job_name("explicit_job_name")

    with patch.dict(os.environ, {"ANYSCALE_JOB_NAME": "env_job_name"}):
        unconfigured_builder._fill_unset_configs_from_env()
        assert unconfigured_builder._job_config.metadata["job_name"] == "env_job_name"
        configured_builder._fill_unset_configs_from_env()
        assert (
            configured_builder._job_config.metadata["job_name"] == "explicit_job_name"
        )


def test_namespace_from_env(mock_auth_api_client) -> None:
    unconfigured_builder = ClientBuilder(
        anyscale_sdk=Mock(),
        auth_api_client=Mock(api_client=Mock(), anyscale_api_client=Mock()),
    )
    configured_builder = ClientBuilder(
        anyscale_sdk=Mock(),
        auth_api_client=Mock(api_client=Mock(), anyscale_api_client=Mock()),
    )
    configured_builder.namespace("explicit_namespace")

    with patch.dict(os.environ, {"ANYSCALE_NAMESPACE": "env_namespace"}):
        unconfigured_builder._fill_unset_configs_from_env()
        assert unconfigured_builder._job_config.ray_namespace == "env_namespace"
        configured_builder._fill_unset_configs_from_env()
        assert configured_builder._job_config.ray_namespace == "explicit_namespace"


def test_multiple_env_configs(mock_auth_api_client) -> None:
    unconfigured_builder = ClientBuilder(
        anyscale_sdk=Mock(),
        auth_api_client=Mock(api_client=Mock(), anyscale_api_client=Mock()),
    )
    partially_configured_builder = ClientBuilder(
        anyscale_sdk=Mock(),
        auth_api_client=Mock(api_client=Mock(), anyscale_api_client=Mock()),
    )
    partially_configured_builder.namespace("explicit_namespace")
    with patch.dict(
        os.environ,
        {"ANYSCALE_NAMESPACE": "env_namespace", "ANYSCALE_CLOUD": "env_cloud"},
    ):
        unconfigured_builder._fill_unset_configs_from_env()
        assert unconfigured_builder._job_config.ray_namespace == "env_namespace"
        assert unconfigured_builder._cloud_name == "env_cloud"
        partially_configured_builder._fill_unset_configs_from_env()
        assert (
            partially_configured_builder._job_config.ray_namespace
            == "explicit_namespace"
        )
        assert partially_configured_builder._cloud_name == "env_cloud"


def test_new_proj_connect_params(tmp_path: Path, project_test_data: Project) -> None:
    project_dir = (tmp_path / "my_proj").absolute().as_posix()
    builder, sdk, _, ray = _make_test_builder(tmp_path)
    sdk.create_project.return_value = ProjectResponse(result=project_test_data)

    # Should create a new .anyscale.yaml file
    builder.project_dir(project_dir).connect()

    assert anyscale.project.get_project_id(project_dir)
    builder._start_session.assert_called_once_with(
        project_id=project_test_data.id,
        cluster_name="cluster-1",
        build_id="build_id",
        compute_template_id="mock_compute_template_id",
    )

    # Also check connection params in this test.
    ray.util.connect.assert_called_with(
        "session-1.userdata.com",
        metadata=[("cookie", "anyscale-token=value"), ("port", "10001")],
        secure=True,
        connection_retries=10,
        ignore_version=True,
        job_config=ray.job_config.JobConfig(),
    )


def test_detect_existing_proj(tmp_path: Path) -> None:
    nested_dir = (tmp_path / "my_proj" / "nested").absolute().as_posix()
    parent_dir = os.path.dirname(nested_dir)
    os.makedirs(nested_dir)
    builder, _, _, _ = _make_test_builder(tmp_path, [], setup_project_dir=False)

    # Setup project in parent dir
    project_yaml = os.path.join(parent_dir, ".anyscale.yaml")
    with open(project_yaml, "w+") as f:
        f.write(yaml.dump({"project_id": 12345}))

    # Should detect the parent project dir
    cwd = os.getcwd()
    try:
        os.chdir(nested_dir)
        builder.session("cluster-0").connect()
    finally:
        os.chdir(cwd)

    builder._start_session.assert_called_once_with(
        project_id=ANY,
        cluster_name="cluster-0",
        build_id="build_id",
        compute_template_id="mock_compute_template_id",
    )


def test_fallback_default_project(tmp_path: Path, project_test_data: Project) -> None:
    builder, sdk, _, _ = _make_test_builder(tmp_path, setup_project_dir=False)
    sdk.create_project.return_value = ProjectResponse(result=project_test_data)

    mock_default_project = project_test_data
    mock_default_project.is_default = True
    sdk.get_default_project = Mock(
        return_value=ProjectResponse(result=mock_default_project)
    )

    # Should use the default project
    mock_find_project_root = Mock(return_value=None)
    with patch.multiple("anyscale.project", find_project_root=mock_find_project_root):
        builder.connect()

    builder._start_session.assert_called_once_with(
        project_id=project_test_data.id,
        cluster_name="cluster-1",
        build_id="build_id",
        compute_template_id="mock_compute_template_id",
    )


def test_background_run_mode(tmp_path: Path, project_test_data: Project) -> None:
    scratch_dir = (tmp_path / "scratch").absolute().as_posix()
    builder, sdk, _, _ = _make_test_builder(tmp_path)
    builder._session_controller.push = Mock()
    builder._exec_controller.anyscale_exec = Mock()
    sdk.create_project.return_value = ProjectResponse(result=project_test_data)

    # Should create a new .anyscale.yaml file in the scratch dir
    builder.run_mode("background").connect()

    assert anyscale.project.get_project_id(scratch_dir)
    builder._session_controller.push.assert_called_with(
        "cluster-1", all_nodes=False, config=None, source=ANY, target=ANY
    )
    builder._exec_controller.anyscale_exec.assert_called_with(
        "cluster-1",
        commands=ANY,
        port_forward=(),
        screen=False,
        stop=False,
        sync=False,
        terminate=False,
        tmux=False,
    )
    builder._os._exit.assert_called_once_with(0)


def test_local_docker_run_mode(tmp_path: Path, project_test_data: Project) -> None:
    scratch_dir = (tmp_path / "scratch").absolute().as_posix()
    builder, sdk, subprocess, _ = _make_test_builder(tmp_path)
    sdk.create_project.return_value = ProjectResponse(result=project_test_data)

    # Should create a new .anyscale.yaml file in the scratch dir
    builder.run_mode("local_docker").connect()

    assert anyscale.project.get_project_id(scratch_dir)
    subprocess.check_call.assert_called_with(
        [
            "docker",
            "run",
            "--env",
            ANY,
            "--env",
            ANY,
            "-v",
            ANY,
            "--entrypoint=/bin/bash",
            ANY,
            "-c",
            ANY,
        ]
    )
    builder._os._exit.assert_called_once_with(0)


def test_connect_with_cloud(tmp_path: Path, project_test_data: Project) -> None:
    builder, sdk, _, _ = _make_test_builder(tmp_path, [])
    sdk.create_project.return_value = ProjectResponse(result=project_test_data)

    # Should create a new .anyscale.yaml file in the scratch dir
    builder.session("cluster-0").cloud("test_cloud").connect()

    assert builder._cloud_name == "test_cloud"
    builder._start_session.assert_called_once_with(
        project_id=project_test_data.id,
        cluster_name="cluster-0",
        build_id="build_id",
        compute_template_id="mock_compute_template_id",
    )


def test_connect_with_cluster_env_dict(
    tmp_path: Path, project_test_data: Project
) -> None:
    builder, sdk, _, _ = _make_test_builder(tmp_path, [])
    sdk.create_project.return_value = ProjectResponse(result=project_test_data)
    sdk.create_app_config.return_value = None

    cluster_env_dict = {
        "name": "my_cluster_env",
        "base_image": "anyscale/ray:1.4.0-py37",
    }
    builder.cluster_env(cluster_env_dict).connect()

    assert builder._cluster_env_dict == {"base_image": "anyscale/ray:1.4.0-py37"}
    assert builder._cluster_env_name == "my_cluster_env"

    builder._anyscale_sdk.create_app_config.assert_called_once_with(
        {
            "name": "my_cluster_env",
            "project_id": project_test_data.id,
            "config_json": {"base_image": "anyscale/ray:1.4.0-py37"},
        }
    )


def test_new_session(tmp_path: Path, project_test_data: Project) -> None:
    builder, sdk, _, _ = _make_test_builder(tmp_path, session_states=[])
    sdk.create_project.return_value = ProjectResponse(result=project_test_data)

    # Should create a new session.
    builder.session("cluster-0").connect()

    builder._start_session.assert_called_once_with(
        project_id=ANY,
        cluster_name="cluster-0",
        build_id="build_id",
        compute_template_id="mock_compute_template_id",
    )


def test_compare_cluster_compute(tmp_path: Path, project_test_data: Project) -> None:
    """
    Testing `_compare_cluster_compute` method when:
    1. Provided cluster compute is same as in cluster
    2. Provided cluster compute is different than cluster
    3. Comparing cluster compute to cluster that doesn't exist (when creating new cluster)
    """
    builder, _, _, _ = _make_test_builder(tmp_path, session_states=[])

    def mock_get_compute_template(cluster_compute_id: str):
        if cluster_compute_id == "cluster_compute_1_id":
            return Mock(result=Mock(config=cluster_compute_1))
        elif cluster_compute_id == "cluster_compute_2_id":
            return Mock(result=Mock(config=cluster_compute_2))

    # Compare two cluster computes with same values
    cluster_compute_1 = _make_compute_template_config()
    cluster_compute_2 = _make_compute_template_config()
    builder._anyscale_sdk.get_compute_template = Mock(
        side_effect=mock_get_compute_template
    )
    assert builder._is_equal_cluster_compute(
        "cluster_compute_1_id", "cluster_compute_2_id"
    )

    # Compare two cluster computes with different values
    cluster_compute_1 = _make_compute_template_config()
    cluster_compute_2 = _make_compute_template_config()
    cluster_compute_2.cloud_id = "fake-cloud-id-2"
    assert not builder._is_equal_cluster_compute(
        "cluster_compute_1_id", "cluster_compute_2_id"
    )


def test_reconnect_without_cluster_env(
    tmp_path: Path, project_test_data: Project
) -> None:
    """
    Tests the following situations to check the default cluster env logic:
    1. connect without any cluster env uses the default cluster env.
    2. Reconnect to existing terminated cluster without providing cluster env should use
       the cluster env of the previously terminated cluster , not the default one.
    3. Reconnect to existing terminated cluster and provide cluster env should use the
       provided cluster env.
    4. Connecting to an existing session never calls start.
    """
    builder, sdk, _, _ = _make_test_builder(tmp_path, session_states=[])
    sdk.create_project.return_value = ProjectResponse(result=project_test_data)

    # Create new session without providing cluster env. The default cluster env should be used
    # to start the cluster.
    builder.connect()
    py_version = "".join(str(x) for x in sys.version_info[0:2])
    ray_version = builder._ray.__version__
    builder._api_client.get_default_cluster_env_build_api_v2_builds_default_py_version_ray_version_get.assert_called_once_with(
        f"py{py_version}", ray_version
    )
    builder._start_session.assert_called_once_with(
        project_id=ANY,
        cluster_name="cluster-0",
        build_id="build_id",
        compute_template_id="mock_compute_template_id",
    )

    # Terminate the cluster. Reconnect to same cluster without providing cluster env.
    # The cluster's cluster env should be the one of the terminated cluster
    builder, sdk, _, _ = _make_test_builder(
        tmp_path, session_states=[], create_build=False,
    )
    session = _make_session(0, "Terminated")
    session.name = "cluster-0"
    session.build_id = "new_build_id_of_terminated"
    sdk.search_sessions = Mock(return_value=SessionListResponse(results=[session]))
    mock_build = _make_build()
    sdk.get_build = Mock(return_value=Mock(result=mock_build))
    builder._get_cluster_env_build = Mock(return_value=mock_build)  # type: ignore
    builder.session("cluster-0").connect()
    sdk.get_build.assert_called_once_with("new_build_id_of_terminated")
    builder._start_session.assert_called_once_with(
        project_id=ANY,
        cluster_name="cluster-0",
        build_id="new_build_id_of_terminated",
        compute_template_id="mock_compute_template_id",
    )

    # Terminate the cluster. Reconnect to same cluster and provide a new cluster env.
    # The cluster's cluster env should be the new one (not the one of the old terminated cluster).
    builder, sdk, _, _ = _make_test_builder(
        tmp_path, session_states=[], create_build=False,
    )
    session = _make_session(0, "Terminated")
    session.name = "cluster-0"
    session.build_id = "old_cluster_build_id"
    sdk.search_sessions = Mock(return_value=SessionListResponse(results=[session]))
    mock_build = _make_build()
    mock_build.id = "newest_build_id"
    sdk.get_build = Mock(return_value=Mock(result=mock_build))
    builder._get_cluster_env_build = Mock(return_value=mock_build)  # type: ignore
    builder.session("cluster-0").cluster_env("newest_cluster_env_name").connect()
    builder._get_cluster_env_build.assert_called_once_with(
        "project_id", "newest_cluster_env_name", None
    )
    builder._start_session.assert_called_once_with(
        project_id=ANY,
        cluster_name="cluster-0",
        build_id="newest_build_id",
        compute_template_id="mock_compute_template_id",
    )

    # Reconnect to the same running cluster and provide a new cluster env.
    # The cluster should be untouched and a warning should be raised.
    builder, sdk, _, _ = _make_test_builder(
        tmp_path, session_states=[], create_build=False,
    )
    builder._log.warning = Mock()
    session = _make_session(0, "Running")
    session.name = "cluster-0"
    session.build_id = "old_cluster_build_id"
    sdk.search_sessions = Mock(return_value=SessionListResponse(results=[session]))
    mock_build = _make_build()
    sdk.get_build = Mock(return_value=Mock(result=mock_build))
    builder._get_cluster_env_build = Mock(return_value=mock_build)  # type: ignore
    builder.session("cluster-0").cluster_env("random_name").connect()
    builder._log.warning.assert_called_once()
    builder._start_session.assert_not_called()


def test_base_docker_image(tmp_path: Path, project_test_data: Project,) -> None:
    scratch_dir = (tmp_path / "scratch").absolute().as_posix()
    builder, _, _, _ = _make_test_builder(tmp_path, session_states=["Running"])

    # Base docker images are no longer supported
    with pytest.raises(ValueError):
        builder.project_dir(scratch_dir).base_docker_image(
            "anyscale/ray-ml:custom"
        ).connect()


def test_requirements_list(tmp_path: Path, project_test_data: Project) -> None:
    builder, _, _, _ = _make_test_builder(tmp_path, session_states=[])

    # anyscale.require().connect() no longer supported
    with pytest.raises(ValueError):
        builder.require(["pandas", "wikipedia"]).connect()


def test_new_session_lost_lock(tmp_path: Path, project_test_data: Project) -> None:
    builder, sdk, _, ray = _make_test_builder(tmp_path, session_states=[])
    sdk.create_project.return_value = ProjectResponse(result=project_test_data)

    # Emulate session lock failure.
    ray.util.connect.side_effect = _connected(ray, {"num_clients": 999999})

    # Should create a new session.
    with pytest.raises(RuntimeError):
        builder.connect()

    builder._start_session.assert_called_once_with(
        project_id=project_test_data.id,
        cluster_name="cluster-0",
        build_id="build_id",
        compute_template_id="mock_compute_template_id",
    )


def test_update_idle_timeout_no_restart(
    tmp_path: Path, project_test_data, mock_auth_api_client
):
    (tmp_path / "scratch").absolute().as_posix()
    api_client = Mock()

    sess = _make_session(0, "Running")
    sess.idle_timeout = 120
    sess_resp = Mock()
    sess_resp.results = [sess]
    sess_resp.metadata.next_paging_token = None
    api_client.list_sessions_api_v2_sessions_get = Mock(return_value=sess_resp)

    builder = ClientBuilder(
        anyscale_sdk=Mock(),
        auth_api_client=Mock(api_client=api_client, anyscale_api_client=Mock()),
    )
    builder._get_organization_default_cloud = Mock()  # type: ignore
    builder._wait_for_app_build = Mock()  # type: ignore
    builder._anyscale_sdk.search_sessions = Mock(
        return_value=SessionListResponse(results=[sess])
    )

    builder._create_or_update_session_data(
        "cluster-0",
        "mock_project_id",
        "mock_build_id",
        "mock_compute_template_id",
        idle_timeout=-1,
    )
    builder._anyscale_sdk.update_cluster.assert_called_once_with(
        sess.id, UpdateCluster(idle_timeout_minutes=-1)
    )
    builder._anyscale_sdk.start_cluster.assert_not_called()


def test_update_allow_public_internet_traffic_restart(
    tmp_path: Path, project_test_data, mock_auth_api_client
):
    (tmp_path / "scratch").absolute().as_posix()
    api_client = Mock()

    sess = _make_session(0, "Running")
    sess.allow_public_internet_traffic = False
    sess_resp = Mock()
    sess_resp.results = [sess]
    sess_resp.metadata.next_paging_token = None
    api_client.list_sessions_api_v2_sessions_get = Mock(return_value=sess_resp)

    builder = ClientBuilder(
        anyscale_sdk=Mock(),
        auth_api_client=Mock(api_client=api_client, anyscale_api_client=Mock()),
    )
    builder._get_cluster_or_die = Mock(return_value=sess)  # type: ignore
    builder._get_organization_default_cloud = Mock()  # type: ignore
    builder._wait_for_app_build = Mock()  # type: ignore
    builder._allow_public_internet_traffic = True
    builder._log_cluster_configs = Mock()  # type: ignore

    builder._start_session(
        "mock_project_id", "cluster-0", "mock_build_id", "mock_compute_template_id",
    )
    builder._anyscale_sdk.start_cluster.assert_called_with(
        "session_id",
        StartClusterOptions(
            allow_public_internet_traffic=True,
            cluster_compute_id="mock_compute_template_id",
            cluster_environment_build_id="mock_build_id",
        ),
    )


def test_log_cluster_configs(tmp_path: Path, project_test_data, mock_auth_api_client):
    (tmp_path / "scratch").absolute().as_posix()
    api_client = Mock()
    sess = _make_session(0, "Running")
    sess_resp = Mock()
    sess_resp.results = [sess]
    sess_resp.metadata.next_paging_token = None
    api_client.list_sessions_api_v2_sessions_get = Mock(return_value=sess_resp)
    builder = ClientBuilder(
        anyscale_sdk=Mock(),
        auth_api_client=Mock(api_client=api_client, anyscale_api_client=Mock()),
    )
    session = Mock()
    session.id = "mock_id"
    builder._create_or_update_session_data = Mock(return_value=(session, True))  # type: ignore
    builder._log_cluster_configs = Mock()  # type: ignore
    # Should create a new session.
    builder._start_session(
        "mock_project_id", "cluster-0", "mock_build_id", "mock_compute_template_id",
    )
    builder._log_cluster_configs.assert_called_with(
        cluster_name="cluster-0",
        build_id="mock_build_id",
        compute_template_id="mock_compute_template_id",
        url="https://console.anyscale.com/projects/mock_project_id/clusters/mock_id",
    )


def test_disable_cloud_change(tmp_path: Path, project_test_data: Project) -> None:
    builder, sdk, _, ray = _make_test_builder(
        tmp_path=tmp_path, cloud_id="test_cloud_1"
    )
    sdk.create_project.return_value = ProjectResponse(result=project_test_data)
    ray.util.disconnect()
    with pytest.raises(Exception):
        builder.session("cluster-0", update=True).cloud("test_cloud_2").connect()


def test_reuse_cluster_env_and_compute_match(
    tmp_path: Path, project_test_data: Project
) -> None:
    """ Checks that when the cluster is active, we never update it.
    TODO(ameer/IanR/Nikita): make cluster compute/env mismatch raise an error when Update=False.
    """
    (tmp_path / "scratch").absolute().as_posix()
    builder, sdk, _, ray = _make_test_builder(tmp_path)
    sdk.create_project.return_value = ProjectResponse(result=project_test_data)

    # Create session to emulate build id match
    sess = _make_session(0, "Running")
    sess.build_id = "build_id"
    sess_resp = Mock()
    sess_resp.results = [sess]
    sess_resp.metadata.next_paging_token = None
    sdk.list_sessions.return_value = sess_resp

    # Build id doesn't match, does not update.
    # We do not update active clusters unless the user explicitly requests it.
    builder.session("cluster-0").connect()
    builder._start_session.assert_not_called()
    ray.util.disconnect()

    # Build id match, updated because the user explicitly asked for update.
    builder.session("cluster-0", update=True).connect()
    builder._start_session.assert_called_once_with(
        project_id=project_test_data.id,
        cluster_name="cluster-0",
        build_id="build_id",
        compute_template_id="mock_compute_template_id",
    )


def test_reuse_session_hash_mismatch(
    tmp_path: Path, project_test_data: Project
) -> None:
    """
    Checks that when the build id and compute template id don't match, a running session is
    updated with connect.
    """
    builder, sdk, _, _ = _make_test_builder(tmp_path)
    sdk.create_project.return_value = ProjectResponse(result=project_test_data)

    # Emulate build id mismatch.
    sess = _make_session(0, "Running")
    sess.build_id = "wrong-build-id"
    sess_resp = Mock()
    sess_resp.results = [sess]
    sess_resp.metadata.next_paging_token = None
    sdk.list_sessions.return_value = sess_resp

    # Should connect and run 'start'.
    builder.session("cluster-0", update=True).connect()

    builder._start_session.assert_called_once_with(
        project_id=project_test_data.id,
        cluster_name="cluster-0",
        build_id="build_id",
        compute_template_id="mock_compute_template_id",
    )


def test_reuse_session_lock_failure(tmp_path: Path, project_test_data: Project) -> None:
    builder, sdk, _, ray = _make_test_builder(tmp_path, session_states=["Running"])
    sdk.create_project.return_value = ProjectResponse(result=project_test_data)

    def create_session(*a: Any, **kw: Any) -> None:
        sess_resp = Mock()
        sess_resp.results = [
            _make_session(0, "Running"),
            _make_session(1, "Running"),
        ]
        sess_resp.metadata.next_paging_token = None
        sdk.search_sessions.return_value = sess_resp
        ray.util.connect.side_effect = _connected(ray, {})

    builder._start_session.side_effect = create_session

    # Emulate session hash code match but lock failure.
    sess0 = _make_session(0, "Running")
    sess0.build_id = "build_id"
    sess1 = _make_session(0, "Running")
    sess1.build_id = "build_id"
    sess_resp = Mock()
    sess_resp.results = [sess0, sess1]
    sess_resp.metadata.next_paging_token = None
    sdk.search_sessions.return_value = sess_resp

    # Creates new session-1.
    builder.connect()

    builder._start_session.assert_called_once_with(
        project_id=project_test_data.id,
        cluster_name="cluster-1",
        build_id="build_id",
        compute_template_id="mock_compute_template_id",
    )


def test_restart_session_conn_failure(
    tmp_path: Path, project_test_data: Project
) -> None:
    builder, sdk, _, ray = _make_test_builder(tmp_path, session_states=["Running"])
    sdk.create_project.return_value = ProjectResponse(result=project_test_data)

    def fail_first_session(url: str, *a: Any, **kw: Any) -> Any:
        raise ConnectionError("mock connect failure")

    # Emulate session hash code match but conn failure.
    ray.util.connect.side_effect = fail_first_session

    # Tries to restart it, but fails.
    with pytest.raises(ConnectionError):
        builder.connect()

    builder._start_session.assert_called_once_with(
        project_id=project_test_data.id,
        cluster_name="cluster-1",
        build_id="build_id",
        compute_template_id="mock_compute_template_id",
    )


def test_fixed_session(tmp_path: Path, project_test_data: Project) -> None:
    builder, sdk, _, _ = _make_test_builder(
        tmp_path, session_states=["Running", "Running"], create_build=False
    )
    sdk.create_project.return_value = ProjectResponse(result=project_test_data)
    mock_app_config = _make_app_template()
    mock_build = _make_build()
    mock_build.id = "mock_build_id"
    cluster_env_identifier = f"{mock_app_config.name}:{mock_build.revision}"
    builder._get_cluster_env_build = Mock(return_value=mock_build)  # type: ignore

    # Should connect and run 'up'.
    builder.session("cluster-1", update=True).cluster_env(
        cluster_env_identifier
    ).connect()

    builder._start_session.assert_called_once_with(
        project_id=project_test_data.id,
        cluster_name="cluster-1",
        build_id="mock_build_id",
        compute_template_id="mock_compute_template_id",
    )


def test_fixed_session_not_running(tmp_path: Path, project_test_data: Project,) -> None:
    builder, sdk, _, _ = _make_test_builder(
        tmp_path, session_states=["Running", "Stopped"]
    )
    sdk.create_project.return_value = ProjectResponse(result=project_test_data)

    # Should connect and run 'up'.
    builder.session("cluster-1").connect()

    builder._start_session.assert_called_once_with(
        project_id=project_test_data.id,
        cluster_name="cluster-1",
        build_id="build_id",
        compute_template_id="mock_compute_template_id",
    )


def test_fixed_session_static_ray_version_mismatch(
    tmp_path: Path, project_test_data: Project,
) -> None:
    builder, sdk, _, ray = _make_test_builder(
        tmp_path, session_states=["Running", "Stopped"]
    )
    sdk.create_project.return_value = ProjectResponse(result=project_test_data)
    ray.__commit__ = "fake_commit"

    # Should connect and not run 'up'.
    with pytest.raises(ValueError):
        builder.session("cluster-0").connect()

    builder._start_session.assert_not_called()


@pytest.mark.parametrize("enable_multiple_clients", [True, False])
def test_multiple_clients(
    enable_multiple_clients: bool, tmp_path: Path, project_test_data: Project,
) -> None:
    try:
        os.environ["ANYSCALE_ALLOW_MULTIPLE_CLIENTS"] = (
            "1" if enable_multiple_clients else "0"
        )
        builder, sdk, _, ray = _make_test_builder(
            tmp_path, session_states=["Running", "Running"]
        )

        sdk.create_project.return_value = ProjectResponse(result=project_test_data)
        ray.util.connect.side_effect = _connected(ray, {"num_clients": 2})

        if enable_multiple_clients:
            builder.session("cluster-1", update=False).connect()
        else:
            with pytest.raises(RuntimeError):
                builder.session("cluster-1", update=False).connect()
        builder._start_session.assert_not_called()
        # Connect should be called an extra time to check versioning
        assert builder._ray.util.connect.call_count == 2
    finally:
        del os.environ["ANYSCALE_ALLOW_MULTIPLE_CLIENTS"]


@pytest.mark.parametrize("remote_version_mismatch", [True, False])
def test_fixed_session_no_update(
    remote_version_mismatch: bool, tmp_path: Path, project_test_data: Project,
) -> None:
    builder, sdk, _, ray = _make_test_builder(
        tmp_path, session_states=["Running", "Running"]
    )
    sdk.create_project.return_value = ProjectResponse(result=project_test_data)

    if remote_version_mismatch:
        ray.util.connect.side_effect = _connected(ray, {"ray_commit": "bad commit"},)

    # Should connect and run 'up'.
    if remote_version_mismatch:
        with pytest.raises(ValueError):
            builder.session("cluster-1", update=False).connect()
    else:
        builder.session("cluster-1", update=False).connect()

    builder._start_session.assert_not_called()
    if remote_version_mismatch:
        # Connect should only be called once -- fail on version mismatch
        builder._ray.util.connect.assert_called_once()
    else:
        # Connect should be called an extra time to check version info
        assert builder._ray.util.connect.call_count == 2


def test_connect_errors_triggers_version_check(
    tmp_path: Path, project_test_data: Project,
) -> None:
    builder, sdk, subprocess, ray = _make_test_builder(
        tmp_path, session_states=["Running", "Running"]
    )
    sdk.create_project.return_value = ProjectResponse(result=project_test_data)

    ray.util.connect.side_effect = ConnectionError("Failed to Connect")
    ret_val = b'{"ray_commit": "BAD_COMMIT", "ray_version": "0.1.0"}\r\n\x1b[0mChecking External environment settings\nFetched IP: session-<session_id>.i.anyscaleuserdata.com\n'
    subprocess.check_output = Mock(return_value=ret_val)
    cluster_name = "cluster-1"

    # This should raise a ValueError from the VersionMismatch (not the ConnectionError)
    with pytest.raises(ValueError):
        builder.session(cluster_name, update=False).connect()

    # subprocess.check_output.assert_called_once_with("")
    subprocess.check_output.assert_called_once_with(
        ["anyscale", "exec", "--session-name", cluster_name, "--", "python", "-c", ANY],
        stderr=ANY,
    )


def test_new_fixed_session(tmp_path: Path, project_test_data: Project) -> None:
    builder, sdk, _, _ = _make_test_builder(tmp_path, session_states=[])
    sdk.create_project.return_value = ProjectResponse(result=project_test_data)

    def create_session(*a: Any, **kw: Any) -> None:
        sess_resp = Mock()
        sess_resp.results = [_make_session(i, "Running") for i in range(3)]
        sess_resp.metadata.next_paging_token = None
        sdk.search_sessions.return_value = sess_resp

    builder._start_session.side_effect = create_session

    # Should create a new session.
    builder.session("cluster-2").connect()

    builder._start_session.assert_called_once_with(
        project_id=project_test_data.id,
        cluster_name="cluster-2",
        build_id="build_id",
        compute_template_id="mock_compute_template_id",
    )


class MockPopen(object):
    def __init__(self) -> None:
        self.returncode = 0

    def communicate(self) -> Tuple[str, str]:
        return (
            '[{"id": "cloud2", "name": "second cloud"}, {"id": "cloud1", "name": "first cloud"}]',
            "",
        )


def test_get_all_clouds(mock_auth_api_client) -> None:
    sdk = Mock()
    builder = ClientBuilder(
        anyscale_sdk=sdk,
        auth_api_client=Mock(api_client=Mock(), anyscale_api_client=Mock()),
    )

    mock_cloud_1 = Mock()
    mock_cloud_1.name = "cloud_1"
    mock_cloud_2 = Mock()
    mock_cloud_2.name = "cloud_2"

    sdk.search_clouds.side_effect = [
        CloudListResponse(
            results=[mock_cloud_1],
            metadata=ListResponseMetadata(
                total=2, next_paging_token="next_paging_token"
            ),
        ),
        CloudListResponse(
            results=[mock_cloud_2], metadata=ListResponseMetadata(total=2),
        ),
    ]

    all_clouds = builder._get_all_clouds()
    assert all_clouds == [mock_cloud_1, mock_cloud_2]
    sdk.search_clouds.assert_has_calls(
        [
            call({"paging": {"count": 50}}),
            call({"paging": {"count": 50, "paging_token": "next_paging_token"}}),
        ]
    )


@pytest.mark.parametrize("last_used_cloud_id", [None, "mock_cloud_id"])
def test_get_last_used_cloud(
    last_used_cloud_id: Optional[str], project_test_data: Project, mock_auth_api_client
) -> None:
    sdk = Mock()
    project_test_data.last_used_cloud_id = last_used_cloud_id
    sdk.get_project.return_value = ProjectResponse(result=project_test_data)
    builder = ClientBuilder(
        anyscale_sdk=sdk,
        auth_api_client=Mock(api_client=Mock(), anyscale_api_client=Mock()),
    )
    mock_cloud_1 = Mock()
    mock_cloud_1.name = "cloud_1"
    mock_cloud_2 = Mock()
    mock_cloud_2.name = "cloud_2"

    builder._get_all_clouds = Mock(return_value=[mock_cloud_1, mock_cloud_2])  # type: ignore
    sdk.get_cloud.return_value = CloudResponse(result=mock_cloud_1)

    if last_used_cloud_id:
        assert (
            builder._get_last_used_cloud("prj_1") == "cloud_1"
        ), "Should use Cloud from Project's last_used_cloud_id"
        sdk.get_cloud.assert_called_once_with(last_used_cloud_id)
        builder._get_all_clouds.assert_not_called()
    else:
        # Check that we get the "default cloud" (cloud first created)
        # if there is no last used cloud.
        assert (
            builder._get_last_used_cloud("prj_1") == "cloud_2"
        ), "Should use oldest Cloud if Project does not have last_used_cloud_id"
        sdk.get_cloud.assert_not_called()
        builder._get_all_clouds.assert_called_once()


@pytest.mark.parametrize("default_cloud_id", [None, "mock_cloud_id"])
def test_get_organization_default_cloud(
    default_cloud_id: Optional[str], mock_auth_api_client
) -> None:
    api_client = Mock()
    api_client.get_user_info_api_v2_userinfo_get.return_value.result = Mock(
        organizations=[Mock(default_cloud_id=default_cloud_id)]
    )
    api_client.get_cloud_api_v2_clouds_cloud_id_get.return_value.result.name = (
        "mock_cloud_name"
    )

    builder = ClientBuilder(
        anyscale_sdk=Mock(),
        auth_api_client=Mock(api_client=api_client, anyscale_api_client=Mock()),
    )

    if default_cloud_id:
        assert builder._get_organization_default_cloud() == "mock_cloud_name"
        api_client.get_cloud_api_v2_clouds_cloud_id_get.assert_called_once_with(
            cloud_id=default_cloud_id
        )
    else:
        assert builder._get_organization_default_cloud() is None
        api_client.get_cloud_api_v2_clouds_cloud_id_get.assert_not_called()

    api_client.get_user_info_api_v2_userinfo_get.assert_called_once()


@pytest.mark.parametrize("static_ray_version_mismatch", [True, False])
def test_cluster_env(
    static_ray_version_mismatch: bool, tmp_path: Path, project_test_data: Project,
) -> None:
    builder, sdk, _, ray = _make_test_builder(
        tmp_path, session_states=[], create_build=False
    )
    sdk.create_project.return_value = ProjectResponse(result=project_test_data)

    if static_ray_version_mismatch:
        ray.__commit__ = "abcdef"
        ray.util.connect.side_effect = _connected(ray, {"ray_commit": "abcdef"},)

    app_templates_resp = Mock()
    app_templates_resp.results = [_make_app_template()]
    app_templates_resp.metadata.next_paging_token = None
    sdk.list_app_configs.return_value = app_templates_resp

    build = _make_build()
    builds_resp = Mock()
    builds_resp.results = [build]
    builds_resp.metadata.next_paging_token = None
    sdk.list_builds.return_value = builds_resp

    get_build_resp = Mock()
    get_build_resp.result = build
    sdk.get_build.return_value = get_build_resp

    def create_session(*a: Any, **kw: Any) -> None:
        sess_resp = Mock()
        sess_resp.results = [_make_session(0, "Running")]
        sess_resp.metadata.next_paging_token = None
        sdk.search_sessions.return_value = sess_resp

    builder._start_session.side_effect = create_session

    with pytest.raises(RuntimeError):
        builder.cluster_env("non-existent-app-config").connect()
    with pytest.raises(TypeError):
        builder.cluster_env([])

    builder.cluster_env(
        {"name": "my_custom_image", "base_image": "anyscale/ray-ml:pinned-nightly"}
    )
    assert builder._cluster_env_name == "my_custom_image"
    assert builder._cluster_env_dict == {"base_image": "anyscale/ray-ml:pinned-nightly"}
    builder.cluster_env({"base_image": "anyscale/ray-ml:pinned-nightly"})
    assert builder._cluster_env_name is None
    assert builder._cluster_env_dict == {"base_image": "anyscale/ray-ml:pinned-nightly"}

    with pytest.raises(RuntimeError):
        # Must provide build identifier if using compute config path and starting
        # session from sdk (with runtime env)
        builder.connect()
    builder.cluster_env(
        {"name": "test-app-config", "base_image": "anyscale/ray-ml:pinned-nightly"}
    ).connect()

    builder._start_session.assert_called_once_with(
        project_id=project_test_data.id,
        cluster_name="cluster-0",
        build_id="build_id",
        compute_template_id="mock_compute_template_id",
    )


@pytest.mark.parametrize(
    "ray_version_tuple",
    [
        ["COMMIT_ID", "2.0.0.dev0", "master/COMMIT_ID/ray-2.0.0.dev0"],
        ["RELEASE_COMMIT_ID", "1.4.0", "releases/1.4.0/RELEASE_COMMIT_ID/ray-1.4.0"],
    ],
)
@pytest.mark.parametrize("py_version", ["36", "37", "38"])
def test_get_wheel_url(py_version, ray_version_tuple) -> None:
    commit_id, ray_version, expected_suffix = ray_version_tuple
    wheel_prefix = f"https://s3-us-west-2.amazonaws.com/ray-wheels/{expected_suffix}"

    expected_py_version = f"cp{py_version}-cp{py_version}m"

    if py_version == "38":
        expected_py_version = expected_py_version.rstrip("m")

    if py_version == "38":
        expected_macos_wheel = (
            f"{wheel_prefix}-{expected_py_version}-macosx_10_15_x86_64.whl"
        )
    else:
        expected_macos_wheel = (
            f"{wheel_prefix}-{expected_py_version}-macosx_10_15_intel.whl"
        )

    assert (
        get_wheel_url(commit_id, ray_version, py_version, "darwin")
        == expected_macos_wheel
    )

    assert (
        get_wheel_url(commit_id, ray_version, py_version, "linux")
        == f"{wheel_prefix}-{expected_py_version}-manylinux2014_x86_64.whl"
    )

    assert (
        get_wheel_url(commit_id, ray_version, py_version, "win32")
        == f"{wheel_prefix}-{expected_py_version}-win_amd64.whl"
    )


def test_commit_url_is_valid() -> None:
    for python_version in ["36", "37", "38"]:
        for pltfrm in ["win32", "linux", "darwin"]:
            url = get_wheel_url(RAY_COMMIT, RAY_VERSION, python_version, pltfrm)
            # We use HEAD, because it is faster than downloading with GET
            resp = requests.head(url)
            assert resp.status_code == 200, f"Cannot find wheel for: {url}"


def test_set_metadata_in_job_config(mock_auth_api_client) -> None:
    sdk = Mock()
    _api_client = Mock()
    _api_client.get_user_info_api_v2_userinfo_get = Mock(
        return_value=Mock(result=Mock(id="mock_creator_id"))
    )

    def mock_set_metadata(key: str, val: str) -> None:
        connect_instance._job_config.metadata[key] = val

    # Test no user specified job name, user specified creator_id
    connect_instance = ClientBuilder(
        anyscale_sdk=sdk,
        auth_api_client=Mock(api_client=_api_client, anyscale_api_client=Mock()),
    )
    connect_instance._job_config.metadata = {}
    connect_instance._job_config.set_metadata = mock_set_metadata
    with patch("sys.argv", new=["file_name"]):
        connect_instance._set_metadata_in_job_config("mock_creator_id")
    assert connect_instance._job_config.metadata["job_name"].startswith("file_name")
    assert connect_instance._job_config.metadata["creator_id"] == "mock_creator_id"

    # Test no user specified job name
    connect_instance = ClientBuilder(
        anyscale_sdk=sdk,
        auth_api_client=Mock(api_client=_api_client, anyscale_api_client=Mock()),
    )
    connect_instance._job_config.metadata = {}
    connect_instance._job_config.set_metadata = mock_set_metadata
    with patch("sys.argv", new=["file_name"]):
        connect_instance._set_metadata_in_job_config()
    assert connect_instance._job_config.metadata["job_name"].startswith("file_name")
    assert connect_instance._job_config.metadata["creator_id"] == "mock_creator_id"

    # Test user specified job name
    connect_instance = ClientBuilder(
        anyscale_sdk=sdk,
        auth_api_client=Mock(api_client=_api_client, anyscale_api_client=Mock()),
    )
    connect_instance._job_config.metadata = {}
    connect_instance._job_config.set_metadata = mock_set_metadata
    connect_instance.job_name("mock_job_name")._set_metadata_in_job_config()
    assert connect_instance._job_config.metadata["job_name"].startswith("mock_job_name")
    assert connect_instance._job_config.metadata["creator_id"] == "mock_creator_id"


def test_namespace(mock_auth_api_client) -> None:
    sdk = Mock()
    _api_client = Mock()

    # Test no user specified job name
    connect_instance = ClientBuilder(
        anyscale_sdk=sdk,
        auth_api_client=Mock(api_client=_api_client, anyscale_api_client=Mock()),
    )

    def mock_set_ray_namespace(namespace: str) -> None:
        connect_instance._job_config.ray_namespace = namespace

    connect_instance._job_config.set_ray_namespace = mock_set_ray_namespace
    connect_instance.namespace("mock_namespace")
    assert connect_instance._job_config.ray_namespace == "mock_namespace"


def test_set_runtime_env_in_job_config(
    tmp_path: Path, project_test_data: Project, mock_auth_api_client
) -> None:

    sdk = Mock()
    _api_client = Mock()
    connect_instance = ClientBuilder(
        anyscale_sdk=sdk,
        auth_api_client=Mock(api_client=_api_client, anyscale_api_client=Mock()),
    )
    connect_instance.env({"working_dir": "/tmp"})._set_runtime_env_in_job_config("/")
    assert connect_instance._job_config.runtime_env["working_dir"] == "/tmp"
    assert connect_instance._job_config.runtime_env["excludes"] == [
        ".git",
        "__pycache__",
        "venv",
        "/.anyscale.yaml",
        "/session-default.yaml",
    ]

    connect_instance = ClientBuilder(
        anyscale_sdk=sdk,
        auth_api_client=Mock(api_client=_api_client, anyscale_api_client=Mock()),
    )
    connect_instance.env({})._set_runtime_env_in_job_config("/tmp")
    assert connect_instance._job_config.runtime_env["working_dir"] == "/tmp"
    assert connect_instance._job_config.runtime_env["excludes"] == [
        ".git",
        "__pycache__",
        "venv",
        "/tmp/.anyscale.yaml",
        "/tmp/session-default.yaml",
    ]

    connect_instance = ClientBuilder(
        anyscale_sdk=sdk,
        auth_api_client=Mock(api_client=_api_client, anyscale_api_client=Mock()),
    )
    connect_instance.env(
        {"working_dir": "/tmp", "excludes": [".gitignore"], "pip": ["numpy"]}
    )._set_runtime_env_in_job_config("/")
    assert connect_instance._job_config.runtime_env["working_dir"] == "/tmp"
    assert connect_instance._job_config.runtime_env["excludes"] == [
        ".git",
        "__pycache__",
        "venv",
        ".gitignore",
        "/.anyscale.yaml",
        "/session-default.yaml",
    ]
    assert connect_instance._job_config.runtime_env["pip"] == ["numpy"]

    connect_instance, sdk, _, _ = _make_test_builder(tmp_path, [])
    sdk.create_project.return_value = ProjectResponse(result=project_test_data)

    connect_instance.env({"working_dir": "/tmp"}).project_dir("/tmp").connect()
    connect_instance._job_config.set_runtime_env.assert_called_once_with(  # type: ignore
        {
            "working_dir": "/tmp",
            "excludes": [
                ".git",
                "__pycache__",
                "venv",
                "/tmp/.anyscale.yaml",
                "/tmp/session-default.yaml",
            ],
            "env_vars": {"RAY_SERVE_ROOT_URL": "https://serve-session-0.userdata.com"},
        }
    )
    connect_instance._start_session.assert_called_once_with(  # type: ignore
        project_id=ANY,
        cluster_name="cluster-0",
        build_id="build_id",
        compute_template_id="mock_compute_template_id",
    )


@patch.dict(
    os.environ,
    {
        "ANYSCALE_SESSION_ID": "ses_fake-session-01234567890",
        "RAY_ADDRESS": "anyscale://fake-cluster",
    },
)
def test_runtime_env_set_when_run_on_anyscale_cluster(
    tmp_path: Path, project_test_data: Project
):
    """Test that the runtime env is set when a Ray client script is run on an Anyscale node.

    See https://github.com/anyscale/product/issues/6809.
    """
    connect_instance, sdk, _, _ = _make_test_builder(tmp_path, [])
    sdk.create_project.return_value = ProjectResponse(result=project_test_data)

    runtime_env_pip = ["seaborn"]
    connect_instance.env({"pip": runtime_env_pip}).connect()
    connect_instance._job_config.set_runtime_env.assert_called_once_with(  # type: ignore
        {"pip": runtime_env_pip}
    )


@pytest.mark.parametrize(
    "anyscale_call_frames",
    [
        [  # black: no
            "/path/anyscale/connect.py",
            "/path/anyscale/connect.py",
            "/path/anyscale/__init__.py",
        ],
        [  # black: no
            "/path/anyscale/connect.py",
            "/path/anyscale/connect.py",
            "/path/ray/client_builder.py",
            "/path/ray/client_builder.py",
        ],
    ],
)
@pytest.mark.parametrize("file_name", ["random_file.py", "anyscale_in_file_name.py"])
def test_is_in_shell(anyscale_call_frames, file_name) -> None:
    """
    Tests if Anyscale Connect Determines if we are in an interactive
    context for both invocations via anyscale.connect() & ray.init("anyscale://")
    """

    def frame_mock(name: str) -> Any:
        mock = Mock()
        mock.filename = name
        return mock

    ipython_shell = [
        "<ipython-input-2-f869cc61c5de>",
        "/home/ubuntu/anaconda3/envs/anyscale/bin/ipython",
    ]
    assert _is_in_shell(list(map(frame_mock, anyscale_call_frames + ipython_shell)))

    python_shell = ["<stdin>"]
    assert _is_in_shell(list(map(frame_mock, anyscale_call_frames + python_shell)))

    # Running file via `ipython random_file.py`
    ipython_from_file = [
        file_name,
        "/home/ubuntu/anaconda3/envs/anyscale/bin/ipython",
    ]
    assert not _is_in_shell(
        list(map(frame_mock, anyscale_call_frames + ipython_from_file))
    )

    # Running file via `python random_file.py`
    python_from_file = [file_name]
    assert not _is_in_shell(
        list(map(frame_mock, anyscale_call_frames + python_from_file))
    )


def test_connect_output(tmp_path: Path, project_test_data: Project) -> None:
    """Test that ray.init("anyscale://") returns a Ray ClientContext
    and has all proper fields set
    """

    builder, sdk, _, _ = _make_test_builder(
        tmp_path, session_states=["Running", "Running"]
    )
    sdk.create_project.return_value = ProjectResponse(result=project_test_data)

    context = builder.session("cluster-1").connect()

    expected_context = AnyscaleClientContext(
        anyscale_cluster_info=AnyscaleClientConnectResponse(cluster_id="cluster-1"),
        python_version=platform.python_version(),
        _num_clients=1,
        ray_version=RAY_VERSION,
        ray_commit=RAY_COMMIT,
        protocol_version="fake_version",
        dashboard_url="https://fake_dashboard.com",
    )

    assert context == expected_context, "Returned Context does not match!"


def test_multiclient_context() -> None:
    """Test that the correct arguments are passed to Ray ClientContext
    on versions where multiclient is supported.
    """

    # Can't patch __init__ indirectly since it's a magic method, track that
    # methods are called with variables
    multiclient_init_called = False
    no_multiclient_init_called = False

    # Simulates ClientContext.__init__ after changes from
    # https://github.com/ray-project/ray/pull/17942
    def multiclient_init(
        self,
        dashboard_url,
        python_version,
        ray_version,
        ray_commit,
        protocol_version,
        _num_clients,
        _context_to_restore,
    ):
        nonlocal multiclient_init_called
        multiclient_init_called = True

    with patch("ray.client_builder.ClientContext.__init__", multiclient_init):
        AnyscaleClientContext(
            anyscale_cluster_info=AnyscaleClientConnectResponse(cluster_id="cluster-1"),
            python_version=platform.python_version(),
            _num_clients=1,
            ray_version=RAY_VERSION,
            ray_commit=RAY_COMMIT,
            protocol_version="fake_version",
            dashboard_url="https://fake_dashboard.com",
        )
        assert multiclient_init_called

    # Simulates ClientContext.__init__ from before changes from
    # https://github.com/ray-project/ray/pull/17942
    def no_multiclient_init(
        self,
        dashboard_url,
        python_version,
        ray_version,
        ray_commit,
        protocol_version,
        _num_clients,
    ):
        nonlocal no_multiclient_init_called
        no_multiclient_init_called = True

    with patch("ray.client_builder.ClientContext.__init__", no_multiclient_init):
        AnyscaleClientContext(
            anyscale_cluster_info=AnyscaleClientConnectResponse(cluster_id="cluster-1"),
            python_version=platform.python_version(),
            _num_clients=1,
            ray_version=RAY_VERSION,
            ray_commit=RAY_COMMIT,
            protocol_version="fake_version",
            dashboard_url="https://fake_dashboard.com",
        )
        assert no_multiclient_init_called


def test_preserve_build_and_cluster_compute_config(
    tmp_path: Path, project_test_data: Project
) -> None:
    """Sometimes, we try to connect to a cluster that already exists, rather
    than starting a new one. In this scenario, we sometimes want to preserve
    the existing cluster env and cluster compute config, and sometimes to replace them
    with new ones.

    We test that we replace/preserve the build and/or cluster-compute-config in
    the following scenarios:

    1. We set a new build_id, and we check that the new build_id is used.
    2. We don't set the build_id, and we check that the old build_id is used.
    3. We set a new cluster-compute-config, and we check that the new cluster-
        compute-config is used.
    4. We don't set the cluster-compute-config, and we check that the old
        cluster-compute-config is used.
    5. We set a new cloud, and we check that the default cluster-compute-config
        is used.
    6. We don't set the cloud, and we check that the old cluster-compute-config
        is used.
    """

    session_name = "cluster-0"
    old_build_id = "old_build_id"
    new_build_id = "build_id"
    old_cluster_compute_config_id = "old_cluster_compute_config"
    new_cluster_compute_config_id = "mock_compute_template_id"

    def create_builder():
        builder, sdk, _, _ = _make_test_builder(tmp_path, [])
        sdk.create_project.return_value = ProjectResponse(result=project_test_data)
        sdk.create_app_config.return_value = None

        session = _make_session(0, "Terminated")

        session.name = session_name
        session.build_id = old_build_id
        session.compute_template_id = old_cluster_compute_config_id

        cluster_compute = Mock()
        cluster_compute.id = new_cluster_compute_config_id
        cluster_compute_results = Mock()
        cluster_compute_results.results = [cluster_compute]
        builder._api_client.search_compute_templates_api_v2_compute_templates_search_post = Mock(
            return_value=cluster_compute_results
        )
        sdk.search_sessions = Mock(return_value=SessionListResponse(results=[session]))

        return builder

    # Scenario 1: We set a new build_id, and we check that the new build_id is
    # used.
    builder = create_builder()

    new_cluster_env_dict = {
        "name": "new_cluster_env",
        "base_image": "anyscale/ray:1.5.0-py37",
    }

    builder.session("cluster-0").cluster_env(new_cluster_env_dict).connect()

    assert len(builder._start_session.call_args_list)
    assert builder._start_session.call_args_list[0][1]["build_id"] == new_build_id

    # Scenario 2: We don't set the build_id, and we check that the old build_id
    # is used.
    builder = create_builder()

    builder.session("cluster-0").connect()

    assert len(builder._start_session.call_args_list)
    assert builder._start_session.call_args_list[0][1]["build_id"] == old_build_id

    # Scenario 3: We set a new cluster-compute-config, and we check that the new
    # cluster-compute-config is used.
    builder = create_builder()

    builder.session("cluster-0").cluster_compute("new_cluster_compute_name").connect()

    assert len(builder._start_session.call_args_list)
    assert (
        builder._start_session.call_args_list[0][1]["compute_template_id"]
        == new_cluster_compute_config_id
    )

    # Scenario 4: We don't set the cluster-compute-config, and we check that the
    # old cluster-compute-config is used.
    builder = create_builder()

    builder.session("cluster-0").connect()

    assert len(builder._start_session.call_args_list)
    assert (
        builder._start_session.call_args_list[0][1]["compute_template_id"]
        == old_cluster_compute_config_id
    )

    # Scenario 5: We set a new cloud, and we check that the default cluster-
    # compute-config is used.
    builder = create_builder()

    builder.session("cluster-0").cloud("new_cloud_name").connect()

    assert len(builder._start_session.call_args_list)
    assert (
        builder._start_session.call_args_list[0][1]["compute_template_id"]
        == new_cluster_compute_config_id
    )

    # Scenario 6: We don't set the cloud, and we check that the old cluster-
    # compute-config is used.
    builder = create_builder()

    builder.session("cluster-0").connect()

    assert len(builder._start_session.call_args_list)
    assert (
        builder._start_session.call_args_list[0][1]["compute_template_id"]
        == old_cluster_compute_config_id
    )


# ray.init("anyscale://"") only works on Ray 1.5+
init_connect_supported = version.parse(ray.__version__) >= version.parse("1.5")

# Check if ray.util.connect accepts ray_init_kwargs to forward
connect_sig = inspect.signature(ray.util.connect)
forward_init_args_supported = "ray_init_kwargs" in connect_sig.parameters


@pytest.mark.skipif(
    not forward_init_args_supported,
    reason="Forwarding init args isn't supported on this version of ray",
)
@pytest.mark.skipif(
    not init_connect_supported,
    reason="ray.init('anyscale://') isn't supported on this version of ray",
)
def test_forward_argument(mock_auth_api_client) -> None:
    """Tests ClientBuilder._forward_argument."""

    sdk = Mock()
    _api_client = Mock()
    connect_instance = ClientBuilder(
        anyscale_sdk=sdk,
        auth_api_client=Mock(api_client=_api_client, anyscale_api_client=Mock()),
    )

    # Should return false on arguments that aren't part of ray.init
    assert not connect_instance._forward_argument("somarg", 123)

    # Should return true on real arguments
    assert connect_instance._forward_argument("object_store_memory", 98765)
    assert connect_instance._forward_argument("log_to_driver", False)
    assert connect_instance._forward_argument("logging_level", logging.INFO)

    # Check values set properly
    assert connect_instance._ray_init_kwargs["object_store_memory"] == 98765
    assert connect_instance._ray_init_kwargs["log_to_driver"] is False
    assert connect_instance._ray_init_kwargs["logging_level"] == logging.INFO
    assert len(connect_instance._ray_init_kwargs) == 3
