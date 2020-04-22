#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models import State
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


@app.route("/states", strict_slashes=False)
def all_states():
    """
    all states
    """
    all_states = storage.all(State)
    my_list = all_states.values()
    return render_template('7-states_list.html', my_list=my_list)


@app.route("/states/<id>", strict_slashes=False)
def all_citiess(id):
    """
    all cities
    """
    ok = None
    all_states = storage.all(State)
    my_list = all_states.values()
    for i in my_list:
        if id == i.id:
            ok = i
            break
    return render_template('9-states.html', my_list=ok)


if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port=5000,
            )
