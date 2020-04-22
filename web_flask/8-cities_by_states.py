#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
"""
FILE 8
"""

app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """
    teardown handling
    """
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def all_citiess():
    """
    all cities
    """
    all_states = storage.all("State")
    my_list = all_states.values()
    return render_template('8-cities_by_states.html', my_list=my_list)


if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port=5000,
            )
