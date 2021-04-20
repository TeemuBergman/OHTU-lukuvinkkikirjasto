from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(1000))
    password = db.Column(db.String(100))


class TipBook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # lisätyn tietueen kytkeminen tiettyyn käyttäjään
    user_id = db.Column(db.Integer)
    author = db.Column(db.String(1000))
    book_name = db.Column(db.String(1000))
    url = db.Column(db.String(1000))
    read_check = db.Column(db.String(1000))
    time_stamp = db.Column(db.Date)
