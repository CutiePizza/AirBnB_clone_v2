#!/usr/bin/python3
"""
File 7
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """
    teardown handling
    """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def all_states():
    """
    all states
    """
    all_states = storage.all()
    my_list = all_states.values()
    return render_template('7-states_list.html', my_list=my_list)


if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port=5000,
            )
