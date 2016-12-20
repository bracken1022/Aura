
from django.conf.urls import url

from pm25.api.pm_data_show import data_show


urlpatterns = [
    url(r'^api/dataShow', data_show, name='dataShow'),
]
