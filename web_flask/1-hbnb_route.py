#!/usr/bin/python3
"""
Script that starts a Flask web application.
"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes=False


@app.route('/')
def hello_hbnb():
    """Display 'Hello HBNB!' when the root route is requested."""
    return "Hello HBNB!"

@app.route('/hbnb')
def display_hbnb():
   """Displays 'HBNB' when the /hbnb route is requested."""
   return "HBNB"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')

