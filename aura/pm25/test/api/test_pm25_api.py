


from django.test import TestCase
from rest_framework import status

from pm25.test.config import BACKEND_URL

ENDPOINT_URL = BACKEND_URL + 'dataShow'

class Pm25DataTest(TestCase):

    def test_should_return_404_with_wrong_api(self):
        response = self.client.get('%s?sta=2011' % 'app/dataShow')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_should_return_400_with_bad_request(self):
        response = self.client.get('%s?start=30' % ENDPOINT_URL)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
