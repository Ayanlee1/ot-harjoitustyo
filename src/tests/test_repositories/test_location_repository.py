import unittest
from services.weather_service import WeatherService
from initialize_database import initialize_database


class TestWeatherService(unittest.TestCase):
    def setUp(self):
        initialize_database()
        self.service = WeatherService()

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

    def test_get_weather_without_api_key(self):
        service = WeatherService()
        service.api_key = ""
        weather = service.get_weather("Helsinki")
        self.assertEqual(weather, "Virhe")

    def test_get_5day_forecast_without_api_key(self):
        service = WeatherService()
        service.api_key = ""
        forecasts = service.get_5day_forecast("Helsinki")
        self.assertEqual(forecasts, ["Virhe"])
