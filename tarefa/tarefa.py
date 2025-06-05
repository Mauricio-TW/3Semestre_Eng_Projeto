class Tarefa:
    def __init__(self, titulo, descricao, prioridade, vencimento = None):
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.vencimento = vencimento

    def __str__(self):
        return f"{self.titulo} - {self.descricao} - Prioridade: {self.prioridade}"

    #PARTE 2 DO TRABALHO
    def exibir(self):
        return f"{self.titulo} - {self.descricao} - Prioridade: {self.prioridade}"
    
    