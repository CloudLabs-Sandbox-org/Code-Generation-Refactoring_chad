## Fetch weather data from OpenWeatherMap API https://openweathermap.org/

import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def fetch_weather(api_key, city):
    """Fetch current weather data for a city from OpenWeatherMap."""
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

# Example usage:
if __name__ == "__main__":
    API_KEY = os.getenv("OPENWEATHER_API_KEY")
    if not API_KEY:
        raise ValueError("Please set OPENWEATHER_API_KEY in your .env file")
    CITY = "Phoenix"
    weather = fetch_weather(API_KEY, CITY)
    print(weather)