"""Author: Adaramola, Bukola Omolewa"""

from backend.app.models.core import CoreModel


class WeatherResponse(CoreModel):
    temperature: float
    description: str
    humidity: float
    pressure: float
    country: str
    wind_speed: float


class WeatherPredictionResponse(CoreModel):
    will_temperature_rise: bool


"""
 temperature = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]
        humidity = weather_data["main"]["humidity"]
        city = weather_data["name"]
        country = weather_data.get("sys", {}).get("country")
        pressure = weather_data["main"]["pressure"]
        wind_speed = weather_data["wind"]["speed"]

"""