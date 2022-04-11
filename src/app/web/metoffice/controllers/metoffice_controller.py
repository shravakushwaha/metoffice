from typing import List, Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio.session import AsyncSession
from fastapi_versioning import version
from app.web.commons.enums import LoggerAttributesEnum
from app.config.config import get_settings
import json
import traceback

from app.web.db import get_session
from ..dto import request_model
from ..services import metoffice_service
from ...commons import enums


router = APIRouter()



@router.post("", status_code=200)
@version(1)
async def create_metoffice(
    metoffice_model: request_model.CreateMetoffice,
    session: AsyncSession = Depends(get_session),
):
    metoffice_data = await metoffice_service.create_metoffice(
        metoffice_model=metoffice_model, session=session
    )
    return metoffice_data




@router.get("", status_code=200)
@version(1)
async def get_metoffice_by_search_criteria(
    search_criteria: request_model.SearchCriteriaMetoffice = Depends(),
    session: AsyncSession = Depends(get_session),
):
    metoffice = await metoffice_service.get_metoffice_by_search_criteria(
        session=session, search_criteria=search_criteria
    )
    return metoffice


@router.get("/weather", status_code=200)
@version(1)
async def get_metoffice_by_api(
    search_criteria: request_model.SearchCriteriaMetofficeByExistingAPI = Depends(),
    session: AsyncSession = Depends(get_session),
):
    metoffice = await metoffice_service.get_metoffice_by_api(
        session=session, search_criteria=search_criteria
    )
    return metoffice


@router.get("/migration/metoffice", status_code=200)
@version(1)
async def create_migration_metoffice(
    search_criteria: request_model.SearchCriteriaMetofficeByExistingAPI = Depends(),
    session: AsyncSession = Depends(get_session),
):
    try:
        metoffice_data = await metoffice_service.create_migration_metoffice(
            session=session,
            search_criteria=search_criteria
        )
        return metoffice_data
    except Exception as e:
        print("Exception===================",e)
        print("traceback=================",traceback.format_exc())