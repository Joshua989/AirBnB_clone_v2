#!/usr/bin/python3
""" Script that begins a Flask web app """
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ print web """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ print web """
    return 'HBNB'


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
