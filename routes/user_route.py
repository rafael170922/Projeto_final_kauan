from flask import Blueprint, request, jsonify
from controllers.user_controller import UserController

user_bp = Blueprint('/users', __name__)

# Rota para registrart um novo Usuário.
@user_bp.route('/register', methods=['POST'])
def register():
    return jsonify(UserController.registrar_usuario(request.get_json()))

# Rota para fazer login de um usuário.
@user_bp.route('/login', methods=['POST'])
def login():
    return jsonify(UserController.logar_usuario(request.get_json()))