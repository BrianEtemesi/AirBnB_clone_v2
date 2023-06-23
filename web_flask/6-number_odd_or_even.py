#!/usr/bin/python3
"""
Starts a Flask web application
Displays a HTML page if `n` is an integer
H1 tag shows whether number is even or odd
"""
from flask import Flask, render_template
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


@app.route('/number/<int:n>')
def is_number(n):
    return "{} is a number"


@app.route('/number_template/<int:n>')
def display_html(n):
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>')
def even_or_odd(n):
    if (n % 2) == 0:
        is_even = True
    else:
        is_even = False
    return render_template('6-number_odd_or_even.html',
                           number=n,
                           status=is_even)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)