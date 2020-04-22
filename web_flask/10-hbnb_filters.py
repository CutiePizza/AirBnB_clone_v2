#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models import State
from models import Amenity
"""
FILE 10
"""

app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """
    teardown handling
    """
    storage.close()



@app.route("/hbnb_filters", strict_slashes=False)
def hbnb():
    """
    state city amenity
    """
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', amenities=amenities, states=states)



if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port=5000,
            )
