#!/usr/bin/python3
""""xdk"""
from flask import Flask, render_template
from models import storage
from models import *
app = Flask(__name__)



@app.route("/states_list", strict_slashes=False)
def fetch_states():
    state_objs = [obj for obj in storage.all("State").values()]
    return render_template("7-states_list.html", 
                           state_objs=state_objs)

@app.teardown_appcontext
def tear_down(self):
    """After each request removes
    the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)