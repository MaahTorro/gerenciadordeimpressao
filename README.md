# Autocompletador de Palavras — BST em Python

Este projeto consiste em um sistema de autocompletar palavras utilizando uma Árvore Binária de Busca (BST). As palavras são carregadas a partir de um dicionário em português e, com base em um prefixo fornecido pelo usuário, o sistema retorna sugestões compatíveis.

## Funcionalidades

- Inserção ordenada das palavras em uma estrutura de árvore binária
- Busca eficiente por prefixos
- Interface no terminal com cores para facilitar a navegação
- Leitura de arquivo de dicionário externo
- Validação de entrada e mensagens de retorno claras

## Como funciona

O programa carrega um arquivo `.txt` com palavras, uma por linha, e as armazena em uma árvore binária de busca. A busca por sugestões ocorre de forma recursiva, identificando todas as palavras que começam com o prefixo fornecido.

## Como usar

1. Baixe ou clone este repositório.
2. Certifique-se de que o arquivo `dicionario_pt.txt` esteja presente no diretório.
3. Execute o script Python com:

```bash
python nome_do_arquivo.py
```

4. Digite o prefixo desejado.
5. Para encerrar a execução, digite `sair`.

## Integrantes

- Marcela Torro — RM557658  
- Matheus V. — RM555177  
- Matheus Queiroz — RM558801  
- Gustavo Attanazio — RM559098  
- Rodrigo Leme — RM550266
