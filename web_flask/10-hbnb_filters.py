#!/usr/bin/python3
"""This project does the hbnb_filters"""

from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def teardown_context(exception):
    """This is the teardown function"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """This function handles routes trough hbnb_filters"""
    states = storage.all('State').values()
    amenities = storage.all('Amenity').values()
    cities = storage.all('City').values()
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities,
                           cities=cities)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
