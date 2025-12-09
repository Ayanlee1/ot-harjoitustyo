# Käyttöohje
Lataa projektin viimeisimmän [releasen](https://github.com/Ayanlee1/ot-harjoitustyo/releases/tag/viikko5) lähdekoodi valitsemalla _Assets_-osion alta _Source code_.

## Asennus

1. Pura ladattu zip-tiedosto
2. Avaa terminaali ja siirry projektin juurihakemistoon:`cd ot-harjoitustyo`
3. Asenna riippuvuudet: `poetry install`
4. Alusta tietokanta: `poetry run python src/initialize_database.py`

## Käynnistys
Käynnistä sovellus komennolla: `poetry run invoke start`

## Sovelluksen käyttö
### Päävalikko
Sovellus käynnistyy päävalikkoon:

=== SÄÄSOVELLUS ===
1. Lisää paikka
2. Näytä paikat
3. Poista paikka
4. Hae sää
5. Hae 5 päivän ennuste
0. Lopeta
Valinta:

### Toiminnot
1. Paikan lisääminen 
- Valitse 1 ja syötä paikan nimi
- Paikka tallentuu tietokantaan
- Esimerkiksi: `Helsinki`

2. Paikkojen listaus
- Valitse `2` nähdäksesi kaikki tallennetut paikat
- Sovellus näyttää listan tallennetuista paikoista 

3. Paikan poistaminen
- Valitse `3` ja syötä poistettavan paikan nimi
- Paikka poistetaan tietokannasta

4. Nykyisen sään hakeminen
- Valitse `4` ja syötä paikan nimi
- Sovellus näyttää nykyisen lämpötilan ja säätilan 
- Esimerkki: `Helsinki: 5.2°C, cloudy`

5. 5 päivän ennusteen hakeminen
- Valitse `5` ja syötä paikan nimi
- Sovellus näyttää 5 päivän sääennusteen 
- Jokaiselle päivälle näytetään päivämäärä, lämpötila ja sääkuvaus

0. Sovelluksen sulkeminen
- Valitse `0` sulkeaksesi sovelluksen

### muut komennot
- Testien suoritus: `poetry run invoke test`
- Testikattavuusraportti: `poetry run invoke coverage-report`
- Koodin laadun tarkistus: `poetry run invoke lint`

### Ongelmanratkaisu

### Sovellus ei käynnisty
- Varmista että olet asentanut riippuvuudet: `poetry install`
- Tarkista että poetry on asennettuna: `poetry --version`
- Suorita alustus: `poetry run python src/initialize_database.py`

### Säähavainnot eivät toimi
- Tarkista internetyhteys
- Sovellus käyttää OpenWeatherMAp API:a, joka vaatii toimivan internet-yhteyden

### Tietokantaongelmat
- Voit aloittaa alusta poistamalla `data/weather.db`-tiedoston ja suorittamalla alustuksen uudelleen

