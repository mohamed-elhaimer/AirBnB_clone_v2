#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask
import urllib.parse

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
