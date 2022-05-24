import requests
import xmltodict
from datetime import datetime


def get_currency_rub():
    date_now = "/".join(str(datetime.now().date()).split("-")[::-1])
    r = requests.get(
        f'https://www.cbr.ru/scripts/XML_dynamic.asp?date_req1={date_now}&date_req2={date_now}&VAL_NM_RQ=R01235')
    data = xmltodict.parse(r.content)
    return float(data['ValCurs']['Record']['Value'].replace(',', '.'))


print(get_currency_rub())
