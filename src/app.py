from flask import Flask
from flask import redirect, render_template, request
from tips import Tips


app = Flask(__name__)
tips = Tips()


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        existing_tips = tips.display_all()
        existing_tips = existing_tips[1].fetchall()
        return render_template("home.html", existing_tips=existing_tips)

    if request.method == "POST":
        tip_name = request.form["tip_name"]
        tip_url = request.form["tip_url"]

        if tips.add_tip(tip_name, tip_url):
            return redirect("/")

        else:
            return render_template("error.html", message="Vinkin tallennus epäonnistui.")

@app.route("/register", methods=["GET","POST"])
def register():
  if request.method=="GET":
    return render_template("register.html")
  if request.method=="POST":
    #Tähän ehto jos rekisteröinti onnistuu ..
    return redirect("/")


@app.route("/results", methods=["GET"])
def result():
    tip_name = request.args["tip_search"]
    formatted_searches = tips.search_by_writer_name(tip_name)
    if formatted_searches == None:
      return render_template("error.html", message="Hakutulosten hakeminen epäonnistui.")
    return render_template("results.html", search_by_name=formatted_searches)


@app.route("/ping")
def ping():
    return "Pong"
