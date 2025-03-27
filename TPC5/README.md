# Trabalho 5 - Máquina de Venda Automática

## Descrição

Este programa implementa uma Máquina de Venda Automática que permite a compra de produtos mediante inserção de moedas. 
A máquina gerencia um *stock* de produtos, aceita pagamentos e retorna o troco mediante estes.
O sistema é controlado através de comandos de texto interativos. Os produtos existentes, bem como os seus detalhes, 
estão definidos no ficheiro `stock.json`, que é fornecido como argumento ao programa.

A máquina suporta as seguintes funcionalidades:

- **Listar produtos disponíveis** com códigos, nomes, quantidades e preços;
- **Inserir moedas** de diferentes valores;
- **Selecionar produtos** para compra, verificando o saldo e a disponibilidade;
- **Retornar troco** ao encerrar a sessão;
- **Adicionar produtos ao *stock*** (somente para manutenção).

## Execução

Para executar a máquina de vendas, utiliza-se o seguinte comando:

```bash
python3 tpc5.py
```

## Comandos Disponíveis

- `LISTAR` → Exibe os produtos disponíveis na máquina;
- `SALDO` → Mostra o saldo atual inserido;
- `MOEDA <valores>` → Insere moedas na máquina (exemplo: `MOEDA 1e, 50c`);
- `SELECIONAR <código>` → Tenta comprar um produto pelo código;
- `SAIR` → Finaliza a operação e retorna o troco;
- `ADICIONAR <código> <nome> <quantidade> <preço>` → Adiciona produtos ao *stock*.

## Exemplo de Utilização

### Entrada:
```
LISTAR
MOEDA 1e, 50c
SELECIONAR A23
SAIR
```

### Saída:
```
maq: Stock carregado, Estado atualizado.
maq: Bom dia. Estou disponível para atender o seu pedido.
+--------+---------------+-----------+----------+
| Código | Nome         | Quantidade | Preço (€) |
+--------+---------------+-----------+----------+
| A23    | água 0.5L   | 7         | 0.70     |
| A12    | café curto  | 10        | 0.60     |
| A34    | sumo 0.2L   | 5         | 0.80     |
| A56    | bolachas    | 7         | 0.50     |
| A78    | chocolate   | 1         | 1.20     |
+--------+---------------+-----------+----------+
maq: Saldo = 0e0c
maq: Saldo = 1e50c
maq: Pode retirar o produto dispensado "água 0.5L"
maq: Pode retirar o troco: 5x 10c.
maq: Até à próxima
```

## Dependências

- *Python* 3
- `tabulate` (instalar com `pip install tabulate`, usada para gerar a tabela de produtos)

## Autor

- Flávia Alexandra Silva Araújo, A96587 (27/03/2025)


<img src="https://avatars.githubusercontent.com/u/73347444?v=4" alt="Autora" width="10%">
