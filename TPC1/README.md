# Trabalho 1

## Descrição
Este programa interpreta uma linha de entrada contendo palavras e 
números e soma os números encontrados, dependendo do estado de um "interruptor" interno.
O estado do interruptor pode ser alterado com as palavras "on" e "off".

## Funcionamento
Após a execução do programa, o utilizador deve inserir uma linha de texto contendo palavras e números.
O programa irá percorrer a linha caractere por caractere:
- Se encontrar "on", ativa a soma e avança dois caracteres;
- Se encontrar "off", desativa a soma e avança três caracteres;
- Se encontrar um número e a soma estiver ativa (on == True), acumula os dígitos consecutivos e adiciona à soma;
- Caso contrário, avança um caractere.


## Exemplo
```
Input: on12off5hello on 3hi 5off
Output: 20
```

## Autor
- Flávia Alexandra Silva Araújo, A96587
![Autora](Images/pfp.png)

