import logging
import pandas as pd
from flask import Flask, request, render_template
import requests

logging.basicConfig(filename = 'app', level = logging.INFO)

# Initalise & Configure!
app = Flask(__name__)
app.config.from_pyfile('config.py')
app.config['COLUMNS'][1] += ' (C)' if app.config['METRIC'] else ' (F)'
df = pd.DataFrame(columns = app.config['COLUMNS'])

@app.route('/', methods=['POST', 'GET'])
def home(df: pd.DataFrame = df):
    if request.method == 'POST':

        # Get lat/long for a given city
        city = request.form.get("city")
        logging.info(f"Attempting to retrieve weather for {city}.")
        geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city},&limit={1}&appid={app.config['API_KEY']}"
        geo_response = requests.get(geo_url)
        geo_resp = geo_response.json()[0]

        # Get weather for given lat/long
        units = 'metric' if app.config['METRIC'] else 'imperial'
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={geo_resp['lat']}&lon={geo_resp['lon']}&appid={app.config['API_KEY']}&units={units}"
        weather_response = requests.get(weather_url)
        weather_resp = weather_response.json()
        city_data = [
            city,
            weather_resp['main']['temp'],
            weather_resp['weather'][0]['description'].capitalize(),
            weather_resp['weather'][0]['icon']
        ]
        logging.info(f'Retrieved city weather data: {city_data}.')
        df = df.append({i:j for i, j in zip(app.config['COLUMNS'], city_data)}, ignore_index = True)
        return render_template('home.html', table = df.to_html())
    else:
        return render_template('home.html')

if __name__ == '__main__':
    app.run(port=5000, use_reloader=False, debug = app.config['DEBUG'])