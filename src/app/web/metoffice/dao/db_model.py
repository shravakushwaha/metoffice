from email.policy import default
from typing import Optional
from sqlalchemy import  Column
from sqlmodel import Field, SQLModel, DateTime
from datetime import datetime
from ...commons.enums import RegionTypeEnum,ParameterTypeEnum

class Metofiice(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    years: str = Field(default=None)                                            
    jan: Optional[str] = Field(default=None)
    feb: Optional[str] = Field(default=None)
    mar: Optional[str] = Field(default=None)
    apr: Optional[str] = Field(default=None)
    may: Optional[str] = Field(default=None)
    jun: Optional[str] = Field(default=None)
    jul: Optional[str] = Field(default=None)
    aug: Optional[str] = Field(default=None)
    sep: Optional[str] = Field(default=None)
    oct: Optional[str] = Field(default=None)
    nov: Optional[str] = Field(default=None)
    dec: Optional[str] = Field(default=None)
    win: Optional[str] = Field(default=None)
    spr: Optional[str] = Field(default=None)
    sum: Optional[str] = Field(default=None)
    aut: Optional[str] = Field(default=None)
    ann: Optional[str] = Field(default=None)
    region: RegionTypeEnum
    parameter: ParameterTypeEnum
    is_active: bool = Field(default=True)
    created_on: datetime = Field(default_factory=datetime.utcnow)
    modified_on: Optional[datetime] = Field(
        sa_column=Column(
            "modified_on",
            DateTime,
            default=datetime.utcnow,
            onupdate=datetime.utcnow,
        )
    )
    
    class Config:
        use_enum_values = True
        

# class Region(SQLModel, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True, index=True)
#     region: str 
#     is_active: bool = Field(default=True)
#     created_on: datetime = Field(default_factory=datetime.utcnow)
#     modified_on: Optional[datetime] = Field(
#         sa_column=Column(
#             "modified_on",
#             DateTime,
#             default=datetime.utcnow,
#             onupdate=datetime.utcnow,
#         )
#     )
    
#     class Config:
#         use_enum_values = True
        

# class Parameter(SQLModel, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True, index=True)
#     parameter: str 
#     is_active: bool = Field(default=True)
#     created_on: datetime = Field(default_factory=datetime.utcnow)
#     modified_on: Optional[datetime] = Field(
#         sa_column=Column(
#             "modified_on",
#             DateTime,
#             default=datetime.utcnow,
#             onupdate=datetime.utcnow,
#         )
#     )
    
#     class Config:
#         use_enum_values = True

