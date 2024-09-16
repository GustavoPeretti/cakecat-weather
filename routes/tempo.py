from flask import Blueprint, render_template

tempo = Blueprint('tempo', __name__)

@tempo.route('/', methods=['GET'])
def buscar_todos_tempos():
    pass

@tempo.route('/<int:data>', methods=['GET'])
def buscar_tempo():
    pass

@tempo.route('/', methods=['POST'])
def cadastrar_tempo():
    pass

@tempo.route('/', methods=['PUT'])
def atualizar_tempo():
    pass

@tempo.route('/', methods=['DELETE'])
def deletar_tempo():
    pass
