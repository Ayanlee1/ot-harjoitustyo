# ot-harjoitustyo

## Sääsovellus

Sovellus, joka näyttää nykyisen säätilan ja ennusteen käyttäjälle.

## Käyttöliittymät

### Ensisijainen: Graafinen käyttöliittymä
Sovelluksella on graafinen käyttöliittymä, joka käynnistetään komennolla:
```bash
poetry run invoke start
```

### Varakäyttöliittymä: Tekstipohjainen
Jos graafinen käyttöliittymä ei toimi, voit käyttää tekstipohjaista käyttöliittymää:
```bash
poetry run python src/text_ui.py
```

## API-avaimen konfigurointi

Sovellus tarvitsee OpenWeatherMap-palvelun API-avaimen toimiakseen.

### 1. Hanki API-avain
1. Rekisteröidy osoitteessa: https://openweathermap.org/api
2. Luo ilmainen API-avain 
3. Kopioi luotu avain

### 2. Luo .env-tiedosto
Luo tiedosto nimeltä **`.env`** projektin juureen (samalle tasolle kuin `pyproject.toml`-tiedosto).

### 3. Lisää API-avain tiedostoon
Avaa `.env`-tiedosto tekstitiedostona ja lisää seuraava rivi:
```
OPENWEATHER_API_KEY=oma_api_avaimesi_tähän
```

Korvaa `oma_api_avaimesi_tähän` omalla OpenWeatherMap API-avaimellasi.

**Tiedostosijainti:**
```
ot-harjoitustyo/
|- dokumentaatio/
|- laskarit/
|- src/
|- .env              <- Luo tämä tiedosto tähän
|- pyproject.toml
```

## Asennus ja käyttö

### Asennus
1. Asenna riippuvuudet: `poetry install`
2. Luo tietokantataulut komennolla: `poetry run python src/initialize_database.py`
3. Käynnistä sovellus: `poetry run invoke start` (graafinen käyttöliittymä)

### Muut komennot
- Testien suoritus: `poetry run invoke test`
- Testikattavuusraportti: `poetry run invoke coverage-report`
- Koodin laadun tarkistus: `poetry run invoke lint`
- Koodin formatointi: `poetry run invoke format`

## Vianetsintä

- **Graafinen käyttöliittymä ei käynnisty:** Kokeile tekstipohjaista käyttöliittymää: `poetry run python src/text_ui.py`
- **"API-avainta ei löytynyt":** Tarkista että `.env`-tiedosto on projektin juuressa ja sisältää oikean API-avaimen
- **Sää ei näy:** Tarkista internet-yhteys ja että API-avain on oikein

## Harjoitustyön dokumentaatio

- [Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](dokumentaatio/tyoaikakirjanpito.md)
- [Changelog](dokumentaatio/changelog.md)
- [Arkkitehtuuri](dokumentaatio/arkkitehtuuri.md)
- [Releases](https://github.com/Ayanlee1/ot-harjoitustyo/releases)