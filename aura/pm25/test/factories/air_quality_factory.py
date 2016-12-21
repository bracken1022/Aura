

import factory

from pm25.models.air_quality import AirQuality


class AirQualityFactory(factory.DjangoModelFactory):
    class Meta:
        model = AirQuality

    city_idx = 100
    city_name = 'xian'
    city_aqi = 177
    local_time = '20160901'
    time_zone = 'zh'
    geo_x = '111.111'
    geo_y = '222.222'
    url = 'aqicn.org'
    pm_25 = 501

