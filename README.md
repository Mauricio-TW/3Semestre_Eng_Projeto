# Projeto de Gerenciamento de Tarefas

## Descrição

Este projeto implementa um sistema simples de gerenciamento de tarefas, utilizando padrões criacionais de projeto para garantir flexibilidade e facilidade de manutenção. A primeira etapa do projeto contempla a aplicação dos padrões **Builder** e **Factory** para a criação de tarefas com diferentes configurações.

## Funcionalidades da 1ª Etapa

- **Classe Tarefa:** Representa uma tarefa com título, descrição, prioridade e data de vencimento.
- **Padrão Builder:** Permite a criação flexível e incremental de objetos `Tarefa` através da classe `TarefaBuilder`.
- **Padrão Factory:** Facilita a criação de tarefas pré-configuradas com funções de fábrica (`criar_tarefa_simples`, `criar_tarefa_com_prioridade`).
- **Testes Unitários:** Implementados para validar a criação e o comportamento das tarefas usando o framework `unittest`.

## Estrutura do Projeto

3Semestre_Eng_Projeto/
├── main.py # Script principal para execução e testes manuais
├── README.md # Documentação do projeto
├── tarefa/ # Pacote com as implementações
│ ├── init.py
│ ├── tarefa.py # Definição da classe Tarefa
│ ├── builder.py # Implementação do padrão Builder
│ └── factory.py # Implementação do padrão Factory
└── testes/ # Testes unitários
└── teste_tarefa.py


## Como Executar os Testes

Certifique-se de ter o Python instalado (versão 3.7 ou superior). Para rodar os testes unitários, execute no terminal:

```bash
py -m unittest discover testes

Você deve ver uma saída indicando que todos os testes foram executados com sucesso:

...
----------------------------------------------------------------------
Ran X tests in Y seconds

OK