#!/usr/bin/env python3

import sys
import json
import ply.lex as lex
import ply.yacc as yacc
from datetime import datetime
from tabulate import tabulate

# Estado da Máquina
class State:
    def __init__(self):
        self.on = True
        self.stock = {}
        self.balance = 0  # em cêntimos
        self.stock_file = ""

state = State()

# Análise Lexical
tokens = [
    "AJUDA", "LISTAR", "MOEDA", "SELECIONAR", "SAIR", "CODIGO", "VALOR_MOEDA"
]

literals = [',', '.']

def t_AJUDA(t): r"(?i:ajuda)"; return t
def t_LISTAR(t): r"(?i:listar)"; return t
def t_SELECIONAR(t): r"(?i:selecionar)"; return t
def t_SAIR(t): r"(?i:sair)"; return t
def t_CODIGO(t): r"[A-Z][0-9]{2}"; return t

def t_MOEDA(t):
    r'(?i:moeda)'
    return t

def t_VALOR_MOEDA(t):
    r'(1c|2c|5c|10c|20c|50c|1e|2e)'
    # Converter para cêntimos
    if t.value.endswith('e'):
        t.value = int(t.value[:-1]) * 100
    else:
        t.value = int(t.value[:-1])
    return t

t_ignore = ' \t\n'

def t_error(t):
    print(f"Caracter inválido: {t.value[0]}")
    t.lexer.skip(1)

def format_balance(balance):
    euros = balance // 100
    cents = balance % 100
    return f"{euros}e{cents}c" if euros > 0 else f"{cents}c"

def coin_change(change):
    coins = [
        ("2e", 200),
        ("1e", 100),
        ("50c", 50),
        ("20c", 20),
        ("10c", 10),
        ("5c", 5),
        ("2c", 2),
        ("1c", 1)
    ]
    result = []
    remaining = change
    
    for coin, value in coins:
        if remaining >= value:
            count = remaining // value
            remaining -= count * value
            result.append(f"{count}x {coin}")
    
    return ", ".join(result) if result else "0c"

def save_stock():
    try:
        with open(state.stock_file, 'w') as f:
            json.dump(list(state.stock.values()), f, indent=4)
    except Exception as e:
        print(f"Erro ao salvar stock: {e}")

# Análise Sintática
def p_comando(p):
    """
    comando : ajuda
            | listar
            | moeda
            | selecionar
            | sair
    """

def p_ajuda(p):
    """ajuda : AJUDA"""
    print("""Comandos disponíveis:
  AJUDA - Mostra esta ajuda
  LISTAR - Lista os produtos disponíveis
  MOEDA <lista de moedas> . - Adiciona moedas (ex: MOEDA 1e, 50c, 20c .)
  SELECIONAR <código> - Seleciona um produto (ex: SELECIONAR A23)
  SAIR - Termina a sessão e devolve o troco""")

def p_listar(p):
    """listar : LISTAR"""
    headers = ["Código", "Nome", "Quantidade", "Preço"]
    rows = []
    for item in state.stock.values():
        rows.append([
            item["cod"],
            item["nome"],
            item["quant"],
            f"{item['preco']:.2f}€"
        ])
    print(tabulate(rows, headers=headers, tablefmt="simple"))

def p_moeda(p):
    '''moeda : MOEDA lista_moedas '.' '''
    print(f"maq: Saldo = {format_balance(state.balance)}")

def p_lista_moedas(p):
    '''
    lista_moedas : VALOR_MOEDA
                | lista_moedas ',' VALOR_MOEDA
    '''
    if len(p) == 2:  # caso base: uma moeda
        state.balance += p[1]
    else:  # caso recursivo: moedas adicionais
        state.balance += p[3]

def format_balance(balance):
    euros = balance // 100
    cents = balance % 100
    if euros > 0 and cents > 0:
        return f"{euros}e{cents}c"
    elif euros > 0:
        return f"{euros}e"
    else:
        return f"{cents}c"

def p_selecionar(p):
    """selecionar : SELECIONAR CODIGO"""
    cod = p[2]
    if cod not in state.stock:
        print(f"maq: Código {cod} inválido")
    elif state.stock[cod]["quant"] <= 0:
        print(f"maq: Produto {state.stock[cod]['nome']} esgotado")
    elif state.balance < state.stock[cod]["preco"] * 100:  # converter para cêntimos
        required = state.stock[cod]["preco"] * 100
        print(f"maq: Saldo insuficiente (Saldo = {format_balance(state.balance)}; Pedido = {format_balance(required)})")
    else:
        state.balance -= state.stock[cod]["preco"] * 100
        state.stock[cod]["quant"] -= 1
        print(f"maq: Pode retirar o produto dispensado \"{state.stock[cod]['nome']}\"")
        print(f"maq: Saldo = {format_balance(state.balance)}")

def p_sair(p):
    """sair : SAIR"""
    if state.balance > 0:
        print(f"maq: Pode retirar o troco: {coin_change(state.balance)}")
    print("maq: Até à próxima")
    save_stock()
    state.on = False

def p_error(p):
    if p:
        print(f"Erro de sintaxe próximo a '{p.value}'")
    else:
        print("Erro de sintaxe no comando")

def main():
    if len(sys.argv) != 2:
        print("Uso: tpc5.py <ficheiro_stock>")
        sys.exit(1)
    
    state.stock_file = sys.argv[1]
    
    try:
        with open(state.stock_file) as f:
            state.stock = {item["cod"]: item for item in json.load(f)}
    except Exception as e:
        print(f"maq: Erro ao carregar stock: {e}")
        sys.exit(1)
    
    print(f"maq: {datetime.now().strftime('%Y-%m-%d')}, Stock carregado, Estado atualizado.")
    print("maq: Bom dia. Estou disponível para atender o seu pedido.")
    
    lexer = lex.lex()
    parser = yacc.yacc()
    
    while state.on:
        try:
            cmd = input(">> ")
            parser.parse(cmd, lexer=lexer)
        except (EOFError, KeyboardInterrupt):
            state.on = False
            save_stock()
            print("\nmaq: Até à próxima")
        except Exception as e:
            print(f"maq: Erro: {e}")

if __name__ == "__main__":
    main()