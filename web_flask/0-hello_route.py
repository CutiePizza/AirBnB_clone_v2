#!/usr/bin/python3
from flask import Flask
"""
file oone
"""

app = Flask(__name__)


@app.route("/")
def hello_hbnb():
    return ("Hello HBNB!")

if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port=5000,
            )
