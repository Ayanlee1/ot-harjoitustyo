import time


class UI:
    """Tekstipohjainen käyttöliittymä säätietosovellukselle."""

    def __init__(self, weather_service):
        """Alustaa käyttöliittymän. Tarvitsee WeatherService-olion toiminnalle."""
        self.service = weather_service

    def run(self):
        """Käynnistää käyttöliittymän pääsilmukan. Näyttää valikon ja käsittelee käyttäjän valintoja kunnes käyttäjä lopettaa."""
        while True:
            print("\n=== SÄÄSOVELLUS ===")
            print("1. Lisää paikka")
            print("2. Näytä paikat")
            print("3. Poista paikka")
            print("4. Hae sää")
            print("5. Hae 5 päivän ennuste")
            print("0. Lopeta")

            choice = input("Valinta: ")

            if choice == "0":
                print("Hei hei!")
                break
            elif choice == "1":
                self._add_location()
            elif choice == "2":
                self._show_locations()
            elif choice == "3":
                self._remove_location()
            elif choice == "4":
                self._get_weather()
            elif choice == "5":
                self._get_forecast()
            else:
                print("Virheellinen valinta")

    def _add_location(self):
        """Pyytää käyttäjältä paikan nimen ja lisää sen tallennettavien paikkojen listaan."""
        location = input("Anna paikan nimi: ")
        success = self.service.add_location(location)
        if success:
            print(f"Paikka '{location}' lisätty.")
        else:
            print(f"Paikka '{location}' on jo listalla.")

    def _show_locations(self):
        """Näyttää kaikki tallennetut paikat listana."""
        locations = self.service.get_locations()
        if locations:
            print("Tallennetut paikat:")
            for location in locations:
                print(f"- {location}")
        else:
            print("Ei tallennettuja paikkoja.")

    def _remove_location(self):
        """Pyytää käyttäjältä poistettavan paikan nimen ja poistaa sen listalta."""
        location = input("Poistettava paikka: ")
        success = self.service.remove_location(location)
        if success:
            print(f"Paikka '{location}' poistettu.")
        else:
            print(f"Paikkaa '{location}' ei löytynyt.")

    def _get_weather(self):
        """Pyytää paikan nimen ja näyttää sen nykyisen säätilan."""
        location = input("Paikka: ")

        print("Haetaan säätietoja", end="", flush=True)

        for _ in range(3):
            time.sleep(0.5)
            print(".", end="", flush=True)

        print()

        weather = self.service.get_weather(location)
        print(weather)

    def _get_forecast(self):
        """Pyytää paikan nimen ja näyttää sen 5 päivän sääennusteen."""
        location = input("Paikka: ")

        print("Haetaan ennustetta", end="", flush=True)

        for _ in range(3):
            time.sleep(0.3)
            print(".", end="", flush=True)
        print()

        forecasts = self.service.get_5day_forecast(location)

        if isinstance(forecasts, list) and len(forecasts) > 0:
            if forecasts[0] == "Virhe":
                print("Virhe ennustetta haettaessa.")

            else:
                print(f"\n5 päivän ennuste {location}:lle:")
                for forecast in forecasts:
                    print(f"  {forecast}")

        else:
            print("Virhe ennustetta haettaessa.")
