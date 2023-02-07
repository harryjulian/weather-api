import pytest
from weather_app.app import app
from weather_app.exceptions import InvalidCityException
from .util import random_string, cities

@pytest.mark.parametrize('input', cities)
def test_cities_correct(client, input):
    resp = client.post("/", data = {'city': input})
    assert resp.status_code == 200

@pytest.mark.parametrize('input', [random_string() for _ in range(15)])
def test_cities_incorrect(client, input):
    resp = client.post("/", data = {'city': input})
    assert b'<h2 style = "color:red;font-family: Arial"> The city name is invalid.</h2>\n</body>\n' in resp.data