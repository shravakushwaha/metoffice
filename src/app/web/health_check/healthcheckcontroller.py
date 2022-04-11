import requests
from requests import status_codes
from requests.api import patch
from requests.models import HTTPBasicAuth
from typing import AnyStr, Dict, List

# from app.sendgrid.mailclient import sendMail

# from requests.sessions import Request
from fastapi import APIRouter, HTTPException, Path, Request, Body
from fastapi_utils.tasks import repeat_every
from fastapi import Depends, FastAPI, HTTPException, status

router = APIRouter()


@router.get("/", status_code=200)
async def health_check():
    print("System is up and running...")
    return {"message": "System is up and running...."}
