from tarefa.builder import TarefaBuilder
from tarefa.facade import TarefaFacade
from tarefa.logger_observer import LoggerObserver  # Parte 3 - Observer
from tarefa.strategy import PrioridadePorDescricao  # Parte 2 - Strategy específica
from tarefa.tarefa import Tarefa

def main():
    # PARTE 1 DO TRABALHO - Builder
    builder = TarefaBuilder()
    tarefa = (builder.set_titulo("Exemplo de tarefa")
                    .set_descricao("Tarefa criada com builder")
                    .set_prioridade("média")
                    .build())
    print("Tarefa criada com o Builder:")
    print(tarefa)

    # PARTE 2 DO TRABALHO - Facade + Decorator
    facade = TarefaFacade()

    tarefa_importante = facade.criar_tarefa_importante("Apresentação", "Preparar slides para a reunião")
    print("\nTarefa importante (Decorator):")
    print(tarefa_importante.exibir())

    tarefa_com_prazo = facade.criar_tarefa_com_prazo("Entrega de relatório", "Enviar relatório final", "12/06/2025")
    print("\nTarefa com prazo (Decorator):")
    print(tarefa_com_prazo.exibir())

    # PARTE 3 DO TRABALHO - Observer
    print("\n--- Exemplo Observer ---")
    tarefa_obs = Tarefa("Observer Exemplo", "Testando Observer", "normal")
    logger = LoggerObserver()
    tarefa_obs.anexar(logger)

    print("Mudando prioridade para 'alta' e notificando observadores:")
    tarefa_obs.set_prioridade("alta")  # Vai disparar log via LoggerObserver

    # PARTE 2 e 3 - Strategy + Observer combinados
    print("\n--- Exemplo Strategy + Observer ---")
    tarefa_strat = Tarefa("Strategy Exemplo", "Essa tarefa é urgente", prioridade=None, estrategia=PrioridadePorDescricao())
    tarefa_strat.anexar(logger)

    print(f"Prioridade inicial calculada pela estratégia: {tarefa_strat.prioridade}")
    print("Alterando descrição para não urgente e aplicando nova prioridade:")
    tarefa_strat.descricao = "Tarefa normal"
    tarefa_strat.aplicar_prioridade()  # Recalcula prioridade e notifica observador

    print(f"Nova prioridade após aplicar estratégia: {tarefa_strat.prioridade}")

if __name__ == "__main__":
    main()