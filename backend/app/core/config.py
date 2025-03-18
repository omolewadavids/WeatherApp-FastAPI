from datetime import date

from starlette.config import Config

config = Config(".env")

PROJECT_NAME = "Weather-App"
VERSION = "1.0.0"
API_PREFIX = "/api"
GIT_AUTH = "Adaramola Omolewa"
GIT_MESSAGE = "You are doing great"
DEPLOY_DATE = date.today()

version = "1.0.0"
release_date = "2025-03-18"
status = "API Status"
commit_hash = "abc123def456gh789"
changelog_url ="https://example.com/changelog" # to keep track of the changes in the API/bug fixes
server ="FastAPI"
environment ="production"
uptime = "72 hours"
documentation_url ="https://example.com/docs"
license ="OMOLEWA Licence"
contact = {"name": "Omolewa Adaramola", "email": "omolewa.davids@gmail.com"}
