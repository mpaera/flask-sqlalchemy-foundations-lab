from flask import Flask, jsonify
from flask_migrate import Migrate

from models import db, Earthquake


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)


@app.route("/")
def index():
    return {"message": "Welcome to the Earthquake API"}


@app.route("/earthquakes/<int:id>")
def earthquake_by_id(id):
    earthquake = Earthquake.query.filter_by(id=id).first()

    if earthquake is None:
        return jsonify({
            "message": f"Earthquake {id} not found."
        }), 404

    return jsonify({
        "id": earthquake.id,
        "magnitude": earthquake.magnitude,
        "location": earthquake.location,
        "year": earthquake.year
    }), 200


@app.route("/earthquakes/magnitude/<float:magnitude>")
def earthquakes_by_magnitude(magnitude):
    earthquakes = Earthquake.query.filter(
        Earthquake.magnitude >= magnitude
    ).all()

    quakes = [
        {
            "id": earthquake.id,
            "magnitude": earthquake.magnitude,
            "location": earthquake.location,
            "year": earthquake.year
        }
        for earthquake in earthquakes
    ]

    return jsonify({
        "count": len(quakes),
        "quakes": quakes
    }), 200


if __name__ == "__main__":
    app.run(port=5555, debug=True)