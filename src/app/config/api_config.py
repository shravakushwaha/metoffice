from pydantic import BaseSettings


class ApiConfig(BaseSettings):
    _surepassBaseUrl = ""
    _surepassAuthorizationToken = ""
    surepass_headers = {"Authorization": _surepassAuthorizationToken}
    
apiConfig = ApiConfig()
