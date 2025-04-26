from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from controllers.agendamento_controller import PedidoController

horarios_bp = Blueprint('pedidos', __name__)

@horarios_bp.route('/listar', methods=['GET'])
@jwt_required()
def listar_horarios():
    return jsonify(PedidoController.listar_opcoes2())