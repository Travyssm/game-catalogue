from flask import render_template, request, redirect, url_for
from gamebacklog import app, db

@app.route("/")
def home():
    return render_template("base.html")