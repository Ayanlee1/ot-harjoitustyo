from database_connection import get_database_connection
from repositories.location_repository import LocationRepository
from services.weather_service import WeatherService
from ui import UI


def main():
    connection = get_database_connection()
    location_repository = LocationRepository(connection)
    weather_service = WeatherService(location_repository)

    ui = UI(weather_service)
    ui.run()


if __name__ == "__main__":
    main()
