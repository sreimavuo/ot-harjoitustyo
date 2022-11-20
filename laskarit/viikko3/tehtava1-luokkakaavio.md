# Tehtävä 1: Monopoli

Monopolia pelataan käyttäen kahta noppaa. Pelaajia on vähintään 2 ja enintään 8. Peliä pelataan pelilaudalla joita on yksi. Pelilauta sisältää 40 ruutua. Kukin ruutu tietää, mikä on sitä seuraava ruutu pelilaudalla. Kullakin pelaajalla on yksi pelinappula. Pelinappula sijaitsee aina yhdessä ruudussa.

## Luokkakaavio

```mermaid
 classDiagram
    Peli "1" -- "2" Noppa
    Peli "1" -- "2-8" Pelaaja
    Peli "1" -- "1" Pelilauta
    Pelaaja "1" -- "1" Pelinappula
    Pelilauta "1" -- "40" Ruutu
    Pelinappula "1" ..> "1" Ruutu
    class Peli
    class Noppa
    class Pelaaja
    class Pelilauta
    class Ruutu {
        seuraavaRuutu
    }
    class Pelinappula
```
