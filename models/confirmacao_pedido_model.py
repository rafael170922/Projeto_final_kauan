import sqlite3
from config import BANCO_DE_DADOS

class ConfirmacaoPedidoModel:

    @staticmethod
    def confirmar_pedido(usuario_id):
        conn = sqlite3.connect(BANCO_DE_DADOS)
        cursor = conn.cursor()

        # Verificando o pedido mais recente do usuário.
        cursor.execute('''SELECT p.id, p.usuario_id, u.email, p.produto_id, p.quantidade, p.status, pr.nome, pr.preco
                          FROM pedidos p
                          JOIN users u ON p.usuario_id = u.id
                          JOIN produtos pr ON p.produto_id = pr.id
                          WHERE p.usuario_id = ? AND p.status != 'confirmado'
                          ORDER BY p.id DESC LIMIT 1''', (usuario_id,))
        pedido = cursor.fetchone()

        print(f"Pedido retornado: {pedido}") # Adicionando o print para verificar o pedido retornado

        if not pedido:
            print(f"Pedido não encontrado para o usuario_id {usuario_id}")
            conn.clone()
            return None
        
        # Atualizando o status do pedido para "confirmado".
        cursor.execute('''UPDATE pedidos SET status = ? WHERE id = ?''', ('confirmado', pedido[0]))

        # Detalhando os produtos do pedido
        produtos = f"{pedido[6]} (ID: {pedido[3]})" # Nome do produto
        quantidade = pedido[4] # Quantidade do produto
        total = pedido[7] * quantidade #Preço unitário * quantidade

        # Criando um dicionário com as informações necessárias para o e-mail
        pedido_detalhado = {
            "usuario_email": pedido[2], # E-mail do usuário
            "produtos": produtos,
            "quantidade": quantidade, # Quantidade de cada produto.
            "total": total
        }

        conn.commit()
        conn.close()

        return pedido_detalhado