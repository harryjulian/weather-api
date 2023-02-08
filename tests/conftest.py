import pytest
from weather_app.app import app

@pytest.fixture()
def client():
    return app.test_client()
