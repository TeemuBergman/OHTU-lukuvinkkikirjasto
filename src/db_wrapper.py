import sqlite3


class DBWrapper:
    def __init__(self):
        self.init_db()

    def __do_query(self, sql: str, fields: dict = {}):
        try:
            db = sqlite3.connect("tips.db")
            db.isolation_level = None
            query = sql
            # tallennetaan haun tulokset display_tips:in käyttöä varten
            results = db.execute(query, fields)
            db.commit()
        except Exception as e:
            print(f"exception: {e}")
            return False
        return True, results  # lisätään palautukseen myös results

    # Tehdää uusi taulukko jos sitä ennestään ole.
    def init_db(self):
        query = "CREATE TABLE IF NOT EXISTS lukuvinkit (id INTEGER PRIMARY KEY, name TEXT NOT NULL, url TEXT, title TEXT);"
        self.__do_query(query)

    def insert(self, fields: dict):
        query = "INSERT INTO lukuvinkit (name, url, title) VALUES (:name, :url, :title)"
        return self.__do_query(query, {"name": fields["name"], "url": fields["url"], "title": fields["title"]})[0]

    # Hakee kaikki olemassa olevat lukuvinkit tietokannasta, jotta ne voidaan esittää etusivulla
    def display_all_tips(self):
        query = "SELECT title, name, url FROM lukuvinkit"
        return self.__do_query(query)

    # Hakee annetun kirjoittajan nimen perusteella tiedot
    def search_by_writer_name(self, nimi):
        query = "SELECT name, title, url FROM lukuvinkit WHERE name LIKE ?"
        return self.__do_query(query, (nimi,))


db_wrapper = DBWrapper()
