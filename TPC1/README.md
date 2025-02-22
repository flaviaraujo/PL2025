# Trabalho 1 - Somador On/Off

## Descrição
Este programa interpreta uma linha de entrada contendo palavras, números e caracteres especiais,
somando os números encontrados conforme o estado de um "interruptor" interno. O estado do interruptor
pode ser alterado com as palavras "on" e "off", independentemente de maiúsculas ou minúsculas. Além disso,
sempre que encontrar o caracter '=', o programa imprime a soma acumulada até aquele momento.


## Funcionamento
Após a execução do programa, o utilizador deve inserir as linhas de texto, podendo conter palavras, números e caracteres especiais.\
O programa processa a entrada caractere por caracter:

- Se encontrar "on" (ignorando maiúsculas/minúsculas), ativa a soma e avança dois caracteres;
- Se encontrar "off" (ignorando maiúsculas/minúsculas), desativa a soma e avança três caracteres;
- Se encontrar "=", imprime a soma acumulada no momento;
- Se encontrar um número e a soma estiver ativa, acumula os dígitos consecutivos e adiciona à soma total;
- Caso contrário, avança um caractere.

Quando a entrada termina (EOF), o programa imprime a soma final.


## Exemplo
```
Input:

Hoje, 7 de Fevereiro de 2025, o professor de Processamento de Linguagens
deu-nos
este trabalho para fazer.=
E deu-nos 7= dias para o fazer...
Cada trabalho destes vale 0.25 valores da nota final!

Output: 

Hoje, 7 de Fevereiro de 2025, o professor de Processamento de Linguagens
deu-nos
este trabalho para fazer.=OfF
>> 2032
E deu-nos 7=
>> 2032
 dias para o fazer... ON
Cada trabalho destes vale 0.25 valores da nota final!
>> 2057
```

## Autor
- Flávia Alexandra Silva Araújo, A96587 (14/02/2025)


<img src="https://avatars.githubusercontent.com/u/73347444?v=4" alt="Autora" width="10%">


