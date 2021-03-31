
from db_wrapper import db_wrapper as default_db_wrapper
import string


class Tips():
  def __init__(self, db_handler=default_db_wrapper):
    self.db_handler = db_handler

  def add_tip(self, name:str, url:str):
    allowed_name_chars = string.ascii_letters + string.digits + "åäöÅÄÖ .,@%_"
    allowed_url_chars = string.ascii_letters + string.digits + "%/:.@?_=-"
        
    if (self.validate(name, allowed_name_chars, 100) and 
        self.validate(url, allowed_url_chars, 200)
    ):
      return self.db_handler.insert({"name":name, "url":url})
      
    else:
      print ("not valid input")
      return False
    
   
  def validate(self, field, encoding:str, length:int):
    
    if len(field) <= length:
      for character in field:
        if character not in encoding:
          return False
      return True

 
