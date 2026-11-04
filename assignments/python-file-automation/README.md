# 📘 Assignment: Automatizando arquivos com Python

## 🎯 Objective

Crie um programa que automatize a organização de arquivos por extensão. Você vai praticar como dividir o trabalho em funções e usar caminhos e pastas com a biblioteca padrão do Python.

## 📝 Tasks

### 🛠️ Classifique arquivos por extensão

#### Descrição
Escreva uma função que receba o nome de um arquivo e determine a categoria com base em sua extensão. Por exemplo, `foto.png` pertence à categoria `png`; arquivos sem extensão devem pertencer à categoria `sem-extensao`.

#### Requisitos
O programa concluído deve:

- Ter uma função que receba um caminho de arquivo e devolva a categoria correspondente.
- Ignorar diferenças entre letras maiúsculas e minúsculas na extensão.
- Tratar arquivos sem extensão sem gerar erro.

### 🛠️ Crie pastas para as categorias

#### Descrição
Use uma pasta de teste com cópias de arquivos. Para cada categoria encontrada, crie uma subpasta com o nome da categoria dentro da pasta de destino.

#### Requisitos
O programa concluído deve:

- Usar `pathlib` para trabalhar com caminhos e criar as pastas necessárias.
- Manter a pasta de origem separada da pasta de destino.
- Não alterar nem apagar arquivos fora da pasta de teste.

### 🛠️ Organize os arquivos e mostre um resumo

#### Descrição
Mova os arquivos da pasta de teste para as subpastas correspondentes e mostre quantos arquivos foram organizados em cada categoria.

#### Requisitos
O programa concluído deve:

- Usar uma função para organizar os arquivos e outra para contar os resultados.
- Usar `shutil` para mover os arquivos para suas categorias.
- Não sobrescrever um arquivo se já existir outro com o mesmo nome no destino; informe que o arquivo foi ignorado.
- Exibir um resumo com o total de arquivos organizados em cada categoria.
