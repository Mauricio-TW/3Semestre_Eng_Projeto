#PARTE 2 DO TRABALHO
import unittest
from tarefa.tarefa import Tarefa
from tarefa.decorators import TarefaImportante, TarefaComNotificacao

class TestDecorator(unittest.TestCase):
    def test_tarefa_importante(self):
        tarefa = Tarefa("Teste", "Descrição", 1, "2025-06-01")
        decorada = TarefaImportante(tarefa)
        self.assertIn("[IMPORTANTE]", decorada.exibir())

    def test_tarefa_com_notificacao(self):
        tarefa = Tarefa("Teste", "Descrição", 1, "2025-06-01")
        decorada = TarefaComNotificacao(tarefa)
        self.assertIn("Notificação ativada", decorada.exibir())