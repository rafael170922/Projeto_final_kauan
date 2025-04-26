from models.confirmacao_pedido_model import ConfirmacaoPedidoModel
from util.envio_email import enviar_email

class ConfirmacaoPedidoController:

    @staticmethod
    def confirmar_pedido(usuario_id):
        #Confirma o agendamento mais recente do usuário no banco de dados
        pedido= ConfirmacaoPedidoModel.confirmar_pedido(usuario_id)

        if not pedido:
            return {"erro": "Agenda não encontrada ou não autorizado."}, 404
        
        # Verifica se a chave 'quantidade' existe no pedido
        if 'quantidade' not in pedido:
            return {"erro": "Informações do agendamento estão incompletas."}, 400

        #Enviar e-mail de confirmação
        usuario_email = pedido['usuario_email'] # E-mail do usuário.
        assunto = "Confirmação do seu agendamento"

        #Corrigindo para incluir o agendamento de cada cliente.
        corpo = f"""
        Olá, seu agendamento foi confirmado com sucesso!

        Detalhes do pedido:
        Corte(s): {pedido['corte']}
        Horario: {pedido['horario']}
        Total: R$ {pedido['total']:.2f}

        Seu agendamneto foi efetuado com sucesso!!

        Agradecemos pela compra e logo entraremos em contato com mais detalhes.

        Atenciosamente,

        Barbearia SeuCorte
        """

        sucesso_email = enviar_email(usuario_email, assunto, corpo)

        if sucesso_email:
            return {"mensagem": "Agendamento confirmado e e-mail enviado com sucesso!"}, 200
        else:
            return {"erro": "Agendamento confirmado, mas não foi possível inviar o e-mail."}, 500