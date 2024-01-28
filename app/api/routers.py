from fastapi import APIRouter

from app.api.endpoints import (charity_project_router, donation_router,
                               user_router)
from app.api.endpoints.google_api import router

main_router = APIRouter()
main_router.include_router(
    charity_project_router, prefix='/charity_project', tags=['charity_projects']
)
main_router.include_router(
    donation_router, prefix='/donation', tags=['donations']
)
main_router.include_router(
    router, prefix='/google', tags=['Google']
)
main_router.include_router(user_router)