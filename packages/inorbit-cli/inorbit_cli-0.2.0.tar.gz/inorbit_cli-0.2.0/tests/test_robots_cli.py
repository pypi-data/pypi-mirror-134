# Copyright (c) 2021, InOrbit, Inc.
# All rights reserved.

import pytest
from inorbit.client import InOrbit
from click.testing import CliRunner
from inorbit.cli import get_robots
from inorbit.cli import describe_robots
from unittest import mock


@pytest.mark.parametrize("robot_name,response", [
    ("gont", [{"id": "121400628", "name": "gont", "agentVersion": "2.3.1", "agentOnline": False, "updatedTs": 1588596807808}])
])
def test_get_robots(requests_mock, robot_name, response):
    test_client = InOrbit(api_key="foo", url="https://foobar.com")
    # mock CLI client and API
    with mock.patch('inorbit.cli.client', test_client):
        requests_mock.get('https://foobar.com/robots', json=response)

        # call `get_robots`` command and validate output
        runner = CliRunner()
        result = runner.invoke(get_robots)
        assert result.exit_code == 0
        assert robot_name in result.stdout


@pytest.mark.parametrize("robot_name,response", [
    ("gont", [{"id": "121400628", "name": "gont", "agentVersion": "2.3.1", "agentOnline": False, "updatedTs": 1588596807808}])
])
def test_describe_robots(requests_mock, robot_name, response):
    test_client = InOrbit(api_key="foo", url="https://foobar.com")
    # mock CLI client and API
    with mock.patch('inorbit.cli.client', test_client):
        requests_mock.get('https://foobar.com/robots', json=response)

        # call `describe_robots`` command and validate output
        runner = CliRunner()
        result = runner.invoke(describe_robots)
        assert result.exit_code == 0
        assert robot_name in result.stdout
        assert "last seen" in result.stdout
        assert "2020-05-04T12:53:27.808000Z" in result.stdout