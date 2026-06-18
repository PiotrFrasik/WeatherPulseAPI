from django.urls import path
from .views import (StationListView, WeatherMeasurementListView,
                    WeatherStatsView, api_entry_point)

urlpatterns = [
    path('', api_entry_point, name='api-root'),
    path('weather', WeatherMeasurementListView.as_view(), name='weather_measurement_list'),
    path('weather/stations/', StationListView.as_view(), name='station_list'),
    path('weather/stats/', WeatherStatsView.as_view(), name='weather_stats')
]