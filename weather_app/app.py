import logging
import warnings
from flask import Flask, request, render_template, Markup
import requests
from requests.exceptions import HTTPError, JSONDecodeError
import pandas as pd

# Configure Logging
logging.basicConfig(filename = 'app', level = logging.INFO)
warnings.simplefilter(action='ignore', category=FutureWarning)

# Configure App
app = Flask(__name__)
app.config.from_pyfile('config.py')
df = pd.DataFrame(columns = app.config['COLUMNS'])
longitude, latitude = (-180, 180), (-90, 90)

@app.route('/', methods=['POST', 'GET'])
def home(df: pd.DataFrame = df):
    if request.method == 'POST':

        # Get lat/long for a given city
        city = request.form.get("city")
        logging.info(f"Attempting to retrieve weather for {city}.")
        geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city},&limit={1}&appid={app.config['API_KEY']}"

        # Send request
        try:
            geo_response = requests.get(geo_url)
            if geo_response.status_code != 200:
                raise HTTPError
        except requests.exceptions.HTTPError as e:
            logging.exception(f"{geo_response.status_code} error whilst querying for {city}.")
            return render_template('home.html', error = f'{geo_response.status_code} error.')

        # Unpack request
        try:
            geo_resp = geo_response.json()
        except JSONDecodeError as e:
            err = "Error decoding the lat/long JSON."
            logging.exception(err)
            return render_template('home.html', error = err)
        try:
            if len(geo_resp) == 0:
                raise InvalidCityException
            else:
                geo_resp = geo_resp[0]
        except InvalidCityException as e:
            logging.exception(e.message)
            return render_template('home.html', error = e.message)

        # Validate values for latitude & longitude
        lat, lon = geo_resp['lat'], geo_resp['lon']
        try:
            assert lat > latitude[0] and lat < latitude[1]
            assert lon > longitude[0] and lon < longitude[1]
        except AssertionError as e:
            err = 'Returned lat/long values out of bounds.'
            logging.exception(err)
            return render_template('home.html', error = err)

        # Get weather for given lat/long
        units = 'metric' if app.config['METRIC'] else 'imperial'
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={app.config['API_KEY']}&units={units}"

        # Send request
        try:
            weather_response = requests.get(weather_url)
            if weather_response.status_code == 401:
                raise HTTPError
        except requests.exceptions.HTTPError as e:
            logging.exception(f"{weather_response.status_code} error whilst querying for {city}.")
            return render_template('home.html', error = f'{weather_response.status_code} error.')
        
        # Unpack request
        try:
            weather_resp = weather_response.json()
        except JSONDecodeError as e:
            err = "Error decoding the weather JSON."
            logging.exception(err)
            return render_template('home.html', error = err)
        
        # Construct Object to return to API
        icon = weather_resp['weather'][0]['icon']
        city_data = [
            city.lower().title(),
            weather_resp['main']['temp'],
            weather_resp['weather'][0]['description'].capitalize(),
            f'static/icons/{icon}.png'
        ]
        logging.info(f'Retrieved city weather data: {city_data}.')
        df = df.append({i:j for i, j in zip(app.config['COLUMNS'], city_data)}, ignore_index = True)
        return render_template(
            'home.html', 
            table = df.to_html(
                escape=False,
                formatters = {'Icon': lambda s: f'<img src="{s}" width="70" height="70">'},
                index = False,
                justify = 'left'
                )
            )
    else:
        return render_template('home.html')

class InvalidCityException(Exception):
    
    def __init__(self):
        self.message = 'This city name is invalid. Please try again.'

if __name__ == '__main__':
    app.run(port=5000, use_reloader=False, debug = app.config['DEBUG'])
