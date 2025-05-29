from tarefa.builder import TarefaBuilder
from tarefa.factory import criar_tarefa_simples, criar_tarefa_com_prioridade

if __name__ == "__main__":
    tarefa1 = criar_tarefa_simples("Estudar Padrões de Projeto")
    print(tarefa1)

    tarefa2 = criar_tarefa_com_prioridade("Fazer trabalho", "alta")
    print(tarefa2)

    tarefa3 = (
        TarefaBuilder("Enviar projeto no GitHub")
        .com_descricao("Subir até as 19h")
        .com_prioridade("alta")
        .com_vencimento("29/05/2025")
        .construir()
    )
    print(tarefa3)
