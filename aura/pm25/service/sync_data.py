
import requests

from rest_framework import status

from pm25.models.air_quality import AirQuality


API_TOKEN = '158d6f398e60645291520da6cbb4db3bac25e27e'

PM25_URL = 'https://api.waqi.info/feed/%s/?token=%s'


def format_aqi_cn_request(city, token):
    return PM25_URL % (city, token)


def request_aqi_cn_for_pm_data(city, token):
    response = requests.get(PM25_URL % (city, token))
    if response.status_code == status.HTTP_200_OK:
        return response.json()

    return {'status': 'error'}


def save_pm_data_to_local(pm_data):
    pass


def validate_json_data(json_data):
    validated_data = {}

    validated_data['city_idx'] = json_data.get('idx')
    validated_data['city_name'] = json_data.get('city').get('name')
    validated_data['city_aqi'] = json_data.get('aqi')
    validated_data['local_time'] = json_data.get('time').get('s')
    validated_data['time_zone'] = json_data.get('time').get('tz')
    validated_data['geo_x'] = json_data.get('city').get('geo')[0]
    validated_data['geo_y'] = json_data.get('city').get('geo')[1]
    validated_data['url'] = json_data.get('city').get('url')
    validated_data['pm_25'] = json_data.get('iaqi').get('pm25').get('v')

    return validated_data


def sync_and_save_pm_data(city, token):
    json_data = request_aqi_cn_for_pm_data(city, token)

    if json_data['status'] == 'error':
        return

    validated_data = validate_json_data(json_data['data'])

    air_quality = AirQuality(city_idx=validated_data.get('city_idx'),
                             city_name=validated_data.get('city_name'),
                             city_aqi=validated_data.get('city_aqi'),
                             local_time=validated_data.get('local_time'),
                             time_zone=validated_data.get('time_zone'),
                             geo_x=validated_data.get('geo_x'),
                             geo_y=validated_data.get('geo_y'),
                             url=validated_data.get('url'),
                             pm_25=validated_data.get('pm_25')
    )

    air_quality.save()

