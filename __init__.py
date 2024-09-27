from flask import Flask
from .routes.home import home
from .routes.admin import admin
from .routes.api import api

app = Flask(__name__)

app.register_blueprint(home)
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(api, url_prefix='/api')
