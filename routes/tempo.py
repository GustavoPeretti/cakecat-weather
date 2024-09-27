from flask import Blueprint, request, jsonify
from ..database.db import db
import datetime

tempo = Blueprint('tempo', __name__)

@tempo.route('/<cidade>/<data>', methods=['GET'])
def buscar_tempo(cidade, data):
    try:
        resultado = db.query('SELECT * FROM tempo WHERE cep = %s AND data_tempo = %s;', cidade, data)

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
        tempos_cadastrados = db.query('SELECT cep FROM tempo WHERE cep = %s AND data_tempo = %s;', dados['cep'], dados['data'])
    except:
        return jsonify({'status': False, 'mensagem': 'Não foi possível processar os dados.'}), 400

    if tempos_cadastrados:
        return jsonify({'status': False, 'mensagem': 'Conflito com recurso já existente.'}), 409

    try:
        cidade = db.query('SELECT cep FROM cidades WHERE cep = %s;', dados['cep'])
    except:
        return jsonify({'status': False, 'mensagem': 'Não foi possível processar os dados.'}), 400
    
    if not cidade:
        return jsonify({'status': False, 'mensagem': f'O CEP "{dados['cep']} não está vinculado a nenhuma cidade.".'}), 400

    try:
        db.query(
            'INSERT INTO tempo VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);',
            dados['cep'],
            dados['data'],
            'admin1',
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

@tempo.route('/<cidade>/<data>', methods=['PUT'])
def atualizar_tempo(cidade, data):
    pass

@tempo.route('/<cidade>/<data>', methods=['DELETE'])
def deletar_tempo(cidade, data):
    pass
