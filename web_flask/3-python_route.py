#!/usr/bin/python3
"""
Script that starts a Flask web application.
"""

from flask import Flask
from werkzeug.utils import escape

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """Display 'Hello HBNB!' when the root route is requested."""
    return "Hello HBNB!"


@app.route('/hbnb')
def display_hbnb():
    """Display 'HBNB' when the /hbnb route is requested."""
    return "HBNB"


@app.route('/c/<text>')
def display_c_text(text):
    """Display 'C <text>' when the /c/<text> is requested."""
    return "C {}".format(escape(text.replace('_', ' ')))


@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def display_python_text(text):
    """Display 'Python <text>' when the /python/<text> route is requested."""
    return "Python {}".format(escape(text.replace('_', ' ')))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')

