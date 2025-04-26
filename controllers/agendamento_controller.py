from flask_jwt_extended import get_jwt_identity
from models.agendamento_model import AgendamentoModel # Verifica se o modelo está correto para pedido.
 
class AgendamentoController:
    @staticmethod
    def listar_opcoes2():
        #Listar os produtos disponíveis para o pedido (nome e preço)
        horario = AgendamentoModel.listar_horarios() # Agora deve trazer apenas 'id', 'nome' e 'preço'.
        return {"horarios_disponiveis": horario}, 200
 
    @staticmethod
    def fazer_agendamento(dados):
        usuario_id = get_jwt_identity() # Obtém o ID do usuário a partir do JWT.
        produto_id = dados.get('produto_id') # Obtém o ID do produto do corpo da requisição.
        horario = dados.get('horario', 1) # Obtém a quantidade, default é 1 se não for passado.
 
        # Verificação para garantir que o produto_id e a quantidade sejam válidos
        if not produto_id or horario <= 0:
            return {"erro": "Produto e quantidade são obrigatórios"}, 400
       
        # Chama o modelo para criar o pedido.
        AgendamentoModel.criar_pedido(usuario_id, produto_id, horario)
        return {"mensagem": "Pedido realizado com sucesso"}, 201