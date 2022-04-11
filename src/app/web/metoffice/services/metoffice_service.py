import traceback
from cv2 import split
from sqlalchemy import null, true
from ..dao import db_model
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from ..dto import request_model
from ..repository import metoffice_repository
import requests
import json
import os
from ...commons import enums

async def create_metoffice(
    metoffice_model: request_model.CreateMetoffice, session: AsyncSession
):
    
    db_new_metoffice = await metoffice_repository.create_metoffice(
        session=session, metoffice_data=metoffice_model
    )
    return db_new_metoffice

    
async def get_metoffice_by_search_criteria(
    session: AsyncSession,
    search_criteria: request_model.SearchCriteriaMetoffice
):
    offset = (search_criteria.current_page - 1) * search_criteria.page_size
    limit = search_criteria.page_size
    query_statement =  generate_metoffice_query_statement(search_criteria=search_criteria).offset(offset).limit(limit)
    
    metoffice_list = await metoffice_repository.get_metoffice_by_search_criteria(
        query_statement=query_statement, session=session
    )
    metoffice_data_list = []
    for items in metoffice_list:
        if search_criteria.type == "date":
            metoffice = request_model.MetofficeResponse.from_orm(items)
            metoffice_data_list.append(metoffice)
        else:
            
            jan_data = {}
            feb_data = {}
            mar_data = {}
            apr_data = {}
            jun_data = {}
            may_data = {}
            jul_data = {}
            aug_data = {}
            sep_data = {}
            oct_data = {}
            nov_data = {}
            dec_data = {}
            win_data = {}
            spr_data = {}
            sum_data = {}
            aut_data = {}
            ann_data = {}
            metoffice_json= {}
            jan_data["id"] = items.id;
            jan_data["jan"] = items.jan;
            jan_data["year_jan"] = items.years;
            feb_data["feb"] = items.feb;
            feb_data["year_feb"] = items.years;
            mar_data["mar"] = items.mar;
            mar_data["year_mar"] = items.years;
            
            apr_data["apr"] = items.jan;
            apr_data["year_may"] = items.years;
            may_data["may"] = items.feb;
            may_data["year_may"] = items.years;
            jun_data["jun"] = items.mar;
            jun_data["year_jun"] = items.years;
            
            jul_data["jul"] = items.jan;
            jul_data["year_jul"] = items.years;
            aug_data["aug"] = items.feb;
            aug_data["year_aug"] = items.years;
            sep_data["sep"] = items.mar;
            sep_data["year_sep"] = items.years;
            
            oct_data["oct"] = items.jan;
            oct_data["year_oct"] = items.years;
            nov_data["nov"] = items.feb;
            nov_data["year_nov"] = items.years;
            dec_data["dec"] = items.mar;
            dec_data["year_dec"] = items.years;
            
            win_data["win"] = items.jan;
            win_data["year_win"] = items.years;
            spr_data["spr"] = items.feb;
            spr_data["year_spr"] = items.years;
            sum_data["sum"] = items.mar;
            sum_data["year_sum"] = items.years;
            aut_data["aut"] = items.feb;
            aut_data["year_aut"] = items.years;
            ann_data["ann"] = items.mar;
            ann_data["year_ann"] = items.years;
            
            metoffice_json.update(jan_data)
            metoffice_json.update(feb_data)
            metoffice_json.update(mar_data)
            metoffice_json.update(apr_data)
            metoffice_json.update(may_data)
            metoffice_json.update(jun_data)
            metoffice_json.update(jul_data)
            metoffice_json.update(aug_data)
            metoffice_json.update(sep_data)
            metoffice_json.update(oct_data)
            metoffice_json.update(nov_data)
            metoffice_json.update(dec_data)
            
            metoffice_json.update(spr_data)
            metoffice_json.update(win_data)
            metoffice_json.update(aut_data)
            metoffice_json.update(ann_data)
            metoffice_json.update(sum_data)
            
            metoffice_data_list.append(metoffice_json)
        if search_criteria.type == "ranked":        
             metoffice_data_list = sorted(metoffice_data_list, key=lambda d: d['jan'], reverse=True)
        
        
        
        
    total_wetoffice = len(metoffice_list)
    last_page = True
    if total_wetoffice == limit:
        last_page = False
    
    return {
        "metoffice_list": metoffice_data_list, 
        "is_last_page": last_page
    }
    # return warehouse_list


def generate_metoffice_query_statement(
    search_criteria: request_model.SearchCriteriaMetoffice,
):
    query_statement = (
        select(db_model.Metofiice)
    )
    if search_criteria.region != None:
        query_statement = query_statement.where(
            db_model.Metofiice.region.ilike("%{}%".format(search_criteria.region))
        )
    if search_criteria.parameter != None:
        query_statement = query_statement.where(
            db_model.Metofiice.parameter == search_criteria.parameter
        )
    
    if search_criteria.is_active:
        if search_criteria.is_active.lower() == "false":
            setattr(search_criteria, "is_active", False)
        else:
            setattr(search_criteria, "is_active", True)
        query_statement = query_statement.filter(db_model.Metofiice.is_active == search_criteria.is_active)


    return query_statement



async def get_metoffice_by_api(
    session: AsyncSession,
    search_criteria: request_model.SearchCriteriaMetofficeByExistingAPI
):
    if search_criteria.type == "date":
        metoffice_list = await get_parameter_from_metoffice_by_date_api(search_criteria=search_criteria)
    else:
        metoffice_list = await get_parameter_from_metoffice_by_ranked_api(search_criteria=search_criteria)
    
    return {
        "metoffice_list": metoffice_list
    }


async def get_parameter_from_metoffice_by_ranked_api(search_criteria: request_model.SearchCriteriaMetofficeByExistingAPI):
    url = f"https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/{search_criteria.parameter}/{search_criteria.type}/{search_criteria.region}.txt"
    header = {"Content-Type": "application/json",}
    response = requests.get(url,header)
    response_data = response.text
    response_data = [item.split() for item in response_data.split('\n')[:-1]]

    response_data = [item for index,item in enumerate(response_data) if index > 4 ]
    datasets_list = []
    
    for item in  response_data:
        if item[0] != "jan":
            data = {}
            lenth = len(item)
        
            data['jan']=item[0] if lenth > 0 else "--"
            data['year_jan']=item[1] if lenth > 1 else "--"
            data['feb']=item[2] if lenth > 2 else "--"
            data['year_feb']=item[3] if lenth > 3 else "--"
            data['mar']=item[4] if lenth > 4 else "--"
            data['year_mar']=item[5] if lenth > 5 else "--"
            data['apr']= item[6] if lenth > 6 else "--"
            data['year_apr']=item[7] if lenth > 7 else "--"
            data['may']=item[8] if lenth > 8 else "--"
            data['year_may']=item[9] if lenth > 9 else "--"
            data['jun']=item[10] if lenth > 10 else "--"
            data['year_jun']=item[11] if lenth > 11 else "--"
            data['jul']=item[12] if lenth > 12 else "--"
            data['year_jul']=item[13] if lenth > 13 else "--"
            data['aug']=item[14] if lenth > 14 else "--"
            data['year_aug']=item[15] if lenth > 15 else "--"
            data['sep']=item[16] if lenth > 16 else "--"
            data['year_sep']=item[17] if lenth > 17 else "--"
            data['oct']=item[16] if lenth > 18 else "--"
            data['year_oct']=item[17] if lenth > 19 else "--"
            data['nov']=item[16] if lenth > 20 else "--"
            data['year_nov']=item[17] if lenth > 21 else "--"
            data['dec']=item[16] if lenth > 22 else "--"
            data['year_dec']=item[17] if lenth > 23 else "--"
            data['win']=item[16] if lenth > 24 else "--"
            data['year_win']=item[17] if lenth > 25 else "--"
            data['spr']=item[16] if lenth > 26 else "--"
            data['year_spr']=item[17] if lenth > 27 else "--"
            data['sum']=item[16] if lenth > 28 else "--"
            data['year_sum']=item[17] if lenth > 29 else "--"
            data['aut']=item[16] if lenth > 30 else "--"
            data['year_aut']=item[17] if lenth > 31 else "--"
            data['ann']=item[16] if lenth > 32 else "--"
            data['year_ann']=item[17] if lenth > 33 else "--"
            datasets_list.append(data)
    return datasets_list


async def get_parameter_from_metoffice_by_date_api(search_criteria: request_model.SearchCriteriaMetofficeByExistingAPI):
    
    url = f"https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/{search_criteria.parameter}/{search_criteria.type}/{search_criteria.region}.txt"
    header = {"Content-Type": "application/json",}
    response = requests.get(url,header)
    response_data = response.text
    response_data = [item.split() for item in response_data.split('\n')[:-1]]

    response_data = [item for index,item in enumerate(response_data) if index > 4 ]
    datasets_list = []
    
    for item in  response_data:
        if item[0] != "year":
            data = {}
            lenth = len(item)
            data['year']=item[0] if lenth > 0 else "--"
            data['jan']=item[1] if lenth > 1 else "--"
            data['feb']=item[2] if lenth > 2 else "--"
            data['mar']=item[3] if lenth > 3 else "--"
            data['apr']=item[4] if lenth > 4 else "--"
            data['may']=item[4] if lenth > 5 else "--"
            data['jun']= item[6] if lenth > 6 else "--"
            data['jul']=item[7] if lenth > 7 else "--"
            data['aug']=item[8] if lenth > 8 else "--"
            data['sep']=item[9] if lenth > 9 else "--"
            data['oct']=item[10] if lenth > 10 else "--"
            data['nov']=item[11] if lenth > 11 else "--"
            data['dec']=item[12] if lenth > 12 else "--"
            data['win']=item[13] if lenth > 13 else "--"
            data['spr']=item[14] if lenth > 14 else "--"
            data['sum']=item[15] if lenth > 15 else "--"
            data['aut']=item[16] if lenth > 16 else "--"
            data['ann']=item[17] if lenth > 17 else "--"
            datasets_list.append(data)
    return datasets_list


async def create_migration_metoffice(
    session: AsyncSession,
    search_criteria: request_model.SearchCriteriaMetofficeByExistingAPI
):
    
    url = f"https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/{search_criteria.parameter}/date/{search_criteria.region}.txt"
    header = {"Content-Type": "application/json",}
    response = requests.get(url,header)
    response_data = response.text
    response_data = [item.split() for item in response_data.split('\n')[:-1]]
    
    response_data = [item for index,item in enumerate(response_data) if index > 4 ]
    datasets_list = []
    for index in  range(len(response_data)):
        for item in  response_data:
            length = len(item)
            if item[0] != "year":
                metoffice_data:request_model.CreateMetoffice
                metoffice_data = request_model.CreateMetoffice(
                    years=item[0] if length > 0 else "---",
                    jan= item[1] if length > 1 else "---",
                    feb= item[2] if length > 2 else "---",
                    mar= item[3] if length > 3 else "---",
                    apr= item[4] if length > 4 else "---",
                    may= item[5] if length > 5 else "---",
                    jun= item[6] if length > 6 else "---",
                    jul= item[7] if length > 7 else "---",
                    aug= item[8] if length > 8 else "---",
                    sep= item[9] if length > 9 else "---",
                    oct= item[10] if length > 10 else "---",
                    nov= item[11] if length > 11 else "---",
                    dec= item[12] if length > 12 else "---",
                    win= item[13] if length > 13 else "---",
                    spr= item[14] if length > 14 else "---",
                    sum= item[15] if length > 15 else "---",
                    aut= item[16] if length > 16 else "---",
                    ann= item[17] if length > 17 else "---",
                    region=search_criteria.region,
                    parameter=search_criteria.parameter
                )
                db_new_metoffice = await metoffice_repository.create_metoffice(
                        session=session, metoffice_data=metoffice_data
                    )
                datasets_list.append(db_new_metoffice)
                
    return datasets_list
     