# Projeto de Gerenciamento de Tarefas

## Descrição

Este projeto implementa um sistema simples de gerenciamento de tarefas, utilizando padrões criacionais de projeto para garantir flexibilidade e facilidade de manutenção. A primeira etapa do projeto contempla a aplicação dos padrões **Builder** e **Factory** para a criação de tarefas com diferentes configurações.

## Funcionalidades da 1ª Etapa

- **Classe Tarefa:** Representa uma tarefa com título, descrição, prioridade e data de vencimento.
- **Padrão Builder:** Permite a criação flexível e incremental de objetos `Tarefa` através da classe `TarefaBuilder`.
- **Padrão Factory:** Facilita a criação de tarefas pré-configuradas com funções de fábrica (`criar_tarefa_simples`, `criar_tarefa_com_prioridade`).
- **Testes Unitários:** Implementados para validar a criação e o comportamento das tarefas usando o framework `unittest`.

## Funcionalidades da 2ª Etapa

- **Padrão Facade:** Implementado através da classe `TarefaFacade` para simplificar a criação de diferentes tipos de tarefas, encapsulando a lógica complexa da criação e composição dos objetos.
- **Padrão Decorator:** Criados decoradores `TarefaImportante` e `TarefaComNotificacao` para adicionar dinamicamente comportamentos às tarefas, como marcar uma tarefa como importante ou ativar notificações, sem modificar a classe original.
- **Testes Unitários:** O `Facade` retorna tarefas simples ou decoradas, abstraindo o cliente da complexidade da construção e da aplicação dos decoradores.
- **Testes Unitários:** Novos testes foram criados para validar o comportamento dos `Decorators` e da `Facade`, garantindo que as tarefas importantes e notificadas exibem as informações esperadas.
- **Melhoria na Manutenção e Extensibilidade:** Com a aplicação dos padrões estruturais, o código fica mais modular, facilitando a adição de novos tipos de tarefas e comportamentos sem impactar o código existente.

## Funcionalidades da 3ª Etapa

- **Padrão Observer:** A classe `Tarefa` foi adaptada para funcionar como Subject que notifica observadores sobre mudanças, principalmente quando a prioridade é alterada. Implementado um `LoggerObserver` que recebe notificações e imprime logs no console, demonstrando o padrão `Observer` em ação.
- **Padrão Strategy:** Adicionada a possibilidade de calcular dinamicamente a prioridade da tarefa com diferentes estratégias. Criadas estratégias como `PrioridadePorData` e `PrioridadePorDescricao` que determinam a prioridade com base em atributos da tarefa (como data de vencimento e conteúdo da descrição). A classe `Tarefa` foi adaptada para aceitar uma estratégia de prioridade e recalcular sua prioridade automaticamente.
- **Integração Strategy + Observer:** A prioridade calculada por uma estratégia pode disparar notificações para observadores inscritos, promovendo alto desacoplamento e flexibilidade.

## Estrutura do Projeto

3Semestre_Eng_Projeto/
├── main.py                # Script principal para execução e testes manuais
├── README.md              # Documentação do projeto
├── tarefa/                # Pacote com as implementações
│   ├── __init__.py
│   ├── tarefa.py          # Definição da classe Tarefa (com Observer e Strategy)
│   ├── builder.py         # Implementação do padrão Builder
│   ├── factory.py         # Implementação do padrão Factory
│   ├── decorators.py      # Implementação dos padrões Decorator
│   ├── facade.py          # Implementação do padrão Facade
│   ├── observer.py        # Implementação do padrão Observer (Subject/Observer)
│   ├── logger_observer.py # Observer concreto que imprime logs
│   └── strategy.py        # Implementação do padrão Strategy
└── testes/                # Testes unitários
    ├── teste_tarefa.py
    ├── teste_decorator.py
    ├── teste_facade.py
    ├── teste_observer.py
    └── teste_strategy.py


## Como Executar os Testes

Certifique-se de ter o Python instalado (versão 3.7 ou superior). Para rodar os testes unitários, execute no terminal:

```bash
py -m unittest discover testes

Você deve ver uma saída indicando que todos os testes foram executados com sucesso:

..........
----------------------------------------------------------------------
Ran 10 tests in 0.001s

OK