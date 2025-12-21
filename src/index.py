import tkinter as tk
from database_connection import get_database_connection
from repositories.location_repository import LocationRepository
from services.weather_service import WeatherService
from ui.ui import UI


def main():
    """Sovelluksen pääfunktio."""
    connection = get_database_connection()
    location_repository = LocationRepository(connection)
    weather_service = WeatherService(location_repository)

    window = tk.Tk()
    window.title("Sääsovellus")
    window.geometry("900x700")

    ui = UI(window, weather_service)
    ui.start()

    window.mainloop()


if __name__ == "__main__":
    main()
