
from db import db

class db_wrapper():
    def __init__(self):
        pass

    def add_tip(self, tip_name,tip_url):
        try:
            sql="INSERT INTO <tässä taulun nimi> (name, url) VALUES (:name, :url)"
            db.session.execute(sql, {"name":tip_name, "url":tip_url})
            db.session.commit()
        except:
            return False
        return True

db_wrapper = db_wrapper()