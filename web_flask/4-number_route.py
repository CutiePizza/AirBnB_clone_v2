#!/usr/bin/python3
from flask import Flask
"""
file five
"""

app = Flask(__name__)


@app.route("/")
def hello_hbnb():
    return ("Hello HBNB!")


@app.route("/hbnb")
def hbnb_only():
    return ("HBNB")


@app.route("/c/<text>")
def hbnb_custom(text):
    return ("C %s" % text.replace('_', ' '))


@app.route("/python/")
@app.route("/python/<text>")
def python_route(text="is cool"):
    return ("Python %s" % text.replace('_', ' '))


@app.route("/number/<int:n>")
def is_number(n):
    return ("%d is a number" % n)


if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port=5000,
            )
