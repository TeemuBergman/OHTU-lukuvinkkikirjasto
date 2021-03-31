from flask import Flask
from flask import redirect,render_template,request
import tips
from app import app

@app.route("/", methods=["GET","POST"])
def home():
  if request.method=="GET":
    return render_template("home.html")
  if request.method=="POST":
    tip_name = request.form["tip_name"]
    tip_url = request.form["tip_url"]
    if tips.add_tip(tip_name,tip_url):
      return redirect("/")
    else:
      return render_template("error.html", message="Vinkin tallennus epäonnistui")