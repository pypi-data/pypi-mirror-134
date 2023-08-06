from typing import Optional, Union
from zeep import Client
import urllib


def generate_api_key(
    wsdl: str = "https://webservice.tecalliance.services/webcat30/v1/services/WebCat30WS.soapEndpoint?wsdl",
    catalog: str = "",
    username: str = "",
    password: str = "",
    default_ttl: Optional[int] = 31536000,
) -> Union[str, None]:
    tecrmiSOAPClient = Client(wsdl)
    # Has to remove strict mode, the TecRMI response is not correct according to its own WSDL
    with tecrmiSOAPClient.settings(strict=False):
        result = tecrmiSOAPClient.service.getAPIKeyForUser(
            catalog=catalog,
            username=username,
            password=password,
            ttlSeconds=default_ttl,
        )
        return result and result.apiKey or None


def gen_deep_link(
    url: Optional[str] = "https://web.tecalliance.net",
    lang: Optional[str] = "fr",
    api_key: str = "",
    module: str = "rmi",
    vehicle_type: str = "cars",
    display: str = "modules",
    catalog: str = "",
    siv: Optional[str] = None,
    vin: Optional[str] = None,
    type_id: Optional[str] = None,
) -> Union[str, None]:
    if not api_key:
        return None
    target_url = f"{url}/{catalog}/{lang}/{module}"

    if module != "home" and vehicle_type:
        target_url += f"/{vehicle_type}"
        if type_id:
            if vehicle_type == "trucks":
                target_url += f"/100{type_id}/{type_id}"
            else:
                target_url += f"/{type_id}/{type_id}"
            if display:
                target_url += f"/{display}"
    params = {"apikey": api_key}
    if siv:
        params.update(
            {
                "searchType": "plate",
                "searchValue": siv,
                "searchValueType": "5",
            }
        )
    if vin and vin != "":
        params.update(
            {
                "searchType": "vin",
                "searchValue": vin,
                "searchValueType": "5",
            }
        )
    if params:
        target_url += "?" + urllib.parse.urlencode(params)
    return target_url
