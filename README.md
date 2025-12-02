# ot-harjoitustyo

## Sääsovellus

Sovellus, joka näyttää nykyisen säätilan ja ennusteen käyttäjälle.

## Käyttöohjeet

### Asennus
1. Asenna riippuvuudet: poetry install
2. Luo tietokantataulut komennolla: poetry run python src/initialize_database.py
3. Käynnistä sovellus: poetry run invoke start

### Muut komennot
- Testien suoritus: poetry run invoke test
- Testikattavuusraportti: poetry run invoke coverage-report
- Koodin laadun tarkistus: poetry run invoke lint
- Koodin formatointi: poetry run invoke format

## Harjoitustyön dokumentaatio

- [Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](dokumentaatio/tyoaikakirjanpito.md)
- [Changelog](dokumentaatio/changelog.md)
- [Arkkitehtuuri](dokumentaatio/arkkitehtuuri.md)
- [Releases](https://github.com/Ayanlee1/ot-harjoitustyo/releases/tag/viikko5) -sivulta