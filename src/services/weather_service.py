from repositories.location_repository import LocationRepository


class WeatherService:
    def __init__(self, location_repository=None):
        self._location_repository = location_repository or LocationRepository()

    def add_location(self, location):
        return self._location_repository.create(location)

    def get_locations(self):
        return self._location_repository.find_all()

    def remove_location(self, location):
        return self._location_repository.delete(location)

    def get_weather(self, location):
        return f"{location}: 20°C, Aurinkoista"
