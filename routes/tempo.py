from flask import Blueprint, request, jsonify, session
from ..database.db import db

tempo = Blueprint('tempo', __name__)

@tempo.route('/<cep>/<data>', methods=['GET'])
def buscar_tempo(cep, data):
    try:
        resultado = db.query('SELECT * FROM tempos WHERE cep = %s AND data_tempo = %s;', cep, data)

        if len(resultado) == 0:
            return jsonify({'status': False, 'mensagem': 'Recurso não foi encontrado.'}), 404
        
        resultado = resultado[0]
        
        resultado['data'] = resultado['data_tempo'].isoformat()
        del resultado['data_tempo']
        resultado['inicio_sol'] = str(resultado['inicio_sol'])
        resultado['fim_sol'] = str(resultado['fim_sol'])
        del resultado['administrador']
    except:
        return jsonify({'status': False, 'mensagem': 'Não foi possível processar os dados.'}), 400

    return jsonify({'status': True, 'resultado': resultado}), 200

@tempo.route('/', methods=['POST'])
def cadastrar_tempo():
    if 'usuario' not in session:
        return jsonify({'status': False, 'mensagem': 'Não autorizado.'}), 401

    dados = request.json

    parametros = [
        'cep',
        'data',
        'condicao',
        'maxima',
        'minima',
        'chuva',
        'vento',
        'umidade',
        'arco_iris',
        'inicio_sol',
        'fim_sol',
        'lua'
    ]

    for parametro in parametros:
        if parametro not in dados:
            return jsonify({'status': False, 'mensagem': f'Parâmetro {parametro} sem argumento.'}), 400
    
    try:
        tempos_cadastrados = db.query('SELECT cep FROM tempos WHERE cep = %s AND data_tempo = %s;', dados['cep'], dados['data'])
    except:
        return jsonify({'status': False, 'mensagem': 'Não foi possível processar os dados.'}), 400

    if tempos_cadastrados:
        return jsonify({'status': False, 'mensagem': 'Conflito com recurso já existente.'}), 409

    try:
        cidade = db.query('SELECT cep FROM cidades WHERE cep = %s;', dados['cep'])
    except:
        return jsonify({'status': False, 'mensagem': 'Não foi possível processar os dados.'}), 400
    
    if not cidade:
        return jsonify({'status': False, 'mensagem': f'O CEP "{dados['cep']}" não está vinculado a nenhuma cidade.".'}), 400

    try:
        db.query(
            'INSERT INTO tempos VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);',
            dados['cep'],
            dados['data'],
            session['usuario'],
            dados['condicao'],
            dados['maxima'],
            dados['minima'],
            dados['chuva'],
            dados['vento'],
            dados['umidade'],
            dados['arco_iris'],
            dados['inicio_sol'],
            dados['fim_sol'],
            dados['lua']
        )
    except:
        return jsonify({'status': False, 'mensagem': 'Não foi possível processar os dados.'}), 400
    
    return jsonify({'status': True, 'mensagem': 'Recurso criado.'}), 201

@tempo.route('/<cep>/<data>', methods=['PUT'])
def atualizar_tempo(cep, data):
    if 'usuario' not in session:
        return jsonify({'status': False, 'mensagem': 'Não autorizado.'}), 401

    dados = request.json

    try:
        resultado = db.query('SELECT cep FROM tempos WHERE cep = %s AND data_tempo = %s;', cep, data)

        if len(resultado) == 0:
            return jsonify({'status': False, 'mensagem': 'Recurso não foi encontrado.'}), 404
    except:
        return jsonify({'status': False, 'mensagem': 'Não foi possível processar os dados.'}), 400
    
    parametros = [
        'condicao',
        'maxima',
        'minima',
        'chuva',
        'vento',
        'umidade',
        'arco_iris',
        'inicio_sol',
        'fim_sol',
        'lua'
    ]

    parametros = [parametro for parametro in parametros if parametro in dados]

    if not parametros:
        return jsonify({'status': False, 'mensagem': f'Nenhum argumento foi especificado.'}), 400
    
    try:
        for parametro in parametros:
            db.query(f'UPDATE tempos SET {parametro} = %s WHERE cep = %s AND data_tempo = %s;', dados[parametro], cep, data)
    except:
        return jsonify({'status': False, 'mensagem': 'Não foi possível processar os dados.'}), 400
    
    return jsonify({'status': True, 'mensagem': 'Recurso atualizado.'}), 200

@tempo.route('/<cep>/<data>', methods=['DELETE'])
def deletar_tempo(cep, data):
    if 'usuario' not in session:
        return jsonify({'status': False, 'mensagem': 'Não autorizado.'}), 401
    
    try:
        resultado = db.query('SELECT * FROM tempos WHERE cep = %s AND data_tempo = %s;', cep, data)

        if len(resultado) == 0:
            return jsonify({'status': False, 'mensagem': 'Recurso não foi encontrado.'}), 404
    except:
        return jsonify({'status': False, 'mensagem': 'Não foi possível processar os dados.'}), 400
    
    try:
        db.query('DELETE FROM tempos WHERE cep = %s AND data_tempo = %s;', cep, data)
    except:
        return jsonify({'status': False, 'mensagem': 'Não foi possível processar os dados.'}), 400

    return jsonify({'status': True, 'mensagem': 'Recurso deletado.'}), 200