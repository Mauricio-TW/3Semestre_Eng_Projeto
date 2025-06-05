import unittest
from tarefa.tarefa import Tarefa
from tarefa.builder import TarefaBuilder
from tarefa.factory import criar_tarefa_simples, criar_tarefa_com_prioridade

class TesteTarefa(unittest.TestCase):

#ALTERAÇÕES FEITAS PARA PARTE 2
    def test_criar_tarefa(self):
        t = Tarefa("Estudar", "Estudar para a prova", "alta")
        self.assertEqual(t.titulo, "Estudar")
        self.assertEqual(t.descricao, "Estudar para a prova")
        self.assertEqual(t.prioridade, "alta")

    def test_builder(self):
        builder = TarefaBuilder()
        tarefa = (builder.set_titulo("Fazer café")
                         .set_descricao("Antes da reunião")
                         .set_prioridade("alta")
                         .build())
        self.assertEqual(tarefa.titulo, "Fazer café")
        self.assertEqual(tarefa.prioridade, "alta")
        self.assertEqual(tarefa.descricao, "Antes da reunião")

#ALTERAÇÕES FEITAS PARA PARTE 2
    def test_factory(self):
        t1 = criar_tarefa_simples("Ler livro")  # descrição padrão "Sem descrição"
        t2 = criar_tarefa_com_prioridade("Enviar email", "alta", "Descrição do email")
        self.assertEqual(t1.titulo, "Ler livro")
        self.assertEqual(t1.descricao, "Sem descrição")
        self.assertEqual(t2.prioridade, "alta")
        self.assertEqual(t2.descricao, "Descrição do email")

if __name__ == "__main__":
    unittest.main()