import os
from dotenv import load_dotenv
import requests
from repositories.location_repository import LocationRepository


load_dotenv()


class WeatherService:
    """Sovelluslogiikasta vastaava luokka säätietojen hakemiseen.
    Hoitaa säätietojen hakemisen OpenWeatherMap API:sta ja
    paikkatietojen hallinnan tietokannan kautta."""

    def __init__(self, location_repository=None):
        """Alustaa WeatherService-olion."""
        self._location_repository = location_repository or LocationRepository()
        self.api_key = os.getenv("OPENWEATHER_API_KEY")

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
        """Hakee nykyisen säätilan annetulle paikalle."""

        if not self.api_key or self.api_key.strip() == "":
            return "Virhe"

        url = "https://api.openweathermap.org/data/2.5/weather"
        params = f"?q={location}&appid={self.api_key}&units=metric"

        try:
            r = requests.get(url + params, timeout=10)
            d = r.json()

            if 'cod' in d and d['cod'] != 200:
                return "Virhe"

            return f"{d['name']}: {d['main']['temp']}°C, {d['weather'][0]['description']}"
        except:
            return "Virhe"

    def get_5day_forecast(self, location):
        """Hakee 5 päivän sääennusteen annetulle paikalle."""
        if not self.api_key or self.api_key.strip() == "":
            return ["Virhe"]

        url = "https://api.openweathermap.org/data/2.5/forecast"
        params = f"?q={location}&appid={self.api_key}&units=metric"

        try:
            r = requests.get(url + params, timeout=10)
            d = r.json()

            if 'cod' in d and d['cod'] != '200':
                return ["Virhe"]

            return [f"{item['dt_txt'][:10]}: {item['main']['temp']}°C, "
                    f"{item['weather'][0]['description']}"
                    for item in d['list'][:40:8]]

        except:
            return ["Virhe"]
