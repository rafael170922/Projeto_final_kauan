from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from controllers.agendamento_controller import AgendamentoController
 
agendamento_bp = Blueprint('pedidos', __name__)
 
@agendamento_bp.route('/produtos', methods=['GET'])
@jwt_required()
def listar_horarios():
    return jsonify(AgendamentoController.listar_opcoes2())
 
@agendamento_bp.route('/fazer', methods=['POST'])
@jwt_required()
def fazer_agendamento():
    return jsonify(AgendamentoController.fazer_pedido(request.get_json()))