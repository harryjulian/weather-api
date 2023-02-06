from weather_app.config import *

def test_key():
    assert isinstance(API_KEY, str)

def test_columns():
    assert isinstance(COLUMNS, list)

def test_debug():
    assert isinstance(DEBUG, bool)

def test_metric():
    assert isinstance(METRIC, bool)