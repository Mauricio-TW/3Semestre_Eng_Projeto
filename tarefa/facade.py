#PARTE 2 DO TRABALHO
from tarefa.builder import TarefaBuilder
from tarefa.factory import criar_tarefa_simples
from tarefa.decorators import TarefaImportante, TarefaComNotificacao

class TarefaFacade:
    def criar_tarefa_rapida(self, titulo: str, descricao: str):
        return criar_tarefa_simples(titulo, descricao)

    def criar_tarefa_importante(self, titulo: str, descricao: str):
        tarefa = criar_tarefa_simples(titulo, descricao)
        return TarefaImportante(tarefa)

    def criar_tarefa_completa(self, titulo: str, descricao: str, prioridade: int, data: str):
        tarefa = (
            TarefaBuilder()
            .com_titulo(titulo)
            .com_descricao(descricao)
            .com_prioridade(prioridade)
            .com_data_vencimento(data)
            .construir()
        )
        return TarefaComNotificacao(tarefa)