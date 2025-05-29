import unittest
from tarefa import tarefa, TarefaBuilder, criar_tarefa_simples

class TestTarefa(unittest.TestCase):

    def test_criacao_simples(self):
        tarefa = criar_tarefa_simples("Comprar leite")
        self.assertEqual(tarefa.titulo, "Comprar leite")
        self.assertEqual(tarefa.prioridade, "normal")

    def test_builder_completo(self):
        tarefa = (TarefaBuilder()
                 .set_titulo("Estudar Python")
                 .set_descricao("Focar em padrões de projeto")
                 .set_prioridade("alta")
                 .set_vencimento("2025-06-01")
                 .build())
        self.assertEqual(tarefa.titulo, "Estudar Python")
        self.assertEqual(tarefa.descricao, "Focar em padrões de projeto")
        self.assertEqual(tarefa.prioridade, "alta")
        self.assertEqual(tarefa.vencimento, "2025-06-01")

if __name__ == "__main__":
    unittest.main()