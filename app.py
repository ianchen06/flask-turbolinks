import os

from flask import Flask, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/test")
def test():
    return redirect(url_for("about"))


@app.after_request
def turbolinks_redirect(response):
    # If this is a redirect, append the target to session
    if "Location" in response.headers:
        session["_turbolinks_redirect_to"] = response.headers["Location"]
    else:
        # If there is redirect target in session, set the header so Turbolinks will change the browser location
        if session.get("_turbolinks_redirect_to"):
            response.headers["Turbolinks-Location"] = session.pop(
                "_turbolinks_redirect_to"
            )
    return response
