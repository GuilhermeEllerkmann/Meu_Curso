from abc import ABC, abstractmethod

class Notificao(ABC):
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool:...

class NotificaoEmail(Notificao):
    def enviar(self) -> bool:
        print('Email: enviando:', self.mensagem)
        return True

class NotificaoSMS(Notificao):
    def enviar(self) -> bool:
        print('SMS: enviando:', self.mensagem)
        return True


def notificar(notificacao: Notificao):
    notificao_enviada = notificacao.enviar()

    if notificao_enviada:
        print('notificacao enviada')
    else:
        print('notificacao nao enviada')

notificar(NotificaoEmail('NOT EMAIL'))
notificar(NotificaoSMS('NOT SMS'))