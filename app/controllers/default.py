from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user

from app import app, db, login_manager
from app.models.tables import User
from app.models.forms import LoginForm


@login_manager.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            flash("Logged in")
            return redirect(url_for("index"))
        else:
            flash("Invalid login")
    else:
        print(form.errors)
    return render_template("login.html", form=form)


@app.route("/logout", methods=["GET", "POST"])
def logout():
    logout_user()
    flash("Logged out")
    return redirect(url_for("index"))
