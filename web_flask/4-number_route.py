#!/usr/bin/python3
"""
Starts a Flask web application
Displays `n is a number` if n is an integer
"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_alx():
    return "Hello HBNB!"


@app.route('/hbnb')
def alx():
    return "HBNB"


@app.route('/c/<text>')
def display_text(text):
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def default_text(text):
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<n>')
def is_number(n):
    n = int(n)
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
