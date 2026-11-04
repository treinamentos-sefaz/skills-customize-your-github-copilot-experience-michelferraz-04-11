# 📘 Atividade: Building REST APIs com FastAPI

## 🎯 Objetivo

Construir uma API REST com FastAPI para gerenciar uma lista de tarefas, aplicando conceitos de rotas HTTP, validação de dados com Pydantic e boas práticas de resposta de erro.

## 📝 Tarefas

### 🛠️ Criar os endpoints básicos da API

#### Descrição
Implemente os endpoints iniciais para verificar se a API está online e listar tarefas cadastradas em memória.

#### Requisitos
O programa concluído deve:

- Expor um endpoint GET em /health que retorne status da aplicação.
- Expor um endpoint GET em /tasks que retorne a lista de tarefas.
- Retornar respostas em formato JSON.

### 🛠️ Implementar criação e atualização de tarefas

#### Descrição
Adicione recursos para criar tarefas e atualizar o status de conclusão usando modelos de dados com validação.

#### Requisitos
O programa concluído deve:

- Expor um endpoint POST em /tasks para criar uma nova tarefa.
- Validar os campos de entrada (por exemplo: titulo obrigatório com pelo menos 3 caracteres).
- Expor um endpoint PATCH em /tasks/{task_id} para marcar uma tarefa como concluída ou pendente.

### 🛠️ Tratar erros e padronizar respostas

#### Descrição
Garanta que a API responda de forma clara quando uma tarefa não for encontrada ou quando o corpo da requisição for inválido.

#### Requisitos
O programa concluído deve:

- Retornar erro 404 com mensagem descritiva quando task_id não existir.
- Retornar erro 422 para dados inválidos com detalhes de validação.
- Incluir mensagens de sucesso e erro consistentes em português.
