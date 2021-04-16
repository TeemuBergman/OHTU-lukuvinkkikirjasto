from .models import TipBook
from sqlalchemy.orm import Session


class DBWrapper:
    def __init__(self, sqlalchemy_object):
        self.db = sqlalchemy_object
        print("alkemy session", self.db.session)
        
        
    def insert(self, fields: dict):
        
        new_tip = TipBook(user_id = fields["user_id"], 
                          author = fields["author"], 
                          url = fields["url"], 
                          book_name = fields["book_name"])
      
        try:
            self.db.session.add(new_tip)
            self.db.session.commit()
            return True
        except Exception as e:
            print(f"exception: {e}")
            return False

        
    # Hakee kaikki olemassa olevat lukuvinkit tietokannasta, jotta ne voidaan esittää etusivulla
    def display_all_tips(self, user_id:int):
        return self.db.session.query(TipBook.book_name, TipBook.author, TipBook.url).filter_by(user_id=user_id).all()

    # Hakee annetun kirjoittajan nimen perusteella tiedot
    def search_by_writer_name(self, author:str, user_id:int):
        return self.db.session.query(TipBook.book_name, TipBook.author, TipBook.url).filter_by(author=author, user_id=user_id).all()


