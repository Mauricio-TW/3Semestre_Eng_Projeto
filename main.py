from tarefa.builder import TarefaBuilder
from tarefa.facade import TarefaFacade

def main():
    # Parte já existente no projeto
    builder = TarefaBuilder()
    tarefa = (builder.set_titulo("Exemplo de tarefa")
                    .set_descricao("Tarefa criada com builder")
                    .set_prioridade("média")
                    .build())
    print("Tarefa criada com o Builder:")
    print(tarefa)

    #PARTE 2 DO TRABALHO
    
    # NOVA PARTE — usando Facade + Decorator
    facade = TarefaFacade()

    # Criando uma tarefa importante
    tarefa_importante = facade.criar_tarefa_importante("Apresentação", "Preparar slides para a reunião")
    print("\nTarefa importante (Decorator):")
    print(tarefa_importante)

    # Criando uma tarefa com prazo
    tarefa_com_prazo = facade.criar_tarefa_com_prazo("Entrega de relatório", "Enviar relatório final", "12/06/2025")
    print("\nTarefa com prazo (Decorator):")
    print(tarefa_com_prazo)

if __name__ == "__main__":
    main()