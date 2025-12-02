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
        +get_forecast(location, days)
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
```

## Käyttöliittymä

Käyttöliittymä on toteutettu tekstipohjaisena `index.py`. Se tarjoaa valikon, jonka kautta käyttäjä voi:

- Lisätä uusia paikkoja
- Tarkastella tallennettuja paikkoja
- Poistaa paikkoja
- Katsoa nykyistä säätä paikalle
- Katsoa 5 päivän sääennusteen paikalle

Käyttöliittymä kutsuu `WeatherService`-luokan metodeja ja näyttää tulokset käyttäjälle.


## Tietojen tallennus

Paikkatiedot tallennetaan SQLite-tietokantaan `locations`-tauluun.
`LocationRepository`-luokka huolehtii tietokantaoperaatioista ja noudattaa Repository-suunnittelumallia.


## Päätoiminnallisuudet

### 5 päivän sääennusteen hakeminen

Kun käyttäjä valitsee valikosta vaihtoehdon "5 - Näytä 5 päivän ennuste" ja syöttää paikan nimen, sovellus toimii seuraavasti:

```mermaid
sequenceDiagram
    actor Käyttäjä
    participant Käyttöliittymä
    participant WeatherService
    participant LocationRepository

    Käyttäjä->>Käyttöliittymä: Valitse "5 - Näytä 5 päivän ennuste"
    Käyttöliittymä->>Käyttäjä: "Minkä paikan ennuste haluat?"
    Käyttäjä->>Käyttöliittymä: Syötä "Helsinki"
    Käyttöliittymä->>WeatherService: get_forecast("Helsinki", 5)
    WeatherService->>LocationRepository: find_all()
    LocationRepository-->>WeatherService: paikkalista
    WeatherService-->>Käyttöliittymä: ennustelista
    Käyttöliittymä-->>Käyttäjä: Näytä 5 päivän ennuste
```
Sekvenssikaavio kuvaa uuden sääennustetoiminnallisuuden toimintaa. Käyttöliittymä kutsuu `WeatherService`-luokan `get_forecast`-metodia, joka hakee tallennetut paikat `LocationRepository`:n kautta. Ennusteet palautetaan käyttöliittymälle, joka näyttää ne käyttäjälle. 

