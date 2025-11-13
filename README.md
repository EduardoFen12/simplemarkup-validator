# simplemarkup-validator
A SimpleMarkup syntax validator built in Python, featuring a custom lexer and parser for checking tag structure and nesting.

# Lexer - SimpleMarkup

Este módulo converte um arquivo .sm em uma lista de tokens.

## Como rodar

python3
>>> from lexer import tokenize
>>> texto = "<titulo>Meu Título</titulo>"
>>> tokenize(texto)

Saída esperada:
[
    ('TAG_ABERTURA', 'titulo'),
    ('TEXTO', 'Meu Título'),
    ('TAG_FECHAMENTO', 'titulo')
]

## Arquivos incluídos
✔ lexer.py  
✔ documento1_valido.sm  
✔ documento2_valido.sm  
✔ documento3_valido.sm  
✔ documento1_invalido.sm  
✔ documento2_invalido.sm  
✔ documento3_invalido.sm

# Parser - SimpleMarkup

O parser recebe tokens do lexer e usa uma pilha para validar
o aninhamento correto das tags.

## Como usar

from lexer import tokenize
from parser import parse

texto = "<a><b>texto</b></a>"
tokens = tokenize(texto)
resultado, mensagem = parse(tokens)
print(resultado, mensagem)

## Saídas esperadas
True Sintaxe válida!
False Erro: ...
