
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


class BaseRepository:
    """
    simple class needed only to keep a reference to Weather API.
    In the future we can add functionality for common API actions

    """
    def __init__(self) -> None:
        self.base_url = BASE_URL
