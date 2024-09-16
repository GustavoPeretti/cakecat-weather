from flask import Flask
from .routes.home import home
from .routes.admin import admin
from .routes.tempo import tempo
import os

app = Flask(__name__)

app.register_blueprint(home)
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(tempo, url_prefix='/tempo')

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
