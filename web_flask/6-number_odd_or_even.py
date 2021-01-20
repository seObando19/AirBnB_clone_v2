#!/usr/bin/python3
"""
script that starts a Flask web application:
Your web application must be listening on 0.0.0.0,
port 5000

Routes:
    */: display “Hello HBNB!”
    */hbnb: display “HBNB”
    */c/<text>: display “C ”,
        followed by the value of the text variable
        (replace underscore _ symbols with a space )
    */python/(<text>): display “Python ”,
        followed by the value of the text variable
        (replace underscore _ symbols with a space )
            -The default value of text is “is cool”
    */number/<n>: display “n is a number” only if n
        is an integer
    */number_template/<n>: display a HTML page only
        if n is an integer:
        -H1 tag: “Number: n” inside the tag BODY
    */number_odd_or_even/<n>: display a HTML page only
        if n is an integer:
        -H1 tag: “Number: n is even|odd” inside the tag BODY
"""

from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB1():
    """Print hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def only_HBNB():
    """Print HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def printText(text):
    """Print letter C and the variable text"""
    text = text.replace('_', ' ')
    return "C %s" % escape(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def printTextPython(text="is cool"):
    """Print word Python and the variable text"""
    text = text.replace('_', ' ')
    return "Python %s" % escape(text)


@app.route('/number/<int:n>', strict_slashes=False)
def isNumber(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def showTemplate(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def oddAndEven(n):
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
