from fastapi import FastAPI,APIRouter,Depends
import os
from helpers.config import get_Settings,Settings
base_router=APIRouter(
    prefix="/api/v1",
    tags=["api_v1"],
)

@base_router.get("/")

async def welcom(app_settings:Settings=Depends(get_Settings)):
    app_settings = get_Settings()
    app_name=app_settings.APP_NAME
    app_version=app_settings.APP_VERSION

    return{"message":"hello word all from asmae !",
           "app_name":app_name,
           "app_version":app_version,}