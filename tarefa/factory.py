from tarefa.tarefa import Tarefa

def criar_tarefa_simples(titulo, descricao = "Sem descrição"):
    return Tarefa(titulo, descricao, prioridade="baixa")

def criar_tarefa_com_prioridade(titulo, prioridade, descricao = "Sem descrição"):
    return Tarefa(titulo, descricao, prioridade)