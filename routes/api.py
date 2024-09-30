from flask import Blueprint, request, jsonify
from .tempo import tempo
from .administrador import administrador
from .conceito import conceito

api = Blueprint('api', __name__)

api.register_blueprint(tempo, url_prefix='/tempo')
api.register_blueprint(administrador, url_prefix='/administrador')
api.register_blueprint(conceito, url_prefix='/conceito')
