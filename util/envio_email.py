import smtplib # Importa a biblioteca para enviar e-mails.
from email.mime.text import MIMEText # Importa a classe para criar o corpo do email em texto.
from email.mime.multipart import MIMEMultipart # Importa a classe  e-mails com múltiplas partes (ex: textos e anexos).
from config import MAIL_USERNAME, MAIL_PASSWORD # Importa as credenciais de e-mail.

def enviar_email(destinatario, assunto, corpo):
    msg = MIMEMultipart() # cria o e-mail
    msg['FROM'] = MAIL_USERNAME # Define o remetente.
    msg['TO'] = destinatario # Define o destinatário.
    msg['Subject'] = assunto # Define o assunto do e-mail.

    msg.attach(MIMEText(corpo, 'plain')) # Anexa o corpo do e-mail.

    try:
        # Conecta ao servidor de e-mail e envia o e-mail.
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls() # Inicia a comunicação segura.
        servidor.login(MAIL_USERNAME, MAIL_PASSWORD) # Realiza o login.
        servidor.send_message(msg) # Envia a mensagem.
        servidor.quit() # Fecha a conexão
        return True # Retorna True se o e-mail for enviado.
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}") # Exibe erro no console.
        return False # Retorna False se houver erro.