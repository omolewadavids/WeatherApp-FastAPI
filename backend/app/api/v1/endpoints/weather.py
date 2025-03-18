from fastapi import APIRouter, Body

from starlette.status import (
    HTTP_201_CREATED,
)

from backend.app.models.user import UserCreate, UserPublic

router = APIRouter()


@router.post("/register", response_model=UserPublic, name="users:register-user", status_code=HTTP_201_CREATED)
async def register_new_user(
        new_user: UserCreate = Body(..., embed=True),
) ->UserPublic:

    pass