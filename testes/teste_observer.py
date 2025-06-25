#PARTE 3 DO TRABALHO
import unittest
from tarefa.tarefa import Tarefa
from tarefa.logger_observer import LoggerObserver  # Exemplo de observer que imprime log

class TestObserver(unittest.TestCase):
    def test_notificacao_ao_mudar_prioridade(self):
        tarefa = Tarefa("Testar Observer", "Descrição", "normal")
        logger = LoggerObserver()
        tarefa.anexar(logger)

        import io
        import sys
        capturado = io.StringIO()
        sys.stdout = capturado  # Redireciona saída para capturar o print

        tarefa.set_prioridade("alta")

        sys.stdout = sys.__stdout__  # Restaura saída padrão
        saida = capturado.getvalue()

        self.assertIn("Prioridade da tarefa 'Testar Observer' mudou para alta", saida)