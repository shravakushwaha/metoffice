# from app.api import notes, ping

from app.web.db import disconnect_db
from app.web.health_check import healthcheckcontroller
from app.web.metoffice.controllers import metoffice_controller
from app.web.enums_apis import enums_controller
from fastapi import FastAPI, Request, Response, status
from starlette.middleware import Middleware
from fastapi_versioning import VersionedFastAPI
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.cors import CORSMiddleware
import time
import os
import uvicorn

# from sqlalchemy.orm import Session
# from app.web.products.dao import models
# from app.web.db import engine, get_db

# models.Base.metadata.create_all(bind=engine)
# from app.web.database.db import init_db


origins = [
    "http://localhost:8002",
    "https://localhost:8002",
    "http://localhost:3001",
    "http://localhost",
    "*",
]

middlewares = [
    # Setup CORS
    Middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    ),
    # Enable GZip
    Middleware(GZipMiddleware, minimum_size=1000),
    # Setup Trusted Host
    Middleware(TrustedHostMiddleware, allowed_hosts=["*"]),
    # authenticaiton middleware
    # Middleware(AuthMiddleware)
]

app = FastAPI(title="metoffice", middleware=middlewares)

# Setup Upload File Limit to 10 MB
MAX_CONTENT_LENGTH = 10_000_000
MIN_DOCUMENT_LENGTH = 50000


@app.middleware("http")
async def checkUploadedFileLength(request: Request, call_next):
    if request.method == "POST":
        if request.method == "POST":
            if "content-length" not in request.headers:
                return Response(
                    status_code=status.HTTP_411_LENGTH_REQUIRED,
                    content="content-length header is missing!",
                )
            content_length = int(request.headers["content-length"])
            if content_length > MIN_DOCUMENT_LENGTH and content_length <= MAX_CONTENT_LENGTH:
                time.sleep(1)
            if content_length > MAX_CONTENT_LENGTH:
                return Response(
                    status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
                    content="File size is too large!",
                )
    return await call_next(request)


@app.on_event("startup")
async def on_startup():
    # get_db()
    # await init_db()
    print("metoffice App started.....")


@app.on_event("shutdown")
async def shutdown():
    print("metoffice App shutdown....")
    # await database.disconnect()
    await disconnect_db()


app.include_router(healthcheckcontroller.router, prefix="/heathcheck", tags=["health-check"])
app.include_router(metoffice_controller.router, prefix="/metoffice", tags=["metoffice"])
app.include_router(enums_controller.router, prefix="/enums", tags=["enums"])


app = VersionedFastAPI(
    app,
    version_format="{major}",
    prefix_format="/metoffice/v{major}",
    middleware=middlewares,
)

# if __name__ == "__main__":
#     uvicorn.run(app,host="0.0.0.0",port=8002)
