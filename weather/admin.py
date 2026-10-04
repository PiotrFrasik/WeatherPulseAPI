from django.contrib import admin
from .models import Station, WeatherMeasurement

@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'latitude', 'longitude')
    search_fields = ('name', 'code')

@admin.register(WeatherMeasurement)
class WeatherMeasurementAdmin(admin.ModelAdmin):
    list_display = ('station', 'air_temp', 'humidity', 'rainfall', 'wind_speed')
    list_filter = ('station', 'created_at')