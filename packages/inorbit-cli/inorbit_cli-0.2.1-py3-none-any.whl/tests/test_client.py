# Copyright (c) 2021, InOrbit, Inc.
# All rights reserved.

import inorbit.exceptions
from inorbit import client
from inorbit.constants import DEFAULT_URL
from inorbit.client import InOrbit
import pytest

def test_client_defaults():
    # InOrbit client API KEY default value can
    # be found in the `tox.ini` file.
    assert client.api_key == "foo"

    # Test client uses `DEFAULT_URL` by default
    assert client._url == DEFAULT_URL

    # Test if API auth headers are configured correctly
    assert 'X-Auth-InOrbit-App-Key' in client.headers
    assert client.headers['X-Auth-InOrbit-App-Key'] == "foo"

def test_client_init():
    # Test exception raised when no `api_key` is provided
    with pytest.raises(ValueError):
        _ = InOrbit()
    
    # Test `DEFAULT_URL` is used when no client `url` is specified
    test_client = InOrbit(api_key="foo")
    assert test_client.api_key == "foo"
    assert test_client._url == DEFAULT_URL

    # Test happy path
    test_client = InOrbit(api_key="foo", url="https://foobar.com")
    assert test_client._url == "https://foobar.com"

    # Check trailing `/` are removed
    test_client = InOrbit(api_key="foo", url="https://foobar.com/")
    assert test_client._url == "https://foobar.com"

def test_client_build_url_method():
    # Create client for testing
    test_client = InOrbit(api_key="foo", url="https://foobar.com")

    # Test build url prepend base url
    assert test_client._build_url('/baz') == "https://foobar.com/baz"
    # Test build url ignores base url whn path starts with `http` or `https`
    assert test_client._build_url('http://foo.bar/baz') == "http://foo.bar/baz"
    assert test_client._build_url('https://foo.bar/baz') == "https://foo.bar/baz"

def test_client_get_session_opts():
    # Create client for testing
    test_client = InOrbit(api_key="foo", url="https://foobar.com")

    client_session_opts = test_client._get_session_opts()
    assert client_session_opts == {'headers': {'X-Auth-InOrbit-App-Key': 'foo'}}

def test_client_http_request(requests_mock):
    test_client = InOrbit(api_key="foo", url="https://test.com")
    requests_mock.get('http://test.com/foo', json={"foo": "bar"})
    response = test_client.http_request('get', 'http://test.com/foo').json()
    assert response == {"foo": "bar"}

    with pytest.raises(inorbit.exceptions.InOrbitAuthenticationError) as excinfo:
        requests_mock.get(
            'http://test.com/foo', status_code=403,
            json={"error": "AUTHENTICATION_ERROR: wrong credentials"})
        _ = test_client.http_request('get', 'http://test.com/foo')

    assert excinfo.value.args[0] == "AUTHENTICATION_ERROR: wrong credentials"

    with pytest.raises(inorbit.exceptions.InOrbitError) as excinfo:
        requests_mock.get(
            'http://test.com/foo', status_code=500)
        _ = test_client.http_request('get', 'http://test.com/foo')

    assert excinfo.value.args[0] == "Unexpected error (500)"