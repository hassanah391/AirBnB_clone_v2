#!/usr/bin/python3
""""xdk"""
from flask import Flask, render_template
from models import storage
from models import *
app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def fetch_citiesByStates():
    states = storage.all("State").values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template(
        "8-cities_by_states.html",
        states=sorted_states
        )


@app.teardown_appcontext
def tear_down(self):
    """After each request removes
    the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
