"""A class to store configuration variables."""

import os


class Config:
    # Flask and some of its extensions use the value of the secret key as a cryptographic key,
    # useful to generate signatures or tokens.
    # Flask-WTF extension uses it to protect web forms against CSRF attack
    # The value of the secret key is set as an expression with two terms:
    # 1st looks for the value of an environment variable SECRET_KEY (preferred),
    # if environment doesn't define the variable, then the hardcoded string is used instead.
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
