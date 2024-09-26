from flask import render_template, request, redirect, url_for, session
from gamebacklog import app, db
from werkzeug.security import generate_password_hash, check_password_hash
from gamebacklog.models import Genre, Game

@app.route("/")
def home():
    if "username" in session:
        return redirect(url_for('dashboard'))
    return render_template("index.html")