#!/usr/bin/python3
"""
Starts a Flask web application
Displays value of text variable in URL
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
def display_default(text):
    text = text.replace('_', ' ')
    return "Python {}".format(text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
