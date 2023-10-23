#!/usr/bin/python3
"""This script is used to setup flask"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """This method handles states lists"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_context(exception):
    """This is the teadown function"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
