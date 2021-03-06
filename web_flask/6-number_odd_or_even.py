#!/usr/bin/python3
from flask import Flask, render_template
"""
file five
"""

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb_only():
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def hbnb_custom(text):
    return ("C %s" % text.replace('_', ' '))


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text="is cool"):
    return ("Python %s" % text.replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    return ("%d is a number" % n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def displayPage_only_number(n):
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def even_or_odd(n):
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port=5000,
            )
