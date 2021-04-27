## Ohjelmistotuotanto 2021 Kevät

![GitHub Actions](https://github.com/HJJHeinonen/OHTU-lukuvinkkikirjasto/workflows/CI/badge.svg) [![codecov](https://codecov.io/gh/HJJHeinonen/OHTU-lukuvinkkikirjasto/branch/master/graph/badge.svg?token=S3WQ2AE38H)](https://codecov.io/gh/HJJHeinonen/OHTU-lukuvinkkikirjasto)

Tämä repositorio on Helsingin yliopiston Ohjelmistotuotanto-kurssin miniprojektia varten.

### Lukuvinkkisovellus

Sovelluksen tarkoitus on pystyä tallettamaan erinäisiä lukuvinkkejä, sekä selaamaan niitä.

[Product & sprint backlog](https://docs.google.com/spreadsheets/d/1kFCFZe4UMkpglo9DqtTRXQ08rH0ui6qu4qKGbNE_1bk)

[CI-palvelu](https://github.com/HJJHeinonen/OHTU-lukuvinkkikirjasto/actions/workflows/main.yml)

[Loppuraportti](https://docs.google.com/document/d/1QKGBlKBjWdvmERDQaRFJ0YyxfSy0uT2hpfjtzI-Mo5g/edit#)

### Definition of Done

Yleisellä tasolla kuvatut laatuvaatimukset

* User storyssa määritelty toiminnallisuus toimii halutulla tavalla ja se on integroitu muuhun ohjelmistoon
* Sovellus tai sen testit eivät hajoa
* Tehty yksikkötestausta ja hyväksymistestausta
* Testattavan koodin testikattavuus kohtuullinen (vähintään n. 70%)
* Asiakas pääsee näkemään koko ajan koodin ja testien tilanteen CI-palvelusta
* Yhtenäinen koodityyli

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

Alusta projektin tietokanta käskyllä

```
poetry run python setup.py
```

Tämän jälkeen siirry alihakemistoon **src**, ja käynnistä virtuaaliympäristö komennoilla:

```bash
cd src
```
Src-hakemistossa aja seuraava komento Flask-palvelimen käynnistämiseksi:

```bash
poetry run flask run
```

Sovellus on nyt käytettävissä selaimen osoitteessa [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

### Testaus

Sovelluksessa on käytetty yksikkötestejä, sekä hyväksymistestejä Robot Frameworkin avulla. Sovellusta käynnistäessä ajettu **poetry install**-komento on asentanut testausta varten tarvittavat riippuvuudet.

#### Yksikkötestit

Yksikkötestit voi ajaa projektihakemiston juuresta komennolla:

```bash
poetry run pytest src
```

#### Hyväksymistestit

Hyväksymistestien ajamista varten Flask-palvelimen on oltava käynnissä. Testit voi ajaa projektin juuresta komennolla:

```bash
poetry run robot src/tests/robotframework
```

**Mikäli testien ajaminen ei onnistu, tarkistathan, että suhteellinen polku hakemistoon on oikea**.
