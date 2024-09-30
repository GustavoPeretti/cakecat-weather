from flask import Blueprint, request, jsonify
from ..database.db import db

cidade = Blueprint('cidade', __name__)

@cidade.route('/<estado>', methods=['GET'])
def buscar_cidades(estado):
    try:
        resultado = db.query('SELECT * FROM cidades WHERE estado = %s ORDER BY cidade ASC;', estado)

        if len(resultado) == 0:
            return jsonify({'status': False, 'mensagem': 'Nenhum recurso não foi encontrado.'}), 404
    except:
        return jsonify({'status': False, 'mensagem': 'Houve um erro ao processar os dados.'}), 500

    return jsonify({'status': True, 'resultado': resultado}), 200
