#!/usr/bin/env python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
from flask_babel import Babel, request
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
    return render_template('2-index.html')


@babel.localeselector
def get_locale():
    '''determine the best match with our supported languages.'''
    user_languages = request.accept_languages.languages()
    # Find the first intersection between user preferences
    #  and supported languages
    for language in user_languages:
        if language in app.config['LANGUAGES']:
            return language
    # Default to the app's default locale if no match found
    return app.config['BABEL_DEFAULT_LOCALE']


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
