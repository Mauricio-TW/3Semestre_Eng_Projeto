from abc import ABC, abstractmethod

class PrioridadeStrategy(ABC):
    @abstractmethod
    def calcular_prioridade(self, tarefa):
        pass

class PrioridadePorData(PrioridadeStrategy):
    def calcular_prioridade(self, tarefa):
        if tarefa.vencimento:
            # Simples: se a data existe, retorna "alta", senão "normal"
            return "alta"
        return "normal"

class PrioridadePorDescricao(PrioridadeStrategy):
    def calcular_prioridade(self, tarefa):
        if "urgente" in tarefa.descricao.lower():
            return "alta"
        return "normal"