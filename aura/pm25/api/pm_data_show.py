

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status

from pm25.exceptions.illegal_parameters_exception import PmDataShowIllegalParameterException
from pm25.service.pm_data_service import check_params, JSONResponse
from pm25.models.air_quality import AirQuality
from pm25.serializers.pm_data_serializer import AirQualitySerializer


@csrf_exempt
@api_view(['GET', ])
@renderer_classes((JSONRenderer, ))
def data_show(request):
    try:
        if request.method == 'GET':
            city, start_date, end_date = check_params(request.GET)
#            air_qualities = AirQuality.objects.filter(city_name=city)
            air_qualities = AirQuality.objects.all()
            air_quality_serializer = AirQualitySerializer(air_qualities, many=True)

            return JSONResponse(air_quality_serializer.data, status=status.HTTP_200_OK)

    except PmDataShowIllegalParameterException as e:
        return Response(e.error_message, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response('Error: %s' % e, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
