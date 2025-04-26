import sqlite3
from config import BANCO_DE_DADOS

class PagamentoModel:
    @staticmethod
    def adicionar_pagamento(usuario_id, tipo_pagamento):
        conn = sqlite3.connect(BANCO_DE_DADOS)
        cursor = conn.cursor()

        # Verificando se tipo_pagamento é válido
        if tipo_pagamento not in ['Credito', 'Debito']:
            return None
        
        # Registrando a forma de pagamento com status 'pendente'
        cursor.execute('''
            INSERT INTO pagamentos (usuario_id, tipo_pagamento, status_pagamento)
            VALUES (?, ?, ?)
        ''', (usuario_id, tipo_pagamento, 'pendente'))

        conn.commit()
        conn.close()

    @staticmethod
    def finalizar_pagamento(pagamento_id):
        conn = sqlite3.connect(BANCO_DE_DADOS)
        cursor = conn.cursor()

        #Atualizando o pagamento para 'realizado' quando o pedido for entregue
        cursor.execute('''
            UPDATE pagamentos SET status_pagamento = ? Where id = ?
        ''', ('realizado', pagamento_id))

        conn.commit()
        conn.close()

    @staticmethod
    def buscar_pagamento_por_usuario(usuario_id):
        conn = sqlite3.connect(BANCO_DE_DADOS)
        cursor = conn.cursor()

        cursor.execute('''
            SELECT * FROM pagamentos WHERE usuario_id = ? ORDER BY id DESC LIMIT 1
        ''', (usuario_id,))
        pagamento = cursor.fetchone()

        conn.close()
        return pagamento