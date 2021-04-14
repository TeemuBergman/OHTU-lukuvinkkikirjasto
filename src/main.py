from flask import Blueprint, redirect, render_template, request
from .tips import Tips
from . import db

tips = Tips()
main = Blueprint('main', __name__)


@main.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "GET":
        existing_tips = tips.display_all()
        existing_tips = existing_tips[1].fetchall()
        return render_template("home.html", existing_tips = existing_tips)

    if request.method == "POST":
        tip_name = request.form["tip_name"]
        tip_url = request.form["tip_url"]

        if tips.add_tip(tip_name, tip_url):
            return redirect("/")
        else:
            return render_template("error.html", message = "Vinkin tallennus epäonnistui.")


@main.route("/results", methods = ["GET"])
def result():
    tip_name = request.args["tip_search"]
    formatted_searches = tips.search_by_writer_name(tip_name)
    if formatted_searches is None:
        return render_template("error.html", message = "Hakutulosten hakeminen epäonnistui.")
    return render_template("results.html", search_by_name = formatted_searches)


@main.route('/profile')
def profile():
    return 'Profile'


@main.route("/ping")
def ping():
    return "Pong"
