from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import requests
import os
from dotenv import load_dotenv

app = FastAPI(title="Weather Checker",
              version="1.0.0",
              description="Sample weather app to practice terraform IaC")

# Get API Key From Environment
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
if not API_KEY:
    raise ValueError("OPENWEATHER_API_KEY environment variable not set.")

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Landing page with instructions."""
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/weather/{city_name}")
async def get_weather(city_name: str):
    """_summary_

    Args:
        city_name (str): _description_

    Raises:
        HTTPException: _description_
        HTTPException: _description_
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "imperial",
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        weather_data = response.json()

        temperature = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]
        humidity = weather_data["main"]["humidity"]
        city = weather_data["name"]
        country = weather_data.get("sys", {}).get("country")
        pressure = weather_data["main"]["pressure"]
        wind_speed = weather_data["wind"]["speed"]

        return {
            "city": city,
            "country": country,
            "temperature": temperature,
            "description": description,
            "humidity": humidity,
            "pressure": pressure,
            "wind_speed": wind_speed,
        }

    except requests.exceptions.RequestException as e:
        if response.status_code == 404:
            raise HTTPException(status_code=404,
                                detail="City not found")
        else:
            raise HTTPException(status_code=500,
                                detail=f"Error fetching weather data: {e}")

    except (KeyError, IndexError) as e:
        raise HTTPException(status_code=500,
                            detail=f"Error parsing weather data: {e}. Check API response format.")