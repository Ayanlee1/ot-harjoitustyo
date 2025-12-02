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

    def get_forecast(self, location, days=5):
        forecasts = []
        for i in range(1, days+1):
            if i == 1:
                forecasts.append("Huomenna: 18°C, Puolipilvistä")
            elif i == 2:
                forecasts.append("Ylihuomenna: 16°C, Sateista")
            elif i == 3:
                forecasts.append("3 päivän päästä: 17°C, Aurinkosta")
            elif i == 4:
                forecasts.append("4 päivän päästä: 15°C, Pilvistä")
            else:
                forecasts.append("5 päivän päästä: 19°C, Aurinkoista")
        return forecasts
