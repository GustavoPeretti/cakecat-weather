from flask import Blueprint, request, jsonify
from ..database.db import db

cidade = Blueprint('cidade', __name__)