#!/usr/bin/python3
"""This script starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/states', strict_slashes=False)
def states_list():
    """Display a HTML page"""
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id):
    """Display a HTML page"""
    state = storage.get(State, id)
    if state:
        return render_template('9-states.html', state=state)
    return render_template('9-states.html', state=None)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')