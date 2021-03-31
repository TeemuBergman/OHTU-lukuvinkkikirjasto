
from db import db
import db_wrapper as default_db_wrapper

class Tips():
  def __init__(self, db_handler=default_db_wrapper):
    self.db_handler = db_handler

  def add_tip(tip_name,tip_url):
    return self.db_handler.add_tip(tip_name,tip_url)
