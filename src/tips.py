
from db_wrapper import db_wrapper as default_db_wrapper
import string


class Tips():
  def __init__(self, db_handler=default_db_wrapper):
    self.db_handler = db_handler
    self.allowed_name_chars = string.ascii_letters + string.digits + "åäöÅÄÖ .,@%_"
    self.allowed_url_chars = string.ascii_letters + string.digits + "%/:.@?_=-"
    self.allowed_name_length = 100
    self.allowed_url_length = 200

  def add_tip(self, name:str, url:str):        
    if (self.validate(name, self.allowed_name_chars, self.allowed_name_length) and 
        self.validate(url, self.allowed_url_chars, self.allowed_url_length)
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

 
