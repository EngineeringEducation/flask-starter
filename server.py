import os

from flask import Flask, render_template, request, redirect, session as flask_session

from model import db, Melon


DATABASE_URL = "sqlite:///melons.db"
SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", "development")


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SECRET_KEY'] = SECRET_KEY


@app.route("/")
def index():
    """Show homepage with number-of-visits count."""

    num = flask_session["visits"] = flask_session.get("visits", 0) + 1
    return render_template("index.html", num=num)


@app.route("/melons")
def melons():
    """Show list of melons from our database."""

    melons = db.session.query(Melon).all()
    return render_template("melons.html", melons=melons)


@app.route("/add-melon", methods=['POST'])
def add_melon():
    """Add a melon and redirect to list of melons."""

    name = request.form.get("name")
    new_melon = Melon(name=name)
    db.session.add(new_melon)
    db.session.commit()

    return redirect("/melons")


if __name__ == '__main__':
    # Connect our application to our database
    db.init_app(app)

    # Create the tables we need from our models (if they already
    # exist, nothing will happen here, so it's fine to do this each
    # time on startup)
    db.create_all(app=app)

    app.run(debug=True)
