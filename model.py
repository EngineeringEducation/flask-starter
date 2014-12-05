from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Melon(db.Model):
    """Melon we offer for sale."""

    id = db.Column(db.Integer,
                   nullable=False,
                   primary_key=True)

    name = db.Column(db.String(50),
                     nullable=False,
                     unique=True)