SECRET_KEY = 'your-secret-key' # Definindo uma chave secreta para a aplicação (essencial para criptografia e sessões).
JWT_SECRET_KEY = SECRET_KEY  # Usando a mesma chave secreta para assinar os tokens JWT (JSON Web Token).
BANCO_DE_DADOS = 'users.db' # Definindo o nome do banco de dados SQLite.

# Confirmação de email para envio.
MAIL_SERVER = 'SMTP.GMAIL.COM' #Servidor SMTP do gmail para envio de e-mails.
MAIL_PORT = 587 # Porta para envio de e-mail com TLS ( Transport layer Security).
MAIL_USERNAME = 'rafaelsl170922@gmail.com' # Endereço de e-mail para enviar os e-mails (substitua pelo seu e-mail).
MAIL_PASSWORD = 'fuon mtoc hkro nibp' # Senha do aplicativo do Gmail ( gerada nas configurações de segurança).
MAIL_USE_TLS = True # Habilita o uso de TLS (protoloco de segurança) ao enviar os emails.
MAIL_USE_SSL = False # Desabilita o uso de ssl (secure Sockets Layer) para e-mails.
