from rest_framework import generics, filters
from .models import WeatherMeasurement, Station
from .serializers import StationSerializer, WeatherMeasurementSerializer


class StationListView(generics.ListAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name']
    search_fields = ['name']

class WeatherMeasurementListView(generics.ListAPIView):
    queryset = WeatherMeasurement.objects.all()
    serializer_class = WeatherMeasurementSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields  = ['station__name']
    ordering_fields = ['station__name', 'created_at']
    ordering = ['-created_at'] # Default sorting