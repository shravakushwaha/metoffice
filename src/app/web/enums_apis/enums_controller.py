from re import search
from typing import List, Optional
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio.session import AsyncSession
from fastapi_versioning import version

from app.web.db import get_session
from app.web.commons import  enums

router = APIRouter()


@router.get("/region", status_code=200)
@version(1)
async def fetch_region_list():
    region_list = [e.value for e in enums.RegionTypeEnum]
    return region_list



@router.get("/parameter", status_code=200)
@version(1)
async def fetch_parameter_list():
    parameter_list = [e.value for e in enums.ParameterTypeEnum]
    return parameter_list    

