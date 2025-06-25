from tarefa.observer import Observer

class LoggerObserver(Observer):
    def atualizar(self, tarefa):
        print(f"[LOG] Prioridade da tarefa '{tarefa.titulo}' mudou para {tarefa.prioridade}")