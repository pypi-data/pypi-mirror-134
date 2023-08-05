# Copyright (c) 2021, InOrbit, Inc.
# All rights reserved.
from pathlib import Path
from unittest import mock

import pytest
from click.testing import CliRunner
from inorbit.cli import apply_config
from inorbit.cli import describe_robots
from inorbit.cli import get_robots
from inorbit.cli import list_config
from inorbit.client import InOrbit


@pytest.mark.parametrize(
    "robot_name,response",
    [
        (
            "gont",
            [
                {
                    "id": "121400628",
                    "name": "gont",
                    "agentVersion": "2.3.1",
                    "agentOnline": False,
                    "updatedTs": 1588596807808,
                }
            ],
        )
    ],
)
def test_get_robots(requests_mock, robot_name, response):
    test_client = InOrbit(api_key="foo", url="https://foobar.com")
    # mock CLI client and API
    with mock.patch("inorbit.cli.client", test_client):
        requests_mock.get("https://foobar.com/robots", json=response)

        # call `get_robots`` command and validate output
        runner = CliRunner()
        result = runner.invoke(get_robots)
        assert result.exit_code == 0
        assert robot_name in result.stdout


@pytest.mark.parametrize(
    "robot_name,response",
    [
        (
            "gont",
            [
                {
                    "id": "121400628",
                    "name": "gont",
                    "agentVersion": "2.3.1",
                    "agentOnline": False,
                    "updatedTs": 1588596807808,
                }
            ],
        )
    ],
)
def test_describe_robots(requests_mock, robot_name, response):
    test_client = InOrbit(api_key="foo", url="https://foobar.com")
    # mock CLI client and API
    with mock.patch("inorbit.cli.client", test_client):
        requests_mock.get("https://foobar.com/robots", json=response)

        # call `describe_robots` command and validate output
        runner = CliRunner()
        result = runner.invoke(describe_robots)
        assert result.exit_code == 0
        assert robot_name in result.stdout
        assert "last seen" in result.stdout
        assert "2020-05-04T09:53:27.808000" in result.stdout


@pytest.mark.parametrize(
    "response",
    [
        (
            [
                {
                    "id": "121400628",
                    "scope": "*",
                    "kind": "Incident",
                    "apiVersion": "v0.1",
                    "description": "foo",
                }
            ]
        )
    ],
)
def test_apply_config(requests_mock, response):
    test_client = InOrbit(api_key="foo", url="https://foobar.com")
    test_config_file = Path(__file__).absolute().parent / "sample_config.json"

    with mock.patch("inorbit.cli.client", test_client):
        requests_mock.post("/configuration/apply", text="Configuration applied")
        # call `apply_config` command and validate output
        runner = CliRunner()
        result = runner.invoke(apply_config, [str(test_config_file)])
        assert result.exit_code == 0
        assert "Configuration applied" in result.stdout

    with mock.patch("inorbit.cli.client", test_client):
        requests_mock.post("/configuration/apply", text="FIXME", status_code=400)

        runner = CliRunner()
        result = runner.invoke(apply_config, [str(test_config_file)])
        assert result.exit_code == 1
        assert "Error: Unexpected error (400)" in result.stdout

    # Assert all calls had the correct payload
    for i in range(2):
        assert "kind" in requests_mock.request_history[i].json()
        assert "metadata" in requests_mock.request_history[i].json()
        assert "spec" in requests_mock.request_history[i].json()
        assert "apiVersion" in requests_mock.request_history[i].json()


{
    "items": [
        {
            "scope": "root",
            "id": "cpuLoadPercentage",
            "label": "CPU usage",
            "suppressed": False,
            "kind": "IncidentDefinition",
        },
        {
            "scope": "root",
            "id": "diskUsagePercentage",
            "label": "Disk usage",
            "suppressed": False,
            "kind": "IncidentDefinition",
        },
        {
            "scope": "root",
            "id": "rosMasterStatus",
            "label": "ROS Status",
            "suppressed": False,
            "kind": "IncidentDefinition",
        },
        {
            "scope": "root",
            "id": "rosDiagnosticsStatus",
            "label": "ROS Diagnostics",
            "suppressed": False,
            "kind": "IncidentDefinition",
        },
        {
            "scope": "company",
            "id": "distanceLinear",
            "label": None,
            "suppressed": True,
            "kind": "IncidentDefinition",
        },
        {
            "scope": "company",
            "id": "networkTotalRate",
            "label": None,
            "suppressed": True,
            "kind": "IncidentDefinition",
        },
        {
            "scope": "company",
            "id": "rosMasterStatus",
            "label": None,
            "suppressed": True,
            "kind": "IncidentDefinition",
        },
        {
            "scope": "company",
            "id": "21cr1yMXq4tGkisD",
            "label": "batteryCharge",
            "suppressed": False,
            "kind": "IncidentDefinition",
        },
        {
            "scope": "company",
            "id": "v-7EiGmO8Gm5wqss",
            "label": None,
            "suppressed": True,
            "kind": "IncidentDefinition",
        },
        {
            "scope": "company",
            "id": "apDQuQhfZhW4pi7E",
            "label": None,
            "suppressed": True,
            "kind": "IncidentDefinition",
        },
        {
            "scope": "company",
            "id": "cpuLoadPercentage",
            "label": "My CPU INC",
            "suppressed": False,
            "kind": "IncidentDefinition",
        },
    ]
}


@pytest.mark.parametrize(
    "response",
    [
        (
            {
                "items": [
                    {
                        "id": "cpuLoadPercentage",
                        "kind": "IncidentDefinition",
                        "label": "My CPU incident",
                        "scope": "company",
                        "suppressed": False,
                    }
                ]
            }
        )
    ],
)
def test_list_config(requests_mock, response):
    test_client = InOrbit(api_key="foo", url="https://foobar.com")
    # mock CLI client and API
    with mock.patch("inorbit.cli.client", test_client):
        requests_mock.get("https://foobar.com/configuration/list", json=response)

        runner = CliRunner()
        result = runner.invoke(list_config)
        assert result.exit_code == 0
        assert "cpuLoadPercentage" in result.stdout
        assert "IncidentDefinition" in result.stdout
        assert "My CPU incident" in result.stdout
        assert "company" in result.stdout
