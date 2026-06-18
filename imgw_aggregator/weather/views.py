from django.db.models import Min, Avg, Max
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import WeatherMeasurement, Station
from .serializers import StationSerializer, WeatherMeasurementSerializer
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_entry_point(request, format=None):
    """
    Main entry point for the REST API.
    """
    return Response({
        'Project description': 'API that aggregates meteorological data from IMGW in real time.',
        'Weather easurement': reverse('weather_measurement_list', request=request, format=format),
        'Weather stations': reverse('station_list', request=request, format=format),
        'Weather stats': reverse('weather_stats', request=request, format=format),
        'Swagger Docs': reverse('swagger-ui', request=request, format=format),
        'Swagger JSON': reverse('schema', request=request, format=format),
    })

class StationListView(ListAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['name']
    search_fields = ['name']

class WeatherMeasurementListView(ListAPIView):
    queryset = WeatherMeasurement.objects.all()
    serializer_class = WeatherMeasurementSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    search_fields  = ['station__name']
    ordering_fields = ['station__name', 'created_at']
    ordering = ['-created_at'] # Default sorting

class WeatherStatsView(APIView):
    def get(self, request, *args, **kwargs):
        stats = WeatherMeasurement.objects.aggregate(
            # Air temp
            highest_air_temp=Max('air_temp'),
            lowest_air_temp=Min('air_temp'),
            average_air_temp=Avg('air_temp'),
            # Ground temp
            highest_ground_temp=Max('ground_temp'),
            lowest_ground_temp=Min('ground_temp'),
            average_ground_temp=Avg('ground_temp'),
            # Humidity
            srednia_wilgotnosc=Avg('humidity')
        )

        return Response(stats)