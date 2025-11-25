import unittest
from repositories.location_repository import LocationRepository


class TestLocationRepository(unittest.TestCase):
    def setUp(self):
        self.repository = LocationRepository()
        self.repository.delete_all()

    def test_create_location(self):
        result = self.repository.create("Helsinki")
        self.assertTrue(result)
        locations = self.repository.find_all()
        self.assertIn("Helsinki", locations)

    def test_create_duplicate_location(self):
        self.repository.create("Tokyo")
        result = self.repository.create("Tokyo")
        self.assertFalse(result)

    def test_delete_location(self):
        self.repository.create("Berlin")
        result = self.repository.delete("Berlin")
        self.assertTrue(result)
        locations = self.repository.find_all()
        self.assertNotIn("Berlin", locations)

    def test_find_all_locations(self):
        self.repository.create("Paris")
        self.repository.create("London")
        locations = self.repository.find_all()
        self.assertEqual(len(locations), 2)
        self.assertIn("Paris", locations)
        self.assertIn("London", locations)
