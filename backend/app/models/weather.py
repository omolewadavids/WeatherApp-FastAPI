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
