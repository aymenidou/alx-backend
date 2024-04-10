#!/usr/bin/env python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
from flask_babel import Babel
babel = Babel()


class Config:
    '''Config class contain Babel configurations'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel.init_app(app)


@app.route('/', strict_slashes=False)
def index():
    """display a HTML page"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
