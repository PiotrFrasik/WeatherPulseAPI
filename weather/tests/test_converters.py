from django.test import TestCase
from weather.models import Station, WeatherMeasurement
from weather.management.commands.fetch_weather import Command

class WeatherConvertersTestCase(TestCase):
    def setUp(self):
        self.command = Command()

        self.station = Station.objects.create(
            name="Test Station",
            code="123456",
            latitude=52.23,
            longitude=21.01
        )

    def test_float_converting_valid(self):
        """Test that valid string representations of weather metrics are correctly converted to float."""
        station_data ={
            "kod_stacji": "123456",
            "temperatura_gruntu": "10.5",
            "temperatura_gruntu_data": "2026-06-18 12:00:00",
            "temperatura_powietrza": "15.4",
            "temperatura_powietrza_data": "2026-06-18 12:00:00",
            "wiatr_srednia_predkosc": "3.2",
            "wilgotnosc_wzgledna": "65.0",
            "opad_10min": "0.0"
        }

        self.command.create_weather_measurement_object(station_data)
        measurement = WeatherMeasurement.objects.get(station=self.station)
        self.assertEqual(measurement.ground_temp, 10.5)
        self.assertEqual(measurement.air_temp, 15.4)
        self.assertEqual(measurement.wind_speed, 3.2)
        self.assertEqual(measurement.humidity, 65.0)
        self.assertEqual(measurement.rainfall, 0.0)

    def test_float_converting_none_and_invalid(self):
        """Checking station with wrong data"""

        bad_station_data = {
            "kod_stacji": "123456",
            "temperatura_gruntu": None,
            "temperatura_gruntu_data": "2026-06-18 12:00:00",
            "temperatura_powietrza": "błąd_imgw",  # Checking ValueError
            "temperatura_powietrza_data": "2026-06-18 12:00:00",
            "wiatr_srednia_predkosc": None,
            "wilgotnosc_wzgledna": "65.0",
            "opad_10min": "0.0"
        }

        self.command.create_weather_measurement_object(bad_station_data)
        measurement = WeatherMeasurement.objects.get(station=self.station)

        self.assertIsNone(measurement.ground_temp)  # We expect None for uploaded None
        self.assertIsNone(measurement.air_temp)  # We expect None for the text "bląd_imgw"
        # We check if the correct field is still saved without any problem
        self.assertEqual(measurement.humidity, 65.0)