# Trabalho 6 - Analisador Léxico e Parser LL(1)

## Descrição

Este programa implementa um analisador léxico e um *parser* LL(1) para expressões matemáticas simples. O analisador léxico usa a biblioteca `ply.lex` para tokenizar a entrada, enquanto o *parser* LL(1) avalia a expressão utilizando uma abordagem recursiva descendente.

O analisador suporta os seguintes *tokens*:

- **Operadores matemáticos:** `+`, `-`, `*`, `/`;
- **Parênteses:** `(`, `)`;
- **Números inteiros**.


## Execução

Para executar o analisador, utiliza-se o seguinte comando:

```bash
python3 tpc6.py
```

Seguidamente, introduz-se uma expressão matemática para ser analisada e calculada.

## Exemplo

### Entrada:
```
2+3
67-(2+3*4)
(9-2)*(13-4)
```

### Saída:
```
Tokens: [LexToken(NUMERO, 2, 1, 0), LexToken(MAIS, '+', 1, 1), LexToken(NUMERO, 3, 1, 2)]
Resultado: 5

Tokens: [LexToken(NUMERO, 67, 1, 0), LexToken(MENOS, '-', 1, 2), LexToken(LPAREN, '(', 1, 3), LexToken(NUMERO, 2, 1, 4), LexToken(MAIS, '+', 1, 5), LexToken(NUMERO, 3, 1, 6), LexToken(MULT, '*', 1, 7), LexToken(NUMERO, 4, 1, 8), LexToken(RPAREN, ')', 1, 9)]
Resultado: 53

Tokens: [LexToken(LPAREN, '(', 1, 0), LexToken(NUMERO, 9, 1, 1), LexToken(MENOS, '-', 1, 2), LexToken(NUMERO, 2, 1, 3), LexToken(RPAREN, ')', 1, 4), LexToken(MULT, '*', 1, 5), LexToken(LPAREN, '(', 1, 6), LexToken(NUMERO, 13, 1, 7), LexToken(MENOS, '-', 1, 8), LexToken(NUMERO, 4, 1, 9), LexToken(RPAREN, ')', 1, 10)]
Resultado: 63
```

## Dependências

- Python 3
- `ply` (instalar com `pip install ply`)


## Autor

- Flávia Alexandra Silva Araújo, A96587 (27/03/2025)


<img src="https://avatars.githubusercontent.com/u/73347444?v=4" alt="Autora" width="10%">

