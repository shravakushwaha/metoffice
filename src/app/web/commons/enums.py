from enum import Enum
    
class LoggerAttributesEnum(str, Enum):
    port = "port"
    url = "url"
    method = "method"
    file_name = "file_name"
    function_name = "function_name"
    attributes = "attributes"
    message = "message"
    stack_trace = "stack_trace"

    ## method options
    method_get = "GET"
    method_get_by_id = "GET_BY_ID"
    method_post = "POST"
    method_put = "PUT"

class RegionTypeEnum(str, Enum):
    UK = "UK"
    England = "England"
    Wales = "Wales"
    Scotland = "Scotland"
    Northern_Ireland = "Northern Ireland"
    England_and_Wales = "England & Wales"
    England_N = "England N"
    England_S = "England S"
    Scotland_N = "Scotland N"
    Scotland_E = "Scotland E"
    Scotland_W = "Scotland W"
    England_E_and_NE = "England E & NE"
    England_NW_and_N_Wales = "England NW/Wales N"
    Midlands = "Midlands"
    East_Anglia = "East Anglia"
    England_SW_and_S_Wales = "England SW/Wales S"
    England_SE_and_Central_S = "England SE/Central S"
    
class ParameterTypeEnum(str, Enum):
    Tmax = "Max temp"
    Tmin = "Min temp"
    Tmean = "Mean temp"
    Sunshine = "Sunshine"
    Rainfall = "Rainfall"
    Raindays1mm = "Rain days ≥1.0mm"
    AirFrost = "Days of air frost"