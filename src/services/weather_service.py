from repositories.location_repository import LocationRepository
import requests


class WeatherService:
    """Sovelluslogiikasta vastaava luokka säätietojen hakemiseen. Hoitaa säätietojen hakemisen OpenWeatherMap API:sta ja paikkatietojen hallinnan tietokannan kautta."""

    def __init__(self, location_repository=None):
        """"Alustaa WeatherService-olion. Luo uuden LocationRepositoryn jos sille ei anneta olemassa olevaa."""
        self._location_repository = location_repository or LocationRepository()
        self.api_key = "0ce853556e41395c0fedcaf6177166f9"

    def add_location(self, location):
        """Lisää uuden paikan tallennettavien paikkojen listaan."""
        return self._location_repository.create(location)

    def get_locations(self):
        """Hakee kaikki tallennetut paikat listana."""
        return self._location_repository.find_all()

    def remove_location(self, location):
        """Poistaa paikan tallennettujen paikkojen listasta."""
        return self._location_repository.delete(location)

    def get_weather(self, location):
        """Hakee nykyisen säätilan annetulle paikalle OpenWeatherMap API:sta."""
        url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={self.api_key}&units=metric"

        try:
            r = requests.get(url)
            d = r.json()
            return f"{d['name']}: {d['main']['temp']}°C, {d['weather'][0]['description']}"
        except:
            return "Virhe"

    def get_5day_forecast(self, location):
        """Hakee 5 päivän sääennusteen annetulle paikalle OpenWeatherMap API:sta."""
        url = f"https://api.openweathermap.org/data/2.5/forecast?q={location}&appid={self.api_key}&units=metric"

        try:
            r = requests.get(url)
            d = r.json()
            return [f"{item['dt_txt'][:10]}: {item['main']['temp']}°C, {item['weather'][0]['description']}"
                    for item in d['list'][:40:8]]
        except:
            return ["Virhe"]
