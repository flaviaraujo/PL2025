# Trabalho 6 - Parser LL(1) Recursivo Descendente

## Descrição

Este programa implementa um ***parser* LL(1) recursivo descendente** que reconhece e avalia expressões aritméticas.
O analisador léxico converte a expressão em *tokens*, e o analisador sintático verifica a estrutura da expressão
seguindo uma gramática LL(1). Durante a análise, o valor da expressão é calculado recursivamente.

O *parser* suporta as seguintes operações:

- **Adição (`+`)** e **Subtração (`-`)**;
- **Multiplicação (`*`)** e **Divisão (`/`)** (com divisão inteira);
- **Uso de parênteses** para agrupar subexpressões.

## Execução

Para executar o programa, utiliza-se o seguinte comando:

```bash
python3 tpc6.py
```

O programa solicita ao utilizador que introduza uma expressão aritmética válida e retorna o resultado da avaliação,
bem como a lista de *tokens* gerada durante a análise léxica. Caso a expressão seja inválida, o programa exibe uma
mensagem de erro.

## Exemplo de Utilização

### Entrada:
```
2+3
(9-2)*(13-4)
67-(2+3*4)
```

### Saída:
```
Digite uma expressão: 2+3
Tokens: ['2', '+', '3', '$']
Resultado: 5

Digite uma expressão: (9-2)*(13-4)
Tokens: ['(', '9', '-', '2', ')', '*', '(', '13', '-', '4', ')', '$']
Resultado: 63

Digite uma expressão: 67-(2+3*4)
Tokens: ['67', '-', '(', '2', '+', '3', '*', '4', ')', '$']
Resultado: 53
```

## Dependências

- *Python* 3
- Biblioteca `re` (incluída por padrão no Python)

## Autor

- Flávia Alexandra Silva Araújo, A96587 (27/03/2025)


<img src="https://avatars.githubusercontent.com/u/73347444?v=4" alt="Autora" width="10%">

