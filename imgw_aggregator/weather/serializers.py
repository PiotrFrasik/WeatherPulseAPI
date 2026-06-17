from rest_framework import serializers
from .models import Station, WeatherMeasurement

class StationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Station
        fields = '__all__'

class WeatherMeasurementSerializer(serializers.ModelSerializer):
    station = serializers.CharField(source='station.name', read_only=True)
    class Meta:
        model = WeatherMeasurement
        fields = '__all__'
