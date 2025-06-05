#PARTE 2 DO TRABALHO
from tarefa.tarefa import Tarefa

class TarefaDecorator:
    def __init__(self, tarefa: Tarefa):
        self._tarefa = tarefa

    def exibir(self):
        return self._tarefa.__str__()

class TarefaImportante(TarefaDecorator):
    def exibir(self):
        return f"[IMPORTANTE] {self._tarefa.exibir()}"

class TarefaComNotificacao(TarefaDecorator):
    def exibir(self):
        return f"{self._tarefa.exibir()} - Notificação ativada"