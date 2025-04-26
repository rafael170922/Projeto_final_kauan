import sqlite3
from config import BANCO_DE_DADOS
 
def obter_conexao_db():
    conn = sqlite3.connect(BANCO_DE_DADOS)
    conn.row_factory = sqlite3.Row
    return conn
 
class PedidoModel:
    @staticmethod
    def listar_horarios():
        #Obtém todos os produtos disponíveis no banco de dados.
        conn = obter_conexao_db()
        cursor = conn.cursor()
        cursor.execute('SELECT id, nome, preco FROM horario') # Apenas id, nome, preço.
        produtos = cursor.fetchall()
        conn.close()
        return [dict(horario) for horario in produtos]
 
    @staticmethod
    def criar_agendamento(usuario_id, produto_id, horario):
        #Insere o pedido no banco de dados.
        conn = obter_conexao_db()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO pedidos (usuario_id, produto_id, horario)
            VALUES (?, ?, ?)
        ''', (usuario_id, produto_id, horario))
        conn.commit()
        conn.close()