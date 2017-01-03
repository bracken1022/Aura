

from mock import patch
from django.test import TestCase
from rest_framework import status

from pm25.models.air_quality import AirQuality
from pm25.service.sync_data import sync_and_save_pm_data
from pm25.test.config import BACKEND_URL

ENDPOINT_URL = BACKEND_URL + 'dataShow'


class Pm25DataTest(TestCase):

    def test_should_return_404_with_wrong_api(self):
        response = self.client.get('%s?sta=2011' % 'app/dataShow')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_should_return_400_with_bad_request(self):
        response = self.client.get('%s?city=xian&startDate=30' % ENDPOINT_URL)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_should_return_200_with_successful_request(self):
        response = self.client.get('%s?city=xian&startDate=20160901&endDate=201609011' % ENDPOINT_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @patch('pm25.service.sync_data.request_aqi_cn_for_pm_data')
    def test_should_return_serializer_data(self, mock_request_aqi_cn_for_pm_data):
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
            "name": "Xian",
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

        expected_json = [{'city_aqi': 71, 'local_time': '2016-12-10 19:00:00', 'pm_25': 71, 'city_idx': 7397, 'city_name': 'Xian', 'url': 'https://aqicn.org/city/usa/illinois/chi_sp/', 'geo_x': '41.913600', 'geo_y': '-87.723900', 'time_zone': '-06:00', 'id': 1}]

        mock_request_aqi_cn_for_pm_data.return_value = mock_json_data

        sync_and_save_pm_data('Xian', 'demo')

        response = self.client.get('%s?city=xian&startDate=20160901&endDate=201609011' % ENDPOINT_URL)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), expected_json)



