import requests
from datetime import datetime
from django.core.management.base import BaseCommand
from django.utils.timezone import make_aware, now
from weather.models import Station, WeatherMeasurement

class Command(BaseCommand):
    help = "Download actual weather from meteo-IMGW"

    def create_station_object(self, station_data):
        """Create a new station object"""
        return Station.objects.create(name=station_data["nazwa_stacji"],
                                 code=station_data["kod_stacji"],
                                 latitude=station_data["lat"],
                                 longitude=station_data["lon"])

    def create_weather_measurement_object(self, station_data):
        """Create a new weather measurement object"""
        def datatime_converting(datatime_str):
            """Converting str to datetime"""
            if datatime_str is None:
                return None
            measurement_datetime_str = datatime_str
            # Time zone awareness
            return make_aware(datetime.strptime(measurement_datetime_str, "%Y-%m-%d %H:%M:%S"))

        def float_converting(data):
            """Converting str to float"""
            if data is None:
                return None
            return float(data)

        station = Station.objects.get(code=station_data["kod_stacji"])

        return WeatherMeasurement.objects.create(station=station,
                                                ground_temp = float_converting(station_data["temperatura_gruntu"]),
                                                ground_temp_date = datatime_converting(station_data["temperatura_gruntu_data"]),
                                                air_temp =  float_converting(station_data["temperatura_powietrza"]),
                                                air_temp_date = datatime_converting(station_data["temperatura_powietrza_data"]),
                                                wind_speed =  float_converting(station_data["wiatr_srednia_predkosc"]),
                                                humidity = float_converting(station_data["wilgotnosc_wzgledna"]),
                                                rainfall = float_converting(station_data["opad_10min"]))


    def handle(self, *args, **kwargs):
        # Download weather's data from IMGW
        link = "https://danepubliczne.imgw.pl/api/data/meteo/"
        data = requests.get(link)

        if data.status_code == 200:
            stations_data = data.json()
            existing_station_codes = set(Station.objects.values_list('code', flat=True))

            if isinstance(stations_data, list):
                # Check if station already exists
                for station_info in stations_data:
                    if station_info['kod_stacji'] not in existing_station_codes:
                        self.create_station_object(station_info)
                        # Update the set of existing station codes
                        existing_station_codes.add(station_info['kod_stacji'])

                    # Create weather measurement object
                    self.create_weather_measurement_object(station_info)







