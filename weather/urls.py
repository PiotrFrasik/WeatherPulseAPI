from django.urls import path
from .views import (StationListView, WeatherMeasurementListView,
                    WeatherStatsView, api_entry_point)
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('', api_entry_point, name='api-root'),
    path('weather', WeatherMeasurementListView.as_view(), name='weather_measurement_list'),
    path('weather/stations/', StationListView.as_view(), name='station_list'),
    path('weather/stats/', WeatherStatsView.as_view(), name='weather_stats'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

]