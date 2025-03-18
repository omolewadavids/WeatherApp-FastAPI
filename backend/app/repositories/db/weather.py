
from backend.app.repositories.db.base import BaseRepository


class UsersRepository(BaseRepository):
    """"
    All database actions associated with the Users resource
    """

    def __init__(self) -> None:
        super().__init__()
        self.auth_service = auth_service

