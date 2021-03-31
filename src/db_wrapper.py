
import sqlite3 

class db_wrapper():
    def __init__(self):
        
        self.init_db()
        
    def __do_query(self, sql:str, fields:dict={}):
        try:
            db = sqlite3.connect("tips.db")
            db.isolation_level = None
            query = sql
            db.execute(query, fields)
            db.commit()
        except Exception as e:
            print (f"exception: {e}")
            return False
        return True


    def init_db(self):    
        # Tehdää uusi taulukko jos sitä ennestään ole.   
        query =  "CREATE TABLE IF NOT EXISTS lukuvinkit (id INTEGER PRIMARY KEY, name TEXT NOT NULL, url TEXT);"
        self.__do_query(query)
              

    def insert(self, fields:dict):
        query = "INSERT INTO lukuvinkit (name, url) VALUES (:name, :url)"
        return self.__do_query(query, {"name":fields["name"], "url":fields["url"]})
       

db_wrapper = db_wrapper()