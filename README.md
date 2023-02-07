# weather-api
A small, robust weather API.

This is a simple weather API built using Flask. Given the name of a city, it will return 
the temperature, a written description of the weather and an icon which 
provides a visual description of conditions.

# Setup

To setup the app, first intall a virtual environment.

Then, install the dependencies.

```pip install -r requirements.txt```

Now, run the app.

```python weather_app/app.py```

Open your browser and visit ```localhost:5000``` to interact with the API.

To run all unit tests:

```pytest```