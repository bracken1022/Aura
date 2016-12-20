import json
from mock import patch, MagicMock

from django.test import TestCase
from rest_framework import status

from pm25.service.sync_data import format_aqi_cn_request
from pm25.service.sync_data import request_aqi_cn_for_pm_data

class SyncDataFromAqiCnTest(TestCase):

    def test_sync_data_response_200_ok(self):
        self.assertEqual(200, status.HTTP_200_OK)

    def test_format_aqi_cn_request(self):
        expected = 'https://api.waqi.info/feed/xian/?token=demo'
        actual = format_aqi_cn_request('xian', 'demo')

        self.assertEqual(actual, expected)





