from fastapi import APIRouter
from fastapi.responses import FileResponse
from starlette.status import HTTP_200_OK

from backend.app.models.version import Version
from backend.app.core import config
from backend.app.utils.logging_config import get_logger

log = get_logger()

router = APIRouter()


@router.get(
    "/",
    response_model=Version,
    name="version:get-current-version",
    status_code=HTTP_200_OK
)
async def get_current_version() -> Version:
    log.info("IHC Version requested", service="get-current-version")
    return Version.parse_obj(
        {
            "version": config.VERSION,
            "git_hash": config.GIT_HASH,
            "git_auth": config.GIT_AUTH,
            "git_message": config.GIT_MESSAGE,
            "deploy_date": config.DEPLOY_DATE,
        }
    )


@router.get("/openapi.yaml", include_in_schema=False)
def get_openapi_yaml():
    log.info("IHC Version requested", service="get-current-version")
    return FileResponse("openapi.yaml", media_type="text/yaml")
