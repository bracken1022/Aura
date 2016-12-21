from django.db import models


class AirQuality(models.Model):

    class Meta:
        app_label = 'pm25'

    created = models.DateTimeField(auto_now_add=True)
    city_idx = models.IntegerField()
    city_name = models.CharField(max_length=100, blank=True, default='')
    city_aqi = models.IntegerField(default=0)
    local_time = models.CharField(max_length=50, blank=True, default='')
    time_zone = models.CharField(max_length=50, blank=True, default='')
    geo_x = models.CharField(max_length=50, blank=True, default='')
    geo_y = models.CharField(max_length=50, blank=True, default='')
    url = models.CharField(max_length=100, blank=True, default='')
    pm_25 = models.IntegerField()



