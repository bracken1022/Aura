
import requests

from rest_framework import status

from pm25.models.air_quality import AirQuality


API_TOKEN = '158d6f398e60645291520da6cbb4db3bac25e27e'

PM25_URL = 'https://api.waqi.info/feed/%s/'
UA_BROWSER = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36'


def format_aqi_cn_request(city):
    return PM25_URL % (city)


def request_aqi_cn_for_pm_data(city, token):
    parameter = {'token': token}
    headers = {'user-agent': UA_BROWSER}
    response = requests.get(format_aqi_cn_request(city), params=parameter, headers=headers)

    if response.status_code == status.HTTP_200_OK:
        return response.json()

    return {'status': 'error'}


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


def data_exist(validated_data):
    local_time = validated_data.get('local_time')
    city_name = validated_data.get('city_name')

    air_quality = AirQuality.objects.filter(local_time=local_time, city_name=city_name)

    if not air_quality:
        return False

    return True


def sync_and_save_pm_data(city, token):
    json_data = request_aqi_cn_for_pm_data(city, token)

    if json_data['status'] == 'error':
        return

    validated_data = validate_json_data(json_data['data'])

    if data_exist(validated_data):
        return

    try:
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
    except Exception as e:
        print('exception happens: %s ' % e)


CITYS = ['xian', 'baoji', 'shanghai', 'beijing', 'tianjin',
 'wuhan', 'nanjing']


def sync_pm25_data_from_usa_embassy():
    for city in CITYS:
        sync_and_save_pm_data(city, API_TOKEN)
