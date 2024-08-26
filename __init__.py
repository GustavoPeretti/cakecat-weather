from flask import Flask
from .routes.home import home
from .routes.admin import admin
from .routes.tempo import tempo

app = Flask(__name__)

app.register_blueprint(home)
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(tempo, url_prefix='/tempo')
