from django.db.models import Min, Avg, Max
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import WeatherMeasurement, Station
from .serializers import StationSerializer, WeatherMeasurementSerializer

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
            highest_ground_temp_temp=Max('ground_temp'),
            lowest_ground_temp_temp=Min('ground_temp'),
            average_ground_temp_temp=Avg('ground_temp'),
            # Humidity
            srednia_wilgotnosc=Avg('humidity')
        )

        return Response(stats)