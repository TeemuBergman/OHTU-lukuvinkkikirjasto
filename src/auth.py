from flask import Blueprint, render_template, redirect, url_for, request, session
from flask_login import login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db
from .tips import Tips
from .db_wrapper import DBWrapper


auth = Blueprint("auth", __name__)


@auth.route("/")
def login():

    # tipsin alustus laitettu tänne jotta saadaan käyttäjän user_id mukaan.
    tips = Tips(DBWrapper(db))
    existing_tips = tips.display_all_all_users()
    user_id = session.get("_user_id",0)

    #if request.method == "GET":
    # return render_template("add_tips.html", existing_tips=existing_tips)

    return render_template("login.html",  existing_tips=existing_tips, user_id=user_id)


@auth.route("/", methods=["GET", "POST"])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        return redirect(url_for('auth.login'))

    login_user(user, remember=remember)

    return redirect(url_for('main.add_tips'))


@auth.route("/register")
def register():
    return render_template("register.html")


@auth.route("/register", methods=["POST"])
def register_post():
    email = request.form.get("email")
    name = request.form.get("name")
    password = request.form.get("password")

    user = User.query.filter_by(email=email).first()

    if user:
        return redirect(url_for("auth.register"))

    new_user = User(email=email, name=name,
                    password=generate_password_hash(password, method="sha256"))

    db.session.add(new_user)
    db.session.commit()

    login_user(new_user)

    return redirect(url_for("auth.login"))


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
