from pydantic import BaseSettings


class ApiConfig(BaseSettings):
    _surepassBaseUrl = ""
    _surepassAuthorizationToken = ""
    surepass_headers = {"Authorization": _surepassAuthorizationToken}
    cinUrl: str = _surepassBaseUrl + "/corporate/cin"
    panUrl: str = _surepassBaseUrl + "/pan/pan"
    aadhaarOTPUrl: str = _surepassBaseUrl + "/aadhaar-v2/generate-otp"
    aadhaarSubmitOTPUrl: str = _surepassBaseUrl + "/aadhaar-v2/submit-otp"

    erpNextUrl = "https://faarmslane.erpnext.com/"
    erpNextApiKey = "d93ff4cccc2281b"
    erpNextApiSecret = "6012aa2f94a1d80"
    magentoBearerToken = "ah1sfe4nyghd6ri5tgn364bkealy3n9u"
    magentoOrderAPI = "https://faarms.com/rest/V1/orders?"
    alternateNumberAPI = "https://faarms.com/rest/V1/get-order-alternate-number/"
    employeeCodeAPI = "https://faarms.com/rest/V1/referencecode?orderId="
    foCodeAPI = "https://faarms.com/rest/V1/focode/"
    sendgridApiKey = "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"
    uengage_api_base_url = "https://www.uengage.in/ueapi/sendTemplate?longSms=1&usr=7534&pwd=faarms@123&mobileNo="
    uengage_api_faarms_red = "&senderId=faarms&templateId=1970&param="
    uengage_api_end = "::ten::::Ag2YUu158lX15l2Q4AZspa"

apiConfig = ApiConfig()
