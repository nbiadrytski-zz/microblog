from flask import Flask

from config import Config


# app object as an instance of class Flask
app = Flask(__name__)
app.config.from_object(Config)


from app import routes