import re # Trabalha com a expressões regulares ( ex: validar, e-mail)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from models.user_model import UserModel
from util.envio_email import enviar_email

def senha_forte(senha):
    """ Valida se a senha é forte"""
    if (len(senha) >= 8 and
        re.search(r"[A-Z]", senha) and
        re.search(r"[a-z]", senha) and
        re.search(r"[0-9]", senha) and
        re.search(r"[!@#$%^&*()<>?\":{}|<>]", senha)):
        return True
    return False

class UserController:
    @staticmethod
    def registrar_usuario(dados):
        username = dados.get('username')
        password = dados.get('password')
        email = dados.get('email')

        if not username or not password or not email:
            return {"erro": "Nome de usuário, senha e e-mail são obrigatórios"}, 400
        
        if not senha_forte(password):
            return {
                "erro": "A senha deve conter pelo menos 8 caracteres, incluindo letras maiúsculas, minúsculas, números e caracteres especiais."
            }, 400
        
        if UserModel.buscar_por_username(username):
            return {"erro": "Nome de usuário ja existe"}, 400
        
        if UserModel.buscar_por_email(email):
            return {"erro": "Email ja cadastrado"}, 400
        
        senha_hash = generate_password_hash(password)

        if UserModel.criar_usuario(username, senha_hash, email):
            corpo_email = f"""
            Olá {username}!

            Parabéns, seu cadastro foi realizado com sucesso!
            Agora você ja pode acessar sua conta normalmente.

            Bem-vindo(a)!

            Atenciosamente,
            BugBurger
            """
            enviar_email(email, "Cadastro realizado com sucesso!", corpo_email)
            
            return {"mensagem": "Usuario registrado com sucesso"}, 201
        return {"erro": "Erro ao registrar usuário"}, 400

    @staticmethod
    def logar_usuario(dados):
        username = dados.get('username')
        password = dados.get('password')

        if not username or not password:
            return {"erro": "Nome de usuário e senha são obrigatórios"}, 400
            
        usuario = UserModel.buscar_por_username(username)
        if usuario and check_password_hash(usuario['password'], password):
            token = create_access_token(identity=str(usuario['id']))

            corpo_email = f"""
            Olá {username}!

            Seu login foi realizado com sucesso.
            Se não foi você quem acessou, por favor, entre em contato com nossa equipe imediatamente.

            Atenciosamente,
            BugBurguer
            """

            enviar_email(usuario['email'], "Login realizado com sucesso", corpo_email)

            return {"access_token": token}, 200
        return {"erro": "Nome de usuário ou senha inválidos"}, 40