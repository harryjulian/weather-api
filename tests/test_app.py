import pytest
from weather_app.app import app
from .util import random_string, cities

def test_load(client):
    resp = client.get('/')
    assert b'Weather API' in resp.data
    assert b'Welcome to this simple Weather API.' in resp.data
    assert b'To query the weather in a given city, input it below.' in resp.data

@pytest.mark.parametrize('input', cities)
def test_cities_correct(client, input):
    resp = client.post("/", data = {'city': input})
    assert b'This city name is invalid. Please try again.' not in resp.data

@pytest.mark.parametrize('input', [random_string() for _ in range(15)])
def test_cities_incorrect(client, input):
    resp = client.post("/", data = {'city': input})
    assert b'This city name is invalid. Please try again.' in resp.data