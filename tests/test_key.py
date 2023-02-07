import requests
import pytest
from weather_app.config import API_KEY
from .util import random_string

def test_key_valid():
    url = f"http://api.openweathermap.org/geo/1.0/direct?q=manchester,&limit={1}&appid={API_KEY}"
    resp = requests.get(url)
    assert resp.status_code == 200

@pytest.mark.parametrize('input', [random_string() for _ in range(5)])
def test_key_invalid(input):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q=manchester,&limit={1}&appid={input}"
    resp = requests.get(url)
    assert resp.status_code != 200
