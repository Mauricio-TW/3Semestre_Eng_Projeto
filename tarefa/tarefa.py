class Tarefa:
    def __init__(self, titulo, descricao="", prioridade="normal", vencimento=None):
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.vencimento = vencimento

    def __str__(self):
        return f"[Tarefa] {self.titulo} - {self.prioridade}"