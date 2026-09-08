from fastapi import FastAPI,APIRouter

import os

base_router=APIRouter(
    prefix="/api/v1",
    tags=["api_v1"],
)

@base_router.get("/")

async def welcom():
    app_name=os.getenv('APP_NAME')
    app_version=os.getenv('APP_VERSION')

    return{"message":"hello word all from asmae !",
           "app_name":app_name,
           "app_version":app_version,}