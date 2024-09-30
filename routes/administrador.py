from flask import Blueprint, request, jsonify, session
from ..database.db import db

administrador = Blueprint('administrador', __name__)

@administrador.route('/', methods=['GET'])
def buscar_administradores():
    if 'usuario' not in session:
        return jsonify({'status': False, 'mensagem': 'Não autorizado.'}), 401
    
    try:
        resultado = db.query('SELECT usuario FROM administradores;')

        if len(resultado) == 0:
            return jsonify({'status': False, 'mensagem': 'Nenhum recurso não foi encontrado.'}), 404
    except:
        return jsonify({'status': False, 'mensagem': 'Houve um erro ao processar os dados.'}), 500

    return jsonify({'status': True, 'resultado': resultado}), 200

@administrador.route('/', methods=['POST'])
def cadastrar_administrador():
    if 'usuario' not in session:
        return jsonify({'status': False, 'mensagem': 'Não autorizado.'}), 401
    
    dados = request.json

    parametros = [
        'usuario',
        'senha'
    ]

    for parametro in parametros:
        if parametro not in dados:
            return jsonify({'status': False, 'mensagem': f'Parâmetro {parametro} sem argumento.'}), 400
    
    try:
        administradores_cadastrados = db.query('SELECT usuario FROM administradores WHERE usuario = %s;', dados['usuario'])
    except:
        return jsonify({'status': False, 'mensagem': 'Não foi possível processar os dados.'}), 400

    if administradores_cadastrados:
        return jsonify({'status': False, 'mensagem': 'Conflito com recurso já existente.'}), 409

    try:
        db.query(
            'INSERT INTO administradores VALUES (%s, SHA2(%s, 256));',
            dados['usuario'],
            dados['senha']
        )
    except:
        return jsonify({'status': False, 'mensagem': 'Não foi possível processar os dados3.'}), 400
    
    return jsonify({'status': True, 'mensagem': 'Recurso criado.'}), 201

@administrador.route('/<usuario>', methods=['PUT'])
def atualizar_administrador(usuario):
    if 'usuario' not in session:
        return jsonify({'status': False, 'mensagem': 'Não autorizado.'}), 401
    
    dados = request.json

    try:
        resultado = db.query('SELECT usuario FROM administradores WHERE usuario = %s;', usuario)

        if len(resultado) == 0:
            return jsonify({'status': False, 'mensagem': 'Recurso não foi encontrado.'}), 404
    except:
        return jsonify({'status': False, 'mensagem': 'Não foi possível processar os dados.'}), 400
    
    parametros = [
        'usuario',
        'senha'
    ]

    parametros = [parametro for parametro in parametros if parametro in dados]

    if not parametros:
        return jsonify({'status': False, 'mensagem': f'Nenhum argumento foi especificado.'}), 400
    
    try:
        for parametro in parametros:
            db.query(f'UPDATE administradores SET {parametro} = %s WHERE usuario = %s;', dados[parametro], usuario)
    except:
        return jsonify({'status': False, 'mensagem': 'Não foi possível processar os dados.'}), 400
    
    return jsonify({'status': True, 'mensagem': 'Recurso atualizado.'}), 200

@administrador.route('/<usuario>', methods=['DELETE'])
def deletar_tempo(usuario):
    if 'usuario' not in session:
        return jsonify({'status': False, 'mensagem': 'Não autorizado.'}), 401
    
    try:
        resultado = db.query('SELECT * FROM administradores WHERE usuario = %s;', usuario)

        if len(resultado) == 0:
            return jsonify({'status': False, 'mensagem': 'Recurso não foi encontrado.'}), 404
    except:
        return jsonify({'status': False, 'mensagem': 'Não foi possível processar os dados.'}), 400
    
    try:
        db.query('DELETE FROM administradores WHERE usuario = %s;', usuario)
    except:
        return jsonify({'status': False, 'mensagem': 'Não foi possível processar os dados.'}), 400

    return jsonify({'status': True, 'mensagem': 'Recurso deletado.'}), 200