from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from controllers.pagamento_controller import PagamentoController

pagamento_bp= Blueprint('pagamentos', __name__)

@pagamento_bp.route('/me', methods=['POST'])
@jwt_required() # Requer que o usuário esteja autenticado.
def cadastrar_pagamento():
    dados = request.get_json()
    usuario_id = get_jwt_identity() # Obtém o ID do usuário autenticado.
    return PagamentoController.adicionar_pagamento() # Alterado para chamar o método correto.