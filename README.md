Harjoitustyö, Ohjelmistotekniikka, Syksy 2022

# Loadouts

## Dokumentaatio

[Vaatimusmäärittely](https://github.com/sreimavuo/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

[Tuntikirjanpito](https://github.com/sreimavuo/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.md)

[Changelog](https://github.com/sreimavuo/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)

## Sovelluksen riippuvuudet

Sovellus on kehitetty ja testattu Python versiolla 3.8.10 (sama mikä on asennettuna yliopiston melkki-palvelimella sekä VDI Cubbli -ympäristöissä).

## Asennus

1. Asenna riippuvuudet komennolla:

```text
poetry install
```

## Komentorivikomennot

### Ohjelman suorittaminen

Ohjelma suoritetaan komennolla:

```text
poetry run invoke start
```

### Testien ajaminen

Automaattiset yksikkötestit ajetaan komennolla:

```text
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportti tuotetaan komennolla:

```text
poetry run invoke coverage-report
```
