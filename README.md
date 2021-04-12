## Ohjelmistotuotanto 2021 Kevät

![GitHub Actions](https://github.com/HJJHeinonen/OHTU-lukuvinkkikirjasto/workflows/CI/badge.svg) [![codecov](https://codecov.io/gh/HJJHeinonen/OHTU-lukuvinkkikirjasto/branch/master/graph/badge.svg?token=S3WQ2AE38H)](https://codecov.io/gh/HJJHeinonen/OHTU-lukuvinkkikirjasto)

Tämä repositorio on Helsingin yliopiston Ohjelmistotuotanto-kurssin miniprojektia varten. 

### Lukuvinkkisovellus 

[Product & sprint backlog](https://docs.google.com/spreadsheets/d/1kFCFZe4UMkpglo9DqtTRXQ08rH0ui6qu4qKGbNE_1bk)

### Komentorivitoiminnot

#### Sovelluksen käynnistäminen

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

Src-hakemistossa aja komento:

```bash
flask run
```

Sovellus on nyt käytettävissä selaimen osoitteessa [http://127.0.0.1:5000/](http://127.0.0.1:5000/).





