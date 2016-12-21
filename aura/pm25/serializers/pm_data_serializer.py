

from rest_framework import serializers

from pm25.models.air_quality import AirQuality


class AirQualitySerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    city_idx = serializers.IntegerField()
    city_name = serializers.CharField(allow_blank=True, max_length=100)
    city_aqi = serializers.IntegerField()
    local_time = serializers.CharField(max_length=50)
    time_zone = serializers.CharField(max_length=50)
    geo_x = serializers.CharField(max_length=50)
    geo_y = serializers.CharField(max_length=50)
    url = serializers.CharField(max_length=100)
    pm_25 = serializers.IntegerField()

    def create(self, validated_data):
        return AirQuality.objects.create(**validated_data)
