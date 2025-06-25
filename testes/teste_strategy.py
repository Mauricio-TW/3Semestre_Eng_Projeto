#PARTE 3 DO TRABALHO
import unittest
from tarefa.strategy import PrioridadePorData, PrioridadePorDescricao
from tarefa.tarefa import Tarefa

class TestStrategy(unittest.TestCase):
    def test_prioridade_por_data(self):
        # Tarefa sem data vence -> prioridade normal
        tarefa = Tarefa("Sem data", "Descrição", estrategia=PrioridadePorData())
        self.assertEqual(tarefa.prioridade, "normal")

        # Tarefa com data vence -> prioridade alta após aplicar
        tarefa.vencimento = "2025-06-30"
        tarefa.aplicar_prioridade()
        self.assertEqual(tarefa.prioridade, "alta")

    def test_prioridade_por_descricao(self):
        # Descrição com "urgente" -> prioridade alta
        tarefa = Tarefa("Urgente", "Tarefa urgente", prioridade=None, estrategia=PrioridadePorDescricao())
        self.assertEqual(tarefa.prioridade, "alta")

        # Alterar descrição remove prioridade alta
        tarefa.descricao = "Tarefa normal"
        tarefa.aplicar_prioridade()
        self.assertEqual(tarefa.prioridade, "normal")