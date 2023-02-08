# Parameters
API_KEY = '' # Enter your API key here!
METRIC = True
DEBUG = False

# Column Names in API
COLUMNS = ['City', 'Temperature', 'Weather', 'Icon']
COLUMNS[1] += f' (C{chr(176)})' if METRIC else f' (F{chr(176)})'
