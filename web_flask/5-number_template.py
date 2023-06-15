#!/usr/bin/python3
"""
Script that starts a Flask web application>
"""

from flask import Flask, render_template
from werkzeug.utils import escape

app = Flask(__name__)
app.url_map.strict_slashes=False

@app.route('/')
def hello_hbnb():
    """Display 'Hello HBNB' when the root route is requested."""
    return "Helo HBNB!"


@app.route('/hbnb')
def display_hbnb():
    """Display 'HBNB' when the /hbnb route is requested."""
    return "HBNB"


@app.route('/c/<text>')
def display_c_text(text):
    """Display 'C <text>' when the /c/<text> route is requested."""
    return "C {}".format(escape(text.replace('_', ' ')))


@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def display_python_text(text):
    """Display 'Python <text>' when the /python/<text> is requested."""
    return "Python {}".format(escape(text.replace('_', ' ')))


@app.route('/number/<int:n>')
def display_n_number(n):
    """Display '<n> is a number' if n is an integer."""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def display_html(n):
    """Display a HTML page only if n ia an integer."""
    return render_template('5-number.html', number=n)


if __name__ == "__main__":
    app.run(debug=True)

