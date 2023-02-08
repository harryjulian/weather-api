# Parameters
API_KEY = 'a7c93eee9d8b811f918b557484939d0f' # Enter your API key here!
METRIC = True
DEBUG = False

# Column Names in API
COLUMNS = ['City', 'Temperature', 'Weather', 'Icon']
COLUMNS[1] += f' (C{chr(176)})' if METRIC else f' (F{chr(176)})'