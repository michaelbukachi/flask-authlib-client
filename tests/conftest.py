import pytest
from flask import Flask
from flask.testing import FlaskClient

from tests.utils import JSONResponse


@pytest.fixture(scope='session')
def flask_app():
    app = Flask(__name__)
    yield app


@pytest.fixture(scope='module')
def client(flask_app):
    app = flask_app
    ctx = flask_app.test_request_context()
    ctx.push()
    app.test_client_class = FlaskClient
    app.response_class = JSONResponse
    return app.test_client()
