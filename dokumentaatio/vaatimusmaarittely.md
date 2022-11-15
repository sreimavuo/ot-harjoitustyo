
# Vaatimusmäärittely

Loadouts - Pakkauslistojen hallinta

## Sovelluksen tarkoitus

Loadout (https://www.collinsdictionary.com/dictionary/english/loadout) on suomeksi käytännössä pakkauslista.

Sovelluksen tarkoitus on auttaa luomaan ja hallitsemaan pakkauslistoja omille varusteille eri käyttötilanteita varten (esim. repun pakkaus kolmen päivän työmatkalle, tai repun pakkaus mökkireissulle, tai viikonlopun lomareissulle).

(Tavallaan muunnelma todo-sovelluksesta, mutta katsotaan miten pitkälle tämä kehittyy..)

## Käyttäjät

Sovellus on yhden käyttäjän graafinen työpöytäsovellus.

## Toiminnallisuus

Functional Requirements:
- Lisätä (ja poistaa) tavaroita
- Lisätä (ja poistaa) "containereita" (taskuja/pusseja/yms eli tavaroita mihin voi laittaa sisään tavaroita
- Lisätä (ja poistaa) eri käyttötilanteita
- Järjestellä listasta tavaroita "containereihin" kunkin käyttötilanteen alle
- Tulostaa pakkauslistan käyttötilanteelle

Non-Functional Requirements:
- Sovelluksen toteutuskieli on Python ja graafinen käyttöliittymä toteutetaan Pythonin mukana tulevalla TkInter-kirjastolla jotta sovellus toimisi eri alustoilla.
- Tiedot tallennetaan sovelluksen omaan paikalliseen SQLite-tietokantaan.

## Käyttöliittymäluonnos





## Kehitysideoita

- Useamman käyttäjän tuki
- Kuvan lisääminen esineille
- Pakkauslistan generoiminen pdf-tiedostoksi (minkä voi printata pakkauksen avuksi)
- Pakkauslistan export/import toiminto millä saa sovelluksen tiedot varmistettua/palautettua
- Eri käyttöliittymiä (teksti/web/skriptattu)
- Havainnekuvien lisääminen containereille (mistä näkee esim. mitä repun taskua/lokeroa tarkoitetaan)
- Jonkinlainen helppitoiminnallisuus
- Kielen valinta (englanti/suomi/ruotsi(?))
