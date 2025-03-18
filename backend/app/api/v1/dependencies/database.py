"""I treat the Weather API as a database of weather records"""

from typing import Callable, Type

from fastapi import Depends

from backend.app.repositories.db.base import BaseRepository
from backend.app.models.weather import WeatherAppURL, WeatherGetType


def get_base_url(request_type: str, repo: BaseRepository = Depends(BaseRepository)) -> WeatherAppURL:
    """
    Get the base URL from the repository based on the request type.
    """
    return repo.base_url


def get_repository(repo_type: Type[BaseRepository]) -> Callable:
    def get_repo(request_url: str = Depends(get_base_url)) -> BaseRepository:
        # Create an instance of the repository using the request_url (base_url)
        repo_instance = repo_type(request_type=request_url)

        return repo_instance

    return get_repo
