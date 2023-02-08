# weather-api
A small, robust weather API.

This is a simple weather API built using Flask. Given the name of a city, it will return 
the temperature, a written description of the weather and an icon which 
provides a visual description of conditions.

# Setup

To run the app, follow these step-by-step instructions.

1. Setup your virtual environment.

> ```$ python3 -m venv venv```

2. Ensure the virtual environment is activated. On MacOS, the command is:

> ```$ source venv/bin/activate```

3. Install the dependencies in your virtual environment.

> ```$ pip install -r requirements.txt```

4. Before running the API you need to enter your own API Key, which can be obtained from
https://openweathermap.org/. In ```weather_app/config.py``` paste your key into the empty ```API_KEY```
string.

5. Before we run the app let's run the test suite to ensure everything is in order. This is important, 
as it also checks the validity of your API key.

> ```$ pytest```

6. Now, run the app.

> ```$ python weather_app/app.py```

7. Open your browser and enter ```localhost:5000``` in your search bar to load the API.
Enter some city names to start exploring the weather across the globe.
