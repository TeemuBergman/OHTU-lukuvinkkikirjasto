from .models import TipBook
from datetime import datetime


class DBWrapper:
    def __init__(self, sqlalchemy_object):
        self.db = sqlalchemy_object

    def insert(self, fields: dict):

        new_tip = TipBook(user_id=fields["user_id"],
                          author=fields["author"],
                          url=fields["url"],
                          book_name=fields["book_name"],
                          read_check="Ei",
                          time_stamp=None)

        try:
            self.db.session.add(new_tip)
            self.db.session.commit()
            return True
        except Exception as e:
            print(f"exception: {e}")
            return False

    # Hakee kaikki olemassa olevat lukuvinkit tietokannasta, jotta ne voidaan esittää etusivulla

    def display_all_tips(self, user_id: int):
        return self.db.session.query(TipBook.book_name, TipBook.author, TipBook.url, TipBook.id, TipBook.read_check, TipBook.time_stamp).filter_by(user_id=user_id).all()

    # Hakee annetun kirjoittajan nimen perusteella tiedot
    def search_by_writer_name(self, author: str, user_id: int):
        return self.db.session.query(TipBook.book_name, TipBook.author, TipBook.url).filter_by(author=author, user_id=user_id).all()

    # Poistaa lukuvinkin
    def delete_tip(self, fields: dict):
        tip = fields["id"]
        self.db.session.query(TipBook).filter_by(id=tip).delete()
        self.db.session.commit()
        return True

    def read_check_tip(self, fields: dict):
        tip = fields["id"]
        new_tip = self.db.session.query(TipBook).filter_by(id=tip).first()

        if new_tip.read_check == "Kyllä":
            new_tip.read_check = "Ei"
            new_tip.time_stamp = None
        else:
            new_tip.read_check = "Kyllä"
            new_tip.time_stamp = datetime.today()

        self.db.session.commit()
        return True
