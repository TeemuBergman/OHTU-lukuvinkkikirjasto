## Ohjelmistotuotanto 2021 Kevät

![GitHub Actions](https://github.com/HJJHeinonen/OHTU-lukuvinkkikirjasto/workflows/CI/badge.svg) [![codecov](https://codecov.io/gh/HJJHeinonen/OHTU-lukuvinkkikirjasto/branch/master/graph/badge.svg?token=S3WQ2AE38H)](https://codecov.io/gh/HJJHeinonen/OHTU-lukuvinkkikirjasto)

Tämä repositorio on Helsingin yliopiston Ohjelmistotuotanto-kurssin miniprojektia varten. 

### Lukuvinkkisovellus 

Sovelluksen tarkoitus on pystyä tallettamaan erinäisiä lukuvinkkejä, sekä selaamaan niitä.

[Product & sprint backlog](https://docs.google.com/spreadsheets/d/1kFCFZe4UMkpglo9DqtTRXQ08rH0ui6qu4qKGbNE_1bk)


### Sovelluksen käynnistäminen

Sovellus käyttää riippuvuuksien hallintaan poetrya, joka tulisi löytyä koneeltasi. Mikäli sinulla ei ole poetrya asennettuna, poetry tarjoaa dokumentaatiossaan useita [asennusvaihtoehtoja](https://python-poetry.org/docs/#installation). Voit tarkistaa, että poetry on asennettu koneellesi komennolla:
```
poetry --version
```
Kun poetry on asennettu, voit kloonata projektin koneellesi.
Kun projekti on kloonattu, asenna riippuvuudet ja alusta virtuaaliympäristö komennolla:

```bash
poetry install
```

Tämän jälkeen siirry alihakemistoon **src**, ja käynnistä virtuaaliympäristö komennoilla:

```bash
cd src
```
```bash
poetry shell
```

Src-hakemistossa aja seuraava komento Flask-palvelimen käynnistämiseksi:

```bash
flask run
```

Sovellus on nyt käytettävissä selaimen osoitteessa [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

### Testaus

Sovelluksessa on käytetty yksikkötestejä, sekä hyväksymistestejä Robot Frameworkin avulla. Sovellusta käynnistäessä ajettu **poetry install**-komento on asentanut testausta varten tarvittavat riippuvuudet.

#### Yksikkötestit

Yksikkötestien ajamista varten tulee olla projektihakemistossa virtuaaliympäristössä. Virtuaaliympäristöön pääset komennolla:

```bash
poetry shell
```
Tämän jälkeen testit voi ajaa komennolla:

```bash
pytest
```

#### Hyväksymistestit

Hyväksymistestien ajamista varten Flask-palvelimen on oltava käynnissä. Mennään ensin virtuaaliympäristöön komennolla:

```bash
poetry shell
```
Tämän jälkeen testit voi ajaa komennolla:

```bash
robot src/tests/robotframework
```

**Mikäli testien ajaminen ei onnistu, tarkistathan, että suhteellinen polku hakemistoon on oikea**.



