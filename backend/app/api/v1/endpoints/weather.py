import json

from fastapi import FastAPI, APIRouter, Body, Depends, HTTPException, Path, File, UploadFile

from starlette.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_404_NOT_FOUND,
    HTTP_422_UNPROCESSABLE_ENTITY,
)

from fastapi.security import OAuth2PasswordRequestForm

from backend.app.models.weather import WeatherResponse
from backend.app.db.repositories.weather import WeatherRepository
from backend.app.api.v1.dependencies.database import get_repository

router = APIRouter()


@router.get("/{city}/", response_model=WeatherResponse, name="users:get-weather-by-city")
async def get_weather_by_city(
        query: str,  # query parameter for the city
        city: str,  # Path parameter for the city
        weather_repo: WeatherRepository = Depends(get_repository(WeatherRepository))
) -> WeatherResponse:
    info = await weather_repo.get_weather_by_city(city=city, query=query)

    if not info:
        raise HTTPException(status_code=404, detail="City not found")

    return info
