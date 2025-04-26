from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from controllers.confirmacao_pedido_controller import ConfirmacaoPedidoController

confirmacao_pedido_bp = Blueprint('confirmacao_pedido', __name__)

@confirmacao_pedido_bp.route('/confirmar', methods=['POST'])
@jwt_required() # Exige que o usuário esteja autenticado.
def confirmar_pedido():
    dados = request.get_json()

    # A requisição agora só precisa ter a confirmação "sim".
    confirmacao = dados.get('confirmacao') # Obtém o valor  "confirmação" da requisição.

    if not confirmacao or confirmacao != "sim":
        return {"erro": "Confirmação inválida. Envie {'confirmacao: 'sim'}."}, 400
    
    usuario_id = get_jwt_identity() # Obtém o ID do usuário autenticado.

    # Passa a confirmação e o ID do usuário para o controlador confirmar o pedido.
    return ConfirmacaoPedidoController.confirmar_pedido(usuario_id)