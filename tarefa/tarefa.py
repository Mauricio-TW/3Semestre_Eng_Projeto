from tarefa.observer import Subject  # Parte 3 - importação do Subject
from tarefa.strategy import PrioridadeStrategy, PrioridadePorData  # Parte 2 - importação das estratégias

class Tarefa(Subject):  # Parte 3 - herda Subject para implementar Observer
    def __init__(self, titulo, descricao, prioridade=None, vencimento=None, estrategia=None):  # Parte 2 - prioridade opcional, estratégia opcional
        super().__init__()  # Parte 3 - inicializa Subject
        self.titulo = titulo
        self.descricao = descricao
        self.vencimento = vencimento
        self.estrategia = estrategia or PrioridadePorData()  # Parte 2 - usa estratégia padrão se não for passada
        self.prioridade = prioridade or self.estrategia.calcular_prioridade(self)  # Parte 2 - define prioridade usando estratégia caso não receba explicitamente

    def __str__(self):
        return f"{self.titulo} - {self.descricao} - Prioridade: {self.prioridade}"

    #PARTE 2 DO TRABALHO
    def exibir(self):
        return f"{self.titulo} - {self.descricao} - Prioridade: {self.prioridade}"

    # PARTE 3 DO TRABALHO
    def set_prioridade(self, nova_prioridade):
        self.prioridade = nova_prioridade
        self.notificar()

    # PARTE 2 DO TRABALHO - método para aplicar estratégia de prioridade
    def aplicar_prioridade(self):
        self.prioridade = self.estrategia.calcular_prioridade(self)
        self.notificar()  # Parte 3 - notifica observadores após mudar prioridade