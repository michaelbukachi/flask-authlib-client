import pytest
import requests_mock as rm
from authlib.integrations.flask_client import OAuth

from flask_authlib_client import AuthClient


class Config:
    RESOURCE_SERVER_INTROSPECTION_URL = 'http://someurl'
    RESOURCE_SERVER_INTROSPECTION_CREDENTIALS = ('test', 'test')


def valid_token():
    return {
        'active': True,
        'scope': 'home'
    }


def valid_token__bad_scope():
    return {
        'active': True,
        'scope': 'clients'
    }


def invalid_token():
    return {
        'active': False
    }


@pytest.fixture(scope='module')
def auth_client(flask_app):
    flask_app.config.from_object(Config)
    oauth = OAuth(flask_app)
    ac = AuthClient(flask_app, oauth)

    @flask_app.route('/')
    @ac.require_oauth('home')
    def example():
        return 'Ok'

    yield ac


def test_failed_token_validation__no_token(client, auth_client):
    res = client.get('/')
    assert res.unauthorized


def test_failed_token_validation__bad_token(requests_mock, client, auth_client):
    requests_mock.post(rm.ANY, json=invalid_token())
    headers = {
        'Authorization': 'Bearer 1245'
    }
    res = client.get('/', headers=headers)
    assert res.unauthorized


def test_failed_token_validation__wrong_scope(requests_mock, client, auth_client):
    requests_mock.post(rm.ANY, json=valid_token__bad_scope())
    headers = {
        'Authorization': 'Bearer 1245'
    }
    res = client.get('/', headers=headers)
    assert res.unauthorized


def test_successful_authorization(requests_mock, client, auth_client):
    requests_mock.post(rm.ANY, json=valid_token())
    headers = {
        'Authorization': 'Bearer 1245'
    }
    res = client.get('/', headers=headers)
    assert res.ok
