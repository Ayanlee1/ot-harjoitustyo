## Monopoli, alustava luokkakaavio

```mermaid
 classDiagram
    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta
    Pelilauta "1" -- "40" Ruutu
    Ruutu "1" -- "1" Ruutu : seuraava
    Ruutu "1" -- "0..8" Pelinappula
    Pelinappula "1" -- "1" Pelaaja
    Pelaaja "2..8" -- "1" Monopolipeli

    Ruutu <|-- Aloitusruutu
    Ruutu <|-- Vankila
    Ruutu <|-- Sattuma
    Ruutu <|-- Yhteismaa
    Ruutu <|-- Asema
    Ruutu <|-- Laitos
    Ruutu <|-- Katu

    Sattuma "1" -- "0..*" Kortti
    Yhteismaa "1" -- "0..*" Kortti

    Kortti "1" -- "1" Toiminto
    
    Ruutu "1" -- "1" Toiminto

    class Monopolipeli {
        aloitusruutu
        vankila
    }
    

    class Pelaaja {
        rahaa
    }

    class Katu {
        talojen_lkm
        hotelli
    }

    Katu "1" -- "0..1" Pelaaja: omistaa
