from tarefa.tarefa import Tarefa

def criar_tarefa_simples(titulo):
    return Tarefa(titulo)

def criar_tarefa_com_prioridade(titulo, prioridade):
    return Tarefa(titulo, prioridade=prioridade)