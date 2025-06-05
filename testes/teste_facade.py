#PARTE 2 DO TRABALHO
import unittest
from tarefa.facade import TarefaFacade

class TestFacade(unittest.TestCase):
    def test_criar_tarefa_rapida(self):
        facade = TarefaFacade()
        tarefa = facade.criar_tarefa_rapida("A", "B")
        self.assertEqual(tarefa.titulo, "A")

    def test_criar_tarefa_importante(self):
        facade = TarefaFacade()
        tarefa = facade.criar_tarefa_importante("X", "Y")
        self.assertIn("[IMPORTANTE]", tarefa.exibir())