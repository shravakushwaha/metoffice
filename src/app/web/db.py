import os
from sqlalchemy import (
    Column,
    Boolean,
    DateTime,
    Integer,
    MetaData,
    String,
    Table,
    func,
    create_engine,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker
from app.config.config import get_settings
from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = get_settings().DB_URL

engine = create_async_engine(DATABASE_URL, pool_size=10, max_overflow=5)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


async def init_db():
    async with engine.begin() as conn:
        # await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        try:
            yield session
        except:
            await session.rollback()
        finally:
            await session.close()

async def disconnect_db():
    await engine.dispose()