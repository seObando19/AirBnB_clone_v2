#!/usr/bin/python3
""" documentation """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB1():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def only_HBNB():
    return "HBNB"

app.run(host="0.0.0.0", port=5000)
