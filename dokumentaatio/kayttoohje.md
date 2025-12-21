# Käyttöohje

Lataa projektin viimeisimmän [releasen](https://github.com/Ayanlee1/ot-harjoitustyo/releases/tag/viikko5) lähdekoodi valitsemalla _Assets_-osion alta _Source code_.

## Asennus

1. Pura ladattu zip-tiedosto
2. Avaa terminaali ja siirry projektin juurihakemistoon: `cd ot-harjoitustyo`
3. Asenna riippuvuudet: `poetry install`
4. Alusta tietokanta: `poetry run python src/initialize_database.py`
5. Luo API-avainta varten `.env`-tiedosto projektin juureen:
   ```
   OPENWEATHER_API_KEY=oma_api_avaimesi_tähän
   ```
   - Saat API-avaimen rekisteröitymällä osoitteessa: https://openweathermap.org/api

## Käynnistys

### Ensisijainen tapa: Graafinen käyttöliittymä
Käynnistä sovellus komennolla: `poetry run invoke start`

### Vaihtoehtoinen tapa: Tekstipohjainen käyttöliittymä
Jos graafinen käyttöliittymä ei toimi, voit käyttää tekstipohjaista käyttöliittymää komennolla:
`poetry run python src/text_ui.py`

## Sovelluksen käyttö

### Graafinen käyttöliittymä
Sovellus avautuu ikkunaan, jossa on seuraavat toiminnot:
- **Paikan lisääminen**: Syötä paikan nimi tekstikenttään ja valitse "Lisää paikka"
- **Paikkojen listaus**: Kaikki tallennetut paikat näkyvät listassa
- **Paikan poistaminen**: Valitse paikka listasta ja valitse "Poista paikka"
- **Sään hakeminen**: Valitse paikka listasta ja valitse "Hae sää" nähdäksesi nykyisen säätilan
- **Ennusteen hakeminen**: Valitse paikka listasta ja valitse "Hae ennuste" nähdäksesi 5 päivän sääennusteen

### Tekstipohjainen käyttöliittymä
Sovellus käynnistyy päävalikkoon:

```
=== SÄÄSOVELLUS ===
1. Lisää paikka
2. Näytä paikat
3. Poista paikka
4. Hae sää
5. Hae 5 päivän ennuste
0. Lopeta
Valinta:
```

#### Toiminnot
1. **Paikan lisääminen** 
   - Valitse 1 ja syötä paikan nimi
   - Paikka tallentuu tietokantaan
   - Esimerkiksi: `Helsinki`

2. **Paikkojen listaus**
   - Valitse `2` nähdäksesi kaikki tallennetut paikat
   - Sovellus näyttää listan tallennetuista paikoista 

3. **Paikan poistaminen**
   - Valitse `3` ja syötä poistettavan paikan nimi
   - Paikka poistetaan tietokannasta

4. **Nykyisen sään hakeminen**
   - Valitse `4` ja syötä paikan nimi
   - Sovellus näyttää nykyisen lämpötilan ja säätilan 
   - Esimerkki: `Helsinki: 5.2°C, cloudy`

5. **5 päivän ennusteen hakeminen**
   - Valitse `5` ja syötä paikan nimi
   - Sovellus näyttää 5 päivän sääennusteen 
   - Jokaiselle päivälle näytetään päivämäärä, lämpötila ja sääkuvaus

0. **Sovelluksen sulkeminen**
   - Valitse `0` sulkeaksesi sovelluksen

## Muut komennot
- Testien suoritus: `poetry run invoke test`
- Testikattavuusraportti: `poetry run invoke coverage-report`
- Koodin laadun tarkistus: `poetry run invoke lint`
- Koodin formatointi: `poetry run invoke format`

## Ongelmanratkaisu

### Sovellus ei käynnisty
- Varmista että olet asentanut riippuvuudet: `poetry install`
- Tarkista että poetry on asennettuna: `poetry --version`
- Suorita alustus: `poetry run python src/initialize_database.py`
- Tarkista että `.env`-tiedosto on olemassa ja sisältää API-avaimen

### Säähavainnot eivät toimi
- Tarkista internetyhteys
- Tarkista että API-avain on oikein `.env`-tiedostossa
- Sovellus käyttää OpenWeatherMap API:a, joka vaatii toimivan internet-yhteyden

### Graafinen käyttöliittymä ei toimi
- Kokeile tekstipohjaista käyttöliittymää: `poetry run python src/text_ui.py`
- Tarkista että TkInter on asennettuna (se tulee Pythonin mukana)

### Tietokantaongelmat
- Voit aloittaa alusta poistamalla `data/weather.db`-tiedoston ja suorittamalla alustuksen uudelleen
