# 📘 Atividade: Consumo Resiliente de APIs Externas

## 🎯 Objetivo

Construir um cliente Python capaz de consumir dados de APIs públicas com robustez, aplicando timeout, retry com backoff exponencial, tratamento de erros e normalização de respostas em um único relatório.

## 📝 Tarefas

### 🛠️ Implementar cliente HTTP com timeout e retry

#### Descrição
Crie funções para buscar dados de pelo menos duas APIs públicas diferentes. O cliente deve suportar falhas temporárias de rede ou respostas 5xx com nova tentativa automática.

#### Requisitos
O programa concluído deve:

- Definir timeout em todas as chamadas HTTP.
- Implementar retry com backoff exponencial para erros de conexão, timeout e respostas 5xx.
- Limitar o número máximo de tentativas para evitar loops infinitos.


### 🛠️ Normalizar e combinar dados de múltiplas fontes

#### Descrição
Converta respostas com estruturas diferentes para um formato comum e gere um único conjunto de dados final para análise simples.

#### Requisitos
O programa concluído deve:

- Consumir pelo menos duas APIs públicas distintas.
- Transformar os dados em um formato padronizado com campos consistentes.
- Combinar os resultados em uma coleção única pronta para exportação.


### 🛠️ Gerar relatório e tratamento de erro amigável

#### Descrição
Crie uma saída final clara para o usuário e mensagens de erro úteis para cenários de falha parcial ou total.

#### Requisitos
O programa concluído deve:

- Exibir um resumo com total de registros válidos e quantidade de falhas por API.
- Salvar o resultado final em arquivo JSON.
- Mostrar mensagens de erro em português com contexto suficiente para diagnóstico.
