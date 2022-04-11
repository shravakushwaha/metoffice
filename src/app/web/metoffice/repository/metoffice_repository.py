from datetime import datetime, timedelta
from operator import or_
from pydantic.main import BaseModel
from sqlalchemy import func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.sql.elements import and_
from ...commons import misc
from ..dao import db_model
from ..dto import request_model


async def create_metoffice(
    session: AsyncSession, metoffice_data: request_model.CreateMetoffice
):
    db_new_metoffice = db_model.Metofiice.from_orm(metoffice_data)
    session.add(db_new_metoffice)
    await session.commit()
    await session.refresh(db_new_metoffice)
    return db_new_metoffice



async def get_metoffice_by_search_criteria(
    session: AsyncSession, query_statement: BaseModel
):
    result = await session.execute(query_statement)
    warehouse = result.scalars().all()
    return warehouse


