import json
from mock import patch, MagicMock, Mock

from django.test import TestCase
from rest_framework import status

from pm25.service.sync_data import format_aqi_cn_request
from pm25.service.sync_data import request_aqi_cn_for_pm_data
from pm25.service.sync_data import sync_and_save_pm_data
from pm25.service.sync_data import request_aqi_cn_for_pm_data

from pm25.models.air_quality import AirQuality

from pm25.test.factories.air_quality_factory import AirQualityFactory

class SyncDataFromAqiCnTest(TestCase):

    def test_sync_data_response_200_ok(self):
        self.assertEqual(200, status.HTTP_200_OK)

    def test_format_aqi_cn_request(self):
        expected = 'https://api.waqi.info/feed/xian/'
        actual = format_aqi_cn_request('xian')

        self.assertEqual(actual, expected)


    @patch('pm25.service.sync_data.request_aqi_cn_for_pm_data')
    def test_after_sync_data_should_be_saved(self, mock_request_aqi_cn_for_pm_data):
        mock_json_data = ({
  "status": "ok",
  "data": {
        "idx":7397,
        "aqi":71,
        "time":{
            "v":1481396400,
            "s":"2016-12-10 19:00:00",
            "tz":"-06:00"
        },
        "city":{
            "name":"Chi_sp, Illinois",
            "url":"https://aqicn.org/city/usa/illinois/chi_sp/",
            "geo":["41.913600","-87.723900"]
        },
        "iaqi":{
            "pm25":{
                "v":71
            }
          }
         }
        })
        mock_request_aqi_cn_for_pm_data.return_value = mock_json_data

        sync_and_save_pm_data('xian', 'demo')
        air_quality = AirQuality.objects.first()

        self.assertEqual('Chi_sp, Illinois', air_quality.city_name)
        self.assertEqual('41.913600', air_quality.geo_x)
        self.assertEqual(71, air_quality.pm_25)
        self.assertEqual('-06:00', air_quality.time_zone)



