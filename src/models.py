from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(100), unique = True)
    name = db.Column(db.String(1000))
    password = db.Column(db.String(100))


class TipBook(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.String(1000))
    book_name = db.Column(db.String(1000))
    url = db.Column(db.String(1000))
