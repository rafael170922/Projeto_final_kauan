from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from controllers.horario_controller import EnderecoController

endereco_bp = Blueprint('enderecos', __name__)

@endereco_bp.route('/me', methods=['POST'])
@jwt_required() # Requer que o usuário esteja autenticado.
def adicionar_endereco():
    dados = request.get_json()
    usuario_id = get_jwt_identity() # Obtem o ID do usuário autenticado.
    return EnderecoController.adicionar_endereco() # Chama a função do controlador.