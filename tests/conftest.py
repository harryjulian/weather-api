import pytest
from weather_app.app import app

@pytest.fixture()
def client():
    return app.test_client()

@pytest.fixture()
def runner():
    return app.test_cli_runner()
