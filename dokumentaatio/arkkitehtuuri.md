# Arkkitehtuuri

## Sovelluslogiikka

Sovellus noudattaa kerrosarkkitehtuuria, jossa käyttöliittymä on eriytetty sovelluslogiikasta.

```mermaid
classDiagram
    class WeatherService {
        -location_repository: LocationRepository
        +add_location(location)
        +get_locations()
        +remove_location(location) 
        +get_weather(location)
    }
    
    class LocationRepository {
        -connection
        +find_all()
        +create(location)
        +delete(location)
    }
    
    class DatabaseConnection {
        +get_database_connection()
    }
    
    WeatherService --> LocationRepository
    LocationRepository --> DatabaseConnection