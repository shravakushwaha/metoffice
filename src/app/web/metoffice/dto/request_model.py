import numbers
import re
from token import OP
from typing import Counter, List, Optional
from pydantic import BaseModel
from datetime import datetime
from fastapi.param_functions import Form
from sqlmodel.main import SQLModel
from fastapi import Query
from ...commons import enums


class CreateMetoffice(BaseModel):
    id: Optional[int]
    years: int                                           
    jan: Optional[str]
    feb: Optional[str]
    mar: Optional[str]
    apr: Optional[str]
    may: Optional[str]
    jun: Optional[str]
    jul: Optional[str]
    aug: Optional[str]
    sep: Optional[str]
    oct: Optional[str]
    nov: Optional[str]
    dec: Optional[str]
    win: Optional[str]
    spr: Optional[str]
    sum: Optional[str]
    aut: Optional[str]
    ann: Optional[str]
    region: enums.RegionTypeEnum
    parameter: enums.ParameterTypeEnum
    
    class Config:
        orm_mode = True
     
        
class MetofficeResponse(BaseModel):
    id: Optional[int]
    years: Optional[int]                                         
    jan: Optional[str]
    feb: Optional[str]
    mar: Optional[str]
    apr: Optional[str]
    may: Optional[str]
    jun: Optional[str]
    jul: Optional[str]
    aug: Optional[str]
    sep: Optional[str]
    oct: Optional[str]
    nov: Optional[str]
    dec: Optional[str]
    win: Optional[str]
    spr: Optional[str]
    sum: Optional[str]
    aut: Optional[str]
    ann: Optional[str]
    
    class Config:
        orm_mode = True
        
###########################################
####### Search Criteria ###################
###########################################
    
class SearchCriteriaMetoffice(BaseModel):
    region: Optional[enums.RegionTypeEnum]
    parameter: Optional[enums.ParameterTypeEnum]
    type: Optional[str]
    
    is_active: Optional[str] = Query("")
    page_size: Optional[int] = Query(
        20, strict=True, ge=20, le=200, multiple_of=1
        # 20, strict=True, multiple_of=1
    )
    current_page: Optional[int] = Query(1, strict=True, ge=1)

class Config:
    orm_mode = True


class SearchCriteriaMetofficeByExistingAPI(BaseModel):
    region: enums.RegionTypeEnum
    parameter: enums.ParameterTypeEnum
    type: Optional[str] = Query("date")

class Config:
    orm_mode = True