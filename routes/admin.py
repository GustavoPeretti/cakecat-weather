from flask import Blueprint, render_template, request, session, redirect, url_for, jsonify
from ..database.db import db

admin = Blueprint('admin', __name__)

@admin.route('/')
def admin_handler():
    if 'usuario' not in session:
        return redirect(url_for('admin.login'))

    return render_template('admin.html')

@admin.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    dados = request.json

    if ('usuario' not in dados) or ('senha' not in dados):
        return jsonify({'status': False, 'mensagem': f'Parâmetro obrigatório sem argumento.'}), 400
    
    resultado = db.query('SELECT usuario FROM administradores WHERE usuario = %s AND senha = SHA2(%s, 256);', dados['usuario'], dados['senha'])

    if not resultado:
        return jsonify({'status': False, 'mensagem': f'Usuário não cadastrado ou senha errada.'}), 401
    
    session['usuario'] = dados['usuario']

    return redirect(url_for('admin.admin_handler'))
