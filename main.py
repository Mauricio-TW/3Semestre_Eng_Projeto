from tarefa.builder import TarefaBuilder

def main():
    builder = TarefaBuilder()
    tarefa = (builder.set_titulo("Exemplo de tarefa")
                    .set_descricao("Tarefa criada com builder")
                    .set_prioridade("média")
                    .build())
    print(tarefa)

if __name__ == "__main__":
    main()