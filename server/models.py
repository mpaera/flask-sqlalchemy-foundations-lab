from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Earthquake(db.Model):
    _tablename_ = "earthquake"

    id = db.Column(db.Integer, primary_key=True)
    magnitude = db.Column(db.Float)
    location = db.Column(db.String)
    year = db.Column(db.Integer)

    def _repr_(self):
        return f"<Earthquake {self.id}: {self.location}>"