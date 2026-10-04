from django.urls import path
from .views import (StationListView, WeatherMeasurementListView,
                    WeatherStatsView)
urlpatterns = [
    path('', WeatherMeasurementListView.as_view(), name='weather_measurement_list'),
    path('stations/', StationListView.as_view(), name='station_list'),
    path('stats/', WeatherStatsView.as_view(), name='weather_stats'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

]