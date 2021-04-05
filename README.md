## Ohjelmistotuotanto 2021 Kevät

![GitHub Actions](https://github.com/HJJHeinonen/OHTU-lukuvinkkikirjasto/workflows/CI/badge.svg) [![codecov](https://codecov.io/gh/HJJHeinonen/OHTU-lukuvinkkikirjasto/branch/master/graph/badge.svg?token=S3WQ2AE38H)](https://codecov.io/gh/HJJHeinonen/OHTU-lukuvinkkikirjasto)

Tämä repositorio on Helsingin yliopiston Ohjelmistotuotanto-kurssin miniprojektille suunnattu. 

**Ryhmä C**

### Lukuvinkkisovellus 

[Product & sprint backlog](https://docs.google.com/spreadsheets/d/1kFCFZe4UMkpglo9DqtTRXQ08rH0ui6qu4qKGbNE_1bk)

### Sovelluksen käynnistäminen

Tarkista, että poetry asennettu koneellesi komennolla:
```
poetry --version
```
Jos ei ole asennettu, poetry tarjoaa dokumentaatiossaan useita [asennusvaihtoehtoja](https://python-poetry.org/docs/#installation).

Kun projekti on kloonattu koneelle, asenna riippuvuudet ja alusta virtuaaliympäristö komennolla:

```bash
poetry install
```

Tämän jälkeen siirry alihakemistoon **src** komennolla

```bash
cd src
```
Hakemistossa aja komento

```bash
flask run
```

Sovelluksen pitäisi aueta localhostiin osoitteeseen [http://127.0.0.1:5000/](http://127.0.0.1:5000/).
