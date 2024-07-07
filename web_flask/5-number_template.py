#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask
import urllib.parse
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """hello hbnb"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello():
    """hello hbnb"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def print_text(text):
    """print text"""
    text = urllib.parse.unquote(text)
    text_with_space = text.replace("_", " ")
    return f"C {text_with_space}"


@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def print_py(text):
    """print text"""
    temp = text.replace("_", " ")
    return f"Python {temp}"


@app.route("/number/<int:n>", strict_slashes=False)
def imanumber(n):
    """display “n is a number” only if n is an integer"""
    return "{:d} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def rendertemplate(n):
    """display html if passed a int"""
    return render_template("5-number.html", num=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
