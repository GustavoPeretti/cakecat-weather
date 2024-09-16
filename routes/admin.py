from flask import Blueprint, render_template

admin = Blueprint('admin', __name__)

@admin.route('/')
def admin_handler():
    return render_template('admin.html')

@admin.route('/login')
def login():
    return render_template('login.html')
