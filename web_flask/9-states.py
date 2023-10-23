#!/usr/bin/python3
"""This is the states and states by id"""

from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def teadown_context(exception):
    """This is the teardown function"""
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """This handles the states"""
    states = storage.all('State').values()
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id):
    """gets a state by it's id"""
    states = storage.all('State').values()
    for state in states:
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
