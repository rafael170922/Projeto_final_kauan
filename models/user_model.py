import sqlite3
from banco_dados.db import obter_conexao_db

class UserModel:
    @staticmethod
    def criar_usuario(username, password, email):
        conn = obter_conexao_db()
        try:
            conn.execute(
                'INSERT INTO users (username, password, email) VALUES (?, ?, ?)', 
                (username, password, email)
            )
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return None
        finally:
            conn.close()
    
    @staticmethod
    def buscar_por_username(username):
        conn = obter_conexao_db()
        usuario = conn.execute(
            'SELECT * FROM users WHERE username = ?', (username,)
        ).fetchone()
        conn.close()
        return usuario

    @staticmethod
    def buscar_por_email(email):
        conn = obter_conexao_db()
        usuario = conn.execute(
            'SELECT * FROM users WHERE email = ?', (email,)
        ).fetchone()
        conn.close()
        return usuario