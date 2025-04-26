from flask import request
from models.pagamento_model import PagamentoModel
from flask_jwt_extended import jwt_required, get_jwt_identity

class PagamentoController:
    
    @staticmethod
    @jwt_required()
    def adicionar_pagamento():
        #Obtendo o ID do usuário autenticado
        usuario_id = get_jwt_identity()

        # Dados do pagamento que vem da requisição
        dados = request.get_json()
        tipo_pagamento = dados.get('tipo_pagamento') # Exemplo: Crédito ou Débito

        #Verificando se o tipo de pagamento foi informado corretamente.
        if not tipo_pagamento:
            return {"erro": "Tipo de pagamento é obrigatório"}, 400
        
        if tipo_pagamento not in ['Credito', 'Debito']:
            return {"erro": "Tipo de pagamento inválido. Escola entre 'Credito' ou 'Debito'."}, 400
        
        # Adicionando o pagamento com o tipo de pagamento.
        PagamentoModel.adicionar_pagamento(usuario_id, tipo_pagamento)

        return {"mensagem": f"Pagamento registrado como {tipo_pagamento}"}, 201