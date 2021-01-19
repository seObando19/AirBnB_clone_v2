#!/usr/bin/python3
""" documentation"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB1():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def only_HBNB():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def printText(text):
    text = text.replace('_', ' ')
    return "C %s" % escape(text)


@app.route('/python/(<text>)', strict_slashes=False)
def printTextPython(text="is cool"):
    text = text.replace('_', ' ')
    return "Python %s" % escape(text)

app.run(host="0.0.0.0", port=5000)
