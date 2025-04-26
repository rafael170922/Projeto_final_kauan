import sqlite3
from config import BANCO_DE_DADOS

def obter_conexao_db():
    conn = sqlite3.connect(BANCO_DE_DADOS)
    conn.row_factory = sqlite3.Row
    return conn

def criar_tabelas():
    conn = obter_conexao_db()
    cursor = conn.cursor()

    # Criando a tabela de usuários.
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
            )
        ''')
    
    # Criando a tebela de produtos
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL
            )
        ''')
    
    # Criando a tabela de pedidos coma coluna 'status'
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS pedidos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER,
            produto_id INTEGER,
            quantidade INTEGER,
            status TEXT DEFAULT 'pendente',
            FOREIGN KEY(usuario_id) REFERENCES users(id),
            FOREIGN KEY(produto_id) REFERENCES produtos(id)
            )
        ''')

    # Criando a tabela pagamentos
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS pagamentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER,
            tipo_pagamento TEXT NOT NULL,
            status_pagamento TEXT NOT NULL,
            FOREIGN KEY(usuario_id) REFERENCES users(id)
        )
    ''')

    horario_existem = cursor.execute('SELECT COUNT(*) FROM horario').fetchone()[0]
    if horario_existem == 0:
        cursor.executemany('''
            INSERT INTO horario (data, hora) VALUES (?, ?)
        ''', [
            ('25/04/25', '8:00'),
            ('26/04/25', '10:00'),
            ('27/04/25', '13:00')
        ])

    # Inserindo produtos iniciais caso a tabela esteja vazia.
    produtos_existem = cursor.execute('SELECT COUNT(*) FROM produtos').fetchone()[0]
    if produtos_existem == 0:
        cursor.executemany('''
            INSERT INTO produtos (nome, preco) VALUES (?, ?)
        ''', [
            ('corte', 40.00),
            ('Barba', 30.00),
            ('Combo', 60.00)
        ])
    
    conn.commit()
    conn.close()