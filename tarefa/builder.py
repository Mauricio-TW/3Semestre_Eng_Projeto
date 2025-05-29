from tarefa.tarefa import Tarefa

class TarefaBuilder:
    def __init__(self):
        self.titulo = None
        self.descricao = ""
        self.prioridade = "normal"
        self.vencimento = None

    def set_titulo(self, titulo):
        self.titulo = titulo
        return self

    def set_descricao(self, descricao):
        self.descricao = descricao
        return self

    def set_prioridade(self, prioridade):
        self.prioridade = prioridade
        return self

    def set_vencimento(self, vencimento):
        self.vencimento = vencimento
        return self

    def build(self):
        if not self.titulo:
            raise ValueError("Título obrigatório")
        return Tarefa(self.titulo, self.descricao, self.prioridade, self.vencimento)