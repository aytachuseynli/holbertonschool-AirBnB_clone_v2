#!/usr/bin/python3
""" Script that starts a Flask web application """

from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Displays a HTML page with all the states sorted by name"""
    states = storage.all("State").values()
    sorted_states = sorted(states, key=lambda x: x.name)
    return render_template("7-states_list.html", states=sorted_states)


@app.teardown_appcontext
def tear(exception):
    """Close the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
