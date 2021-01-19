#!usr/bin/python3
""" documentation """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    return "Hello HBNB!"

app.run(host="0.0.0.0", port=5000)
