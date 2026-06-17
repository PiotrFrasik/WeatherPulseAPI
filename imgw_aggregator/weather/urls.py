from django.urls import path

from .views import StationListView, WeatherMeasurementListView

urlpatterns = [
    path('stations/', StationListView.as_view(), name='station_list'),
    path('weather_measurement/', WeatherMeasurementListView.as_view(), name='weather_measurement_list'),
]