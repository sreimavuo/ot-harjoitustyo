# Vaatimusmäärittely

## Sovelluksen tarkoitus

Ajatuksena on tehdä Microsoft OneNoten ja Apple Notesin tyylinen sovellus muistiinpanojen tekemiseen ja jaotteluun.

## Käyttäjät

- Sovellus ei sisällä käyttäjähallintaa, oletus on että kukin käyttäjä käyttää sovellusta omalla tunnuksellaan ja tallentaa muistikirjan esim. omaan kotihakemistoonsa.

## Suunnitellut toiminnallisuudet

- Sovellus etsii käynnistyshakemistosta olemassa olevaa muistikirjaa, jos sitä ei löydy, pyytää käyttäjältä nimeä uudelle ja luo sen
- Muistikirjaan voi tehdä kansioita (folder)
- Muistikirjaan voi tehdä muistiinpanoja (note) mihin voi kirjoittaa tekstiä
- Muistiinpanot tallennetaan käynnistyshakemiston alle sovelluksen omaan hakemistoon, kansiota vastaa tiedostojärjestelmän kansio, muistiinpanoa tekstitiedosto.
- Tallennus käyttäjän erillisellä valinnalla (näppäinoikotie tai menu-valinta)

## Mahdolliset lisäominaisuudet

- Tekstin ulkoasun muokkaus käyttäen jotain avointa standardia, esim. Markdown tai Asciidoc
- Useamman muistikirjan tuki (muistikirjojen luominen, avaaminen ja sulkeminen)
- Kuvien lisääminen
- Tietokanta tallennusvälineenä (ja export-toiminnallisuus tiedostoiksi)
- Jatkuva tallennus (esim. tietyn sekuntimäärän välein)
- Muistiinpanojen siirtäminen kansiosta toiseen
- Tagien lisääminen, muistiinpanojen listaaminen/jaotteleminen niiden perusteella
