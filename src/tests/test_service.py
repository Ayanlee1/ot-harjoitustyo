import unittest
from weather.service import WeatherService

class TestWeatherService(unittest.TestCase):
    
    def setUp(self):
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