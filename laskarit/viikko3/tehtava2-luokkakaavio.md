# Tehtävä 2: Laajennettu Monopoli

Laajennetaan edellisen tehtävän luokkakaaviota tuomalla esiin seuraavat asiat:

Ruutuja on useampaa eri tyyppiä:
- Aloitusruutu
- Vankila
- Sattuma ja yhteismaa
- Asemat ja laitokset
- Normaalit kadut (joihin liittyy nimi)

Monopolipelin täytyy tuntea sekä aloitusruudun että vankilan sijainti.

Jokaiseen ruutuun liittyy jokin toiminto.

Sattuma- ja yhteismaaruutuihin liittyy kortteja, joihin kuhunkin liittyy joku toiminto.

Toimintoja on useanlaisia. Ei ole vielä tarvetta tarkentaa toiminnon laatua.

Normaaleille kaduille voi rakentaa korkeintaan 4 taloa tai yhden hotellin. Kadun voi omistaa joku pelaajista. Pelaajilla on rahaa.

## Luokkakaavio

```mermaid
 classDiagram
    Peli "1" -- "2" Noppa
    Peli "1" -- "2-8" Pelaaja
    Peli "1" -- "1" Pelilauta
    Pelaaja "1" -- "1" Pelinappula
    Pelilauta "1" -- "40" Ruutu
    Pelinappula "1" ..> "1" Ruutu
    sattumaRuutu ..> sattumaPakka
    yhteismaaRuutu ..> yhteismaaPakka
    sattumaPakka "1" -- "n" sattumaKortti
    yhteismaaPakka "1" -- "n" yhteismaaKortti
    Ruutu <|-- katuRuutu
    Ruutu <|-- aloitusRuutu
    Ruutu <|-- vankilaRuutu
    Ruutu <|-- asemaRuutu
    Ruutu <|-- laitosRuutu
    Ruutu <|-- sattumaRuutu
    Ruutu <|-- yhteismaaRuutu
    class Peli {
        aloitusSijainti
        vankilaSijainti
    }
    class Noppa
    class Pelaaja {
        nimi
        rahavarat
    }
    class Pelilauta {
        ruudut[]
    }
    class Ruutu {
        nimi
        sijainti
        toiminto
    }
    class katuRuutu {
        rakennukset
        omistaja
    }
    class aloitusRuutu
    class vankilaRuutu
    class asemaRuutu
    class laitosRuutu
    class sattumaRuutu
    class yhteismaaRuutu

    class Pelinappula {
        sijainti
    }
    class sattumaKortit
    class yhteismaaKortit
    class sattumaKortti {
        toiminto
    }
    class yhteismaaKortti {
        toiminto
    }
```
