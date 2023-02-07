# Parameters
API_KEY = '' # Enter your API key here!
METRIC = False
DEBUG = True

# Column Names in API
COLUMNS = ['City', 'Temperature', 'Weather', 'Icon']
COLUMNS[0] += f' (C{chr(176)})' if METRIC else f' (F{chr(176)})'