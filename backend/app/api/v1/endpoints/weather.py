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

router = APIRouter()


@router.get("/{city}/", response_model=WeatherResponse, name="users:get-weather-by-city")
async def get_weather_by_city(
        # city: str, users_repo: UsersRepository = Depends(get_repository(UsersRepository))
) -> WeatherResponse:
    # info = await weather_repo.get_weather_by_city(cityname=city)
    #
    # if not info:
    #     raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="City not found")
    #
    # return info
    pass