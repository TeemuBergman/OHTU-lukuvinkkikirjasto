﻿from flask import Blueprint, redirect, render_template, request, session
from flask_login import login_required
from .tips import Tips
from . import db
from .db_wrapper import DBWrapper

main = Blueprint('main', __name__)


@main.route("/add_tips", methods=["GET", "POST"])
@login_required
def add_tips():
    # tipsin alustus laitettu tänne jotta saadaan käyttäjän user_id mukaan.
    tips = Tips(DBWrapper(db), session["_user_id"])

    if request.method == "GET":
        unread_tips = tips.display_unread_tips()
        read_tips = tips.display_read_tips()

        return render_template("add_tips.html", unread_tips=unread_tips, read_tips=read_tips)

    if request.method == "POST":
        tip_name = request.form["tip_name"]
        tip_url = request.form["tip_url"]
        tip_title = request.form["tip_title"]

        if tips.add_tip(tip_name, tip_url, tip_title):
            return redirect("/add_tips")
        else:
            return render_template("error.html", message="Vinkin tallennus epäonnistui.")


@main.route("/results", methods=["GET"])
@login_required
def result():
    # tipsin alustus laitettu tänne jotta saadaan käyttäjän user_id mukaan.
    tips = Tips(DBWrapper(db), session["_user_id"])

    tip_name = request.args["tip_search"]
    formatted_searches = tips.search_by_writer_name(tip_name)
    if formatted_searches is None:
        return render_template("error.html", message="Ei hakutuloksia.")
    return render_template("results.html", search_by_name=formatted_searches)


@main.route("/delete", methods=["POST"])
@login_required
def submit():
    if request.form["action"] == "Poista":
        return delete_tip()

    if request.form["action"] == "Luettu / Ei luettu":
        return check_tip()


def delete_tip():
    tips = Tips(DBWrapper(db), session["_user_id"])
    tip_id = request.form["tip_id"]
    tips.delete_tip(tip_id)
    return redirect("/add_tips")


def check_tip():
    # tipsin luetuksi merkitseminen
    tips = Tips(DBWrapper(db), session["_user_id"])
    tip_id = request.form["tip_id"]
    tips.read_check_tip(tip_id)
    return redirect("/add_tips")


# Tarpeellinen Githubin Robot testaukseen
@main.route("/ping")
def ping():
    return "Pong"
