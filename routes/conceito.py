from flask import Blueprint, request, jsonify, session
from ..database.db import db

conceito = Blueprint('conceito', __name__)

@conceito.route('/<titulo>', methods=['GET'])
def buscar_conceito(titulo):
    if 'usuario' not in session:
        return jsonify({'status': False, 'mensagem': 'Não autorizado.'}), 401

    try:
        resultado = db.query('SELECT * FROM conceitos WHERE titulo = %s;', titulo)

        if len(resultado) == 0:
            return jsonify({'status': False, 'mensagem': 'Recurso não foi encontrado.'}), 404
        
        resultado = resultado[0]
    except:
        return jsonify({'status': False, 'mensagem': 'Não foi possível processar os dados.'}), 400

    return jsonify({'status': True, 'resultado': resultado}), 200

@conceito.route('/', methods=['GET'])
def buscar_conceitos():
    if 'usuario' not in session:
        return jsonify({'status': False, 'mensagem': 'Não autorizado.'}), 401
    
    try:
        resultado = db.query('SELECT titulo, descricao, cor FROM conceitos;')

        if len(resultado) == 0:
            return jsonify({'status': False, 'mensagem': 'Nenhum recurso não foi encontrado.'}), 404
    except:
        return jsonify({'status': False, 'mensagem': 'Houve um erro ao processar os dados.'}), 500

    return jsonify({'status': True, 'resultado': resultado}), 200

@conceito.route('/', methods=['POST'])
def cadastrar_conceito():
    if 'usuario' not in session:
        return jsonify({'status': False, 'mensagem': 'Não autorizado.'}), 401
    
    dados = request.json

    parametros = [
        'titulo',
        'descricao',
        'cor'
    ]

    for parametro in parametros:
        if parametro not in dados:
            return jsonify({'status': False, 'mensagem': f'Parâmetro {parametro} sem argumento.'}), 400
    
    try:
        conceitos_cadastrados = db.query('SELECT titulo FROM conceitos WHERE titulo = %s;', dados['titulo'])
    except:
        return jsonify({'status': False, 'mensagem': 'Não foi possível processar os dados.'}), 400

    if conceitos_cadastrados:
        return jsonify({'status': False, 'mensagem': 'Conflito com recurso já existente.'}), 409

    try:
        db.query(
            'INSERT INTO conceitos VALUES (%s, %s, %s, %s);',
            dados['titulo'],
            'admin1',
            dados['descricao'],
            dados['cor']
        )
    except:
        return jsonify({'status': False, 'mensagem': 'Não foi possível processar os dados3.'}), 400
    
    return jsonify({'status': True, 'mensagem': 'Recurso criado.'}), 201

@conceito.route('/<titulo>', methods=['PUT'])
def atualizar_conceito(titulo):
    if 'usuario' not in session:
        return jsonify({'status': False, 'mensagem': 'Não autorizado.'}), 401
    
    dados = request.json

    try:
        resultado = db.query('SELECT titulo FROM conceitos WHERE titulo = %s;', titulo)

        if len(resultado) == 0:
            return jsonify({'status': False, 'mensagem': 'Recurso não foi encontrado.'}), 404
    except:
        return jsonify({'status': False, 'mensagem': 'Não foi possível processar os dados.'}), 400
    
    parametros = [
        'titulo',
        'descricao',
        'cor'
    ]

    parametros = [parametro for parametro in parametros if parametro in dados]

    if not parametros:
        return jsonify({'status': False, 'mensagem': f'Nenhum argumento foi especificado.'}), 400
    
    try:
        for parametro in parametros:
            db.query(f'UPDATE conceitos SET {parametro} = %s WHERE titulo = %s;', dados[parametro], titulo)
    except:
        return jsonify({'status': False, 'mensagem': 'Não foi possível processar os dados.'}), 400
    
    return jsonify({'status': True, 'mensagem': 'Recurso atualizado.'}), 200

@conceito.route('/<titulo>', methods=['DELETE'])
def deletar_conceito(titulo):
    if 'usuario' not in session:
        return jsonify({'status': False, 'mensagem': 'Não autorizado.'}), 401
    
    try:
        resultado = db.query('SELECT * FROM conceitos WHERE titulo = %s;', titulo)

        if len(resultado) == 0:
            return jsonify({'status': False, 'mensagem': 'Recurso não foi encontrado.'}), 404
    except:
        return jsonify({'status': False, 'mensagem': 'Não foi possível processar os dados.'}), 400
    
    try:
        db.query('DELETE FROM conceitos WHERE titulo = %s;', titulo)
    except:
        return jsonify({'status': False, 'mensagem': 'Não foi possível processar os dados.'}), 400

    return jsonify({'status': True, 'mensagem': 'Recurso deletado.'}), 200