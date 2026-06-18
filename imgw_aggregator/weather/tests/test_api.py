from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from weather.models import Station


class WeatherAPITestCase(APITestCase):
    def setUp(self):
        self.station1 = Station.objects.create(
            name="WARSZAWA", code="125", latitude=52.23, longitude=21.01
        )
        self.station2 = Station.objects.create(
            name="WŁODAWA", code="345", latitude=51.55, longitude=23.52
        )

        self.stations_url = reverse('station_list')

    def test_get_stations_list_success(self):
        """Test retrieving the list of all weather stations successfully."""
        # Test request
        response = self.client.get(self.stations_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if returned two stations
        self.assertEqual(len(response.data), 2)

        # Checking if data is correct
        self.assertEqual(response.data[0]['name'], "WARSZAWA")
        self.assertEqual(response.data[1]['name'], "WŁODAWA")

    def test_station_search_filter(self):
        """Test filtering the list of weather stations by name using the 'search' query parameter."""
        # send a GET query with the search parameter ?search=WŁODAWA
        response = self.client.get(self.stations_url, {'search': 'WŁODAWA'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # The filter should cut off Warsaw and return ONLY 1 station (Włodawa)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "WŁODAWA")