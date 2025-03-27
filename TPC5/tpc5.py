import json
import datetime
from tabulate import tabulate

class VendingMachine:
    def __init__(self, stock_file='stock.json'):
        self.stock_file = stock_file
        self.load_stock()
        self.balance = 0
        self.print_initial_message()

    def load_stock(self):
        try:
            with open(self.stock_file, 'r', encoding='utf-8') as f:
                self.stock = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.stock = []

    def save_stock(self):
        with open(self.stock_file, 'w', encoding='utf-8') as f:
            json.dump(self.stock, f, indent=4)

    def format_balance(self):
        euros = int(self.balance)
        cents = round((self.balance - euros) * 100)
        return f"{euros}e{cents}c"

    def print_initial_message(self):
        print("maq: Stock carregado, Estado atualizado.")
        print("maq: Bom dia. Estou disponível para atender o seu pedido.")
        print(f"Data: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        self.list_products()
        self.show_balance()

    def list_products(self):
        if not self.stock:
            print("A máquina está vazia.")
            return
        headers = ["Código", "Nome", "Quantidade", "Preço (€)"]
        table = [[item['cod'], item['nome'], item['quant'], f"{item['preco']:.2f}"] for item in self.stock]
        print(tabulate(table, headers=headers, tablefmt="grid"))

    def show_balance(self):
        print(f"maq: Saldo = {self.format_balance()}")

    def insert_coins(self, coins):
        coin_values = {"1e": 1.0, "50c": 0.5, "20c": 0.2, "10c": 0.1, "5c": 0.05, "2c": 0.02, "1c": 0.01}
        for coin in coins:
            coin = coin.lower()
            if coin in coin_values:
                self.balance += coin_values[coin]
            else:
                print(f"maq: Moeda inválida ({coin}) ignorada.")
        self.show_balance()



    def select_product(self, code):
        for item in self.stock:
            if item['cod'] == code:
                if item['quant'] > 0:
                    if self.balance >= item['preco']:
                        self.balance -= item['preco']
                        item['quant'] -= 1
                        print(f"maq: Pode retirar o produto dispensado \"{item['nome']}\"")
                        self.save_stock()
                    else:
                        print(f"maq: Saldo insuficiente para satisfazer o seu pedido")
                        print(f"maq: Saldo = {self.format_balance()}; Pedido = {int(item['preco'])}e{int((item['preco'] - int(item['preco'])) * 100)}c")
                else:
                    print("maq: Produto esgotado.")
                self.show_balance()
                return
        print("maq: Produto inexistente.")
        self.show_balance()

    def return_change(self):
        coins = [1.0, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
        change = []
        amount = self.balance
        for coin in coins:
            count = int(amount // coin)
            if count > 0:
                change.append(f"{count}x {'1e' if coin == 1.0 else f'{int(coin * 100)}c'}")
                amount -= count * coin
        if change:
            print("maq: Pode retirar o troco:", ", ".join(change) + ".")
        self.balance = 0
        self.show_balance()

    def add_product(self, code, name, quantity, price):
        for item in self.stock:
            if item['cod'] == code:
                item['quant'] += quantity
                break
        else:
            self.stock.append({"cod": code, "nome": name, "quant": quantity, "preco": price})
        self.save_stock()

    def run(self):
        while True:
            command = input(">> ").strip().upper()
            if command == "LISTAR":
                self.list_products()
            elif command == "SALDO":
                self.show_balance()
            elif command.startswith("MOEDA"):
                coins = command.replace("MOEDA ", "").split(", ")
                self.insert_coins(coins)
            elif command.startswith("SELECIONAR"):
                code = command.split(" ")[1]
                self.select_product(code)
            elif command == "SAIR":
                self.return_change()
                print("maq: Até à próxima")
                break
            elif command.startswith("ADICIONAR"):
                try:
                    parts = command.split(" ", 4)
                    code, name, quantity, price = parts[1], parts[2], int(parts[3]), float(parts[4])
                    self.add_product(code, name, quantity, price)
                except (ValueError, IndexError):
                    print("Erro no comando ADICIONAR. Use o formato: ADICIONAR <código> <nome> <quantidade> <preço>")
            else:
                print("Comando inválido.")

if __name__ == "__main__":
    machine = VendingMachine()
    machine.run()
