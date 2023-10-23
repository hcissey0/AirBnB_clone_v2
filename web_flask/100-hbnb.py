#!/usr/bin/python3
"""This is the hbnb flask static"""

from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def teardown_context(exception):
    """This is the teardown function"""
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """This is the hbnb route handler"""
    states = storage.all('State').values()
    amenities = storage.all('Amenity').values()
    places = storage.all('Place').values()
    cities = storage.all('City').values()
    return render_template('100-hbnb.html',
                           states=states, amenities=amenities,
                           places=places, cities=cities)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
