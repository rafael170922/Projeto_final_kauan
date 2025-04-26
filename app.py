from flask import Flask # Importa a classe Flask para criar a aplicação web
from flask_jwt_extended import JWTManager # Importa o gerenciador de JWT para autenticação.
from banco_dados.db import criar_tabelas # Importa a função criar tabelas no banco de dados.
from routes.user_route import user_bp # Importa o Blueprint de usuários.
from routes.agendamento_route import pedido_bp # Importa Blueprint de pedidos.
from routes.horario_route import horarios_bp # Importa o Blueprint de horarios.
from routes.endereco_route import endereco_bp # Importa o Blueprint endereços.
from routes.pagamento_route import pagamento_bp # importa o Blueprint de pagamento.
from routes.confirmacao_pedido_route import confirmacao_pedido_bp # importa o blueprint de confirmação de pedidos.

# Cria a aplicação Flask.
app = Flask(__name__)
# Carrega as configurações do arquivo 'configuração.py'.
app.config.from_pyfile('config.py')

# Inicializa o gerenciador JWT para autenticação.
jwt = JWTManager(app)
# Cria as tabelas no banco de dados (caso ainda não existam).
criar_tabelas()

# Registra os blueprints com os respectivos prefixos de URL.
app.register_blueprint(user_bp, url_prefix='/users') # Rota de usuários.
app.register_blueprint(pedido_bp, url_prefix='/pedidos') # Rota de pedidos.
app.register_blueprint(horarios_bp, url_prefix='/horarios') # Rota de Horarios
app.register_blueprint(endereco_bp, url_prefix='/enderecos') # Rota de endereços.
app.register_blueprint(pagamento_bp, url_prefix='/pagamentos') # Rota de pagamentos.
app.register_blueprint(confirmacao_pedido_bp, url_prefix='/pedidos') # Rota de confirmação de pedidos.

# Executa a aplicação em modo debug.
if __name__ == '__main__':
    app.run(debug=True)