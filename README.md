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

## Estrutura do Projeto

3Semestre_Eng_Projeto/
├── main.py                # Script principal para execução e testes manuais
├── README.md              # Documentação do projeto
├── tarefa/                # Pacote com as implementações
│   ├── __init__.py
│   ├── tarefa.py          # Definição da classe Tarefa
│   ├── builder.py         # Implementação do padrão Builder
│   ├── factory.py         # Implementação do padrão Factory
│   ├── decorators.py      # Implementação dos padrões Decorator
│   └── facade.py          # Implementação do padrão Facade
└── testes/                # Testes unitários
    ├── teste_tarefa.py
    ├── teste_decorator.py
    └── teste_facade.py


## Como Executar os Testes

Certifique-se de ter o Python instalado (versão 3.7 ou superior). Para rodar os testes unitários, execute no terminal:

```bash
py -m unittest discover testes

Você deve ver uma saída indicando que todos os testes foram executados com sucesso:

...
----------------------------------------------------------------------
Ran 7 tests in 0.000s

OK