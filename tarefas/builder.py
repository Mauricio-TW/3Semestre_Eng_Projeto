from tarefa import Tarefa

class TarefaBuilder:
    def __init__(self, titulo):
        self._titulo = titulo
        self._descricao = ""
        self._prioridade = "normal"
        self._vencimento = None

    def com_descricao(self, descricao):
        self._descricao = descricao
        return self

    def com_prioridade(self, prioridade):
        self._prioridade = prioridade
        return self

    def com_vencimento(self, vencimento):
        self._vencimento = vencimento
        return self

    def construir(self):
        return Tarefa(
            titulo=self._titulo,
            descricao=self._descricao,
            prioridade=self._prioridade,
            vencimento=self._vencimento
        )
