#!/usr/bin/env python3
"""
starts a Flask web application
"""

from flask import Flask, render_template, request
from flask_babel import Babel, gettext
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
    # home_title = gettext('3-index.html')
    # home_header = gettext('3-index.html')
    return render_template('3-index.html')


@babel.localeselector
def get_locale():
    '''determine the best match with our supported languages.'''
    user_languages = request.accept_languages.best_match(
        app.config['LANGUAGES'])
    return user_languages


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
