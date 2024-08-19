from flask import Flask
from .routes.home import home

app = Flask(__name__)

app.register_blueprint(home)
