import ply.lex as lex

# Definição dos tokens
tokens = (
    'NUMERO', 'MAIS', 'MENOS', 'MULT', 'DIV', 'LPAREN', 'RPAREN', 'EOF'
)

t_MAIS = r'\+'
t_MENOS = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Caractere ilegal: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

class LL1Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def eat(self, token_type):
        if self.pos < len(self.tokens) and self.tokens[self.pos].type == token_type:
            self.pos += 1
        else:
            raise SyntaxError(f"Esperado {token_type}, encontrado {self.tokens[self.pos].type if self.pos < len(self.tokens) else 'EOF'}")

    def parse(self):
        result = self.expr()
        if self.pos < len(self.tokens):
            raise SyntaxError("Tokens extras na entrada.")
        return result

    def expr(self):
        result = self.term()
        while self.pos < len(self.tokens) and self.tokens[self.pos].type in ('MAIS', 'MENOS'):
            op = self.tokens[self.pos].type
            self.eat(op)
            right = self.term()
            result = result + right if op == 'MAIS' else result - right
        return result

    def term(self):
        result = self.factor()
        while self.pos < len(self.tokens) and self.tokens[self.pos].type in ('MULT', 'DIV'):
            op = self.tokens[self.pos].type
            self.eat(op)
            right = self.factor()
            result = result * right if op == 'MULT' else result // right
        return result

    def factor(self):
        if self.tokens[self.pos].type == 'NUMERO':
            value = self.tokens[self.pos].value
            self.eat('NUMERO')
            return value
        elif self.tokens[self.pos].type == 'LPAREN':
            self.eat('LPAREN')
            value = self.expr()
            self.eat('RPAREN')
            return value
        else:
            raise SyntaxError(f"Token inesperado: {self.tokens[self.pos].type}")

if __name__ == "__main__":
    while True:
        try:
            expr = input("Digite uma expressão: ").strip()
            if not expr:
                break
            lexer.input(expr)
            tokens = list(lexer)
            print("Tokens:", tokens)
            parser = LL1Parser(tokens)
            print("Resultado:", parser.parse())
        except Exception as e:
            print("Erro:", e)
