#!/usr/bin/python3
""""9-states Module"""
from flask import Flask, render_template
from models import storage
from models import *
app = Flask(__name__)


@app.route('/states')
@app.route('/states_list')
def fetch_states():
    """display html page
    fetch sorted states to insert into html in UL tag
    """
    state_objs = [s for s in storage.all("State").values()]
    return render_template(
        '7-states_list.html',
        state_objs=state_objs)


@app.route('/')
def hello_hbnb():
    """display text"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """display text"""
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    """display custom text given"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_text(text="is cool"):
    """display custom text given
       first route statement ensures it works for:
          curl -Ls 0.0.0.0:5000/python ; echo "" | cat -e
          curl -Ls 0.0.0.0:5000/python/ ; echo "" | cat -e
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def text_if_int(n):
    """display text only if int given"""
    return "{:d} is a number".format(n)


@app.route('/cities_by_states')
def fetch_cities_by_states():
    """display html page
    fetch sorted states to insert into html in UL tag
    fetch sorted cities in each state into LI tag ->in HTML file
    """
    state_objs = [s for s in storage.all("State").values()]
    return render_template(
        '8-cities_by_states.html',
        state_objs=state_objs)


@app.route('/states/<id>')
def stateID(id):
    """display html page; customize heading with state.name
    fetch sorted cities for this state ID into LI tag ->in HTML file
    """
    state_obj = None
    for state in storage.all("State").values():
        if state.id == id:
            state_obj = state

    return render_template(
        '9-states.html',
        state_obj=state_obj)


@app.teardown_appcontext
def tear_down(self):
    """After each request removes
    the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
