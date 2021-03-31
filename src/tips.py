
from db import db

def add_tip(tip_name,tip_url):
  try:
    sql="INSERT INTO <tässä taulun nimi> (name, url) VALUES (:name, :url)"
    db.session.execute(sql, {"name":tip_name, "url":tip_url})
    db.session.commit()
  except:
    return False
  return True