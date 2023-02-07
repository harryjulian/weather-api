import requests
from weather_app.config import *

def test_key():
    assert isinstance(API_KEY, str)

def test_key_valid():
    url = f"http://api.openweathermap.org/geo/1.0/direct?q=manchester,&limit={1}&appid={API_KEY}"
    resp = requests.get(url)
    assert resp.status_code == 200

def test_columns():
    assert isinstance(COLUMNS, list)

def test_debug():
    assert isinstance(DEBUG, bool)

def test_metric():
    assert isinstance(METRIC, bool)