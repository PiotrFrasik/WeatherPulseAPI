from django.urls import path
from .views import (StationListView, WeatherMeasurementListView,
                    WeatherStatsView)
urlpatterns = [
    path('', WeatherMeasurementListView.as_view(), name='weather_measurement_list'),
    path('stations/', StationListView.as_view(), name='station_list'),
    path('stats/', WeatherStatsView.as_view(), name='weather_stats'),
]