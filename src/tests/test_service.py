import unittest
from services.weather_service import WeatherService
from repositories.location_repository import LocationRepository


class TestWeatherService(unittest.TestCase):
    def setUp(self):
        self.location_repository = LocationRepository()
        self.location_repository.delete_all()
        self.service = WeatherService(self.location_repository)

    def test_add_location(self):
        result = self.service.add_location("Helsinki")
        self.assertTrue(result)
        self.assertIn("Helsinki", self.service.get_locations())

    def test_add_duplicate_location(self):
        self.service.add_location("Tokyo")
        result = self.service.add_location("Tokyo")
        self.assertFalse(result)

    def test_remove_location(self):
        self.service.add_location("Berlin")
        result = self.service.remove_location("Berlin")
        self.assertTrue(result)
        self.assertNotIn("Berlin", self.service.get_locations())

    def test_get_weather(self):
        weather = self.service.get_weather("Test")
        self.assertEqual(weather, "Test: 20°C, Aurinkoista")

    def test_get_forecast_with_invalid_days(self):
        forecasts = self.service.get_forecast("Test", -1)
        self.assertEqual(len(forecasts), 0)
