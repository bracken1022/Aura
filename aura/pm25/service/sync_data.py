
import requests

from rest_framework import status


API_TOKEN = '158d6f398e60645291520da6cbb4db3bac25e27e'

PM25_URL = 'https://api.waqi.info/feed/%s/?token=%s'


def format_aqi_cn_request(city, token):
    return PM25_URL % (city, token)


def request_aqi_cn_for_pm_data(city, token):
    response = requests.get(PM25_URL % (city, token))
    if response.status_code == status.HTTP_200_OK:
        return response.json()

    return {'status': response.status_code}


def save_pm_data_to_local(pm_data):
    pass
