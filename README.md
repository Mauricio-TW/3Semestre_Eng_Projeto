### README.md

# Sistema de Gerenciamento de Tarefas (To-Do List)

## Objetivo
Este projeto foi criado como parte de um trabalho prático para aplicar os principais padrões de projeto de software de forma incremental.

## 🔧 1ª Entrega - Padrões Criacionais

### Padrões Utilizados:

- **Factory Method:** usado para criar tarefas simples e com prioridade.
- **Builder:** usado para construir tarefas com múltiplos atributos opcionais (descrição, prioridade, vencimento).

### Por que esses padrões?
- O **Factory Method** fornece simplicidade e flexibilidade ao criar tarefas básicas.
- O **Builder** permite construir objetos complexos com uma API fluente e legível.

### Exemplo de Uso:
```python
from tarefa.builder import TarefaBuilder

nova_tarefa = (
    TarefaBuilder("Estudar")
    .com_descricao("Revisar padrões de projeto")
    .com_prioridade("alta")
    .com_vencimento("29/05/2025")
    .construir()
)
