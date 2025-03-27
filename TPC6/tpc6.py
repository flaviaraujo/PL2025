import re

def tokenize(expression):
    expression = expression.replace(" ", "")
    tokens = re.findall(r'\d+|[()+\-*/]', expression)
    return tokens + ['$']

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def lookahead(self):
        return self.tokens[self.pos]
    
    def match(self, expected):
        if self.lookahead() == expected:
            self.pos += 1
        else:
            raise SyntaxError(f"Erro de sintaxe: esperado '{expected}', mas encontrado '{self.lookahead()}' na posição {self.pos}")

    def expr(self):
        """ expr -> term expr_cont """
        value = self.term()
        return self.expr_cont(value)
    
    def expr_cont(self, inherited_value):
        """ expr_cont -> ('+' | '-') term expr_cont | vazio """
        if self.lookahead() in ('+', '-'):
            op = self.lookahead()
            self.match(op)
            value = self.term()
            if op == '+':
                inherited_value += value
            else:
                inherited_value -= value
            return self.expr_cont(inherited_value)
        return inherited_value
    
    def term(self):
        """ term -> factor term_cont """
        value = self.factor()
        return self.term_cont(value)
    
    def term_cont(self, inherited_value):
        """ term_cont -> ('*' | '/') factor term_cont | vazio """
        if self.lookahead() in ('*', '/'):
            op = self.lookahead()
            self.match(op)
            value = self.factor()
            if op == '*':
                inherited_value *= value
            else:
                inherited_value //= value 
            return self.term_cont(inherited_value)
        return inherited_value
    
    def factor(self):
        """ factor -> NUM | '(' expr ')' """
        if self.lookahead().isdigit():
            value = int(self.lookahead())
            self.match(self.lookahead())
            return value
        elif self.lookahead() == '(':
            self.match('(')
            value = self.expr()
            self.match(')')
            return value
        else:
            raise SyntaxError(f"Token inesperado: {self.lookahead()}")

    def parse(self):
        result = self.expr()
        if self.lookahead() != '$':
            raise SyntaxError("Entrada inválida. Tokens restantes após análise.")
        return result

if __name__ == "__main__":
    while True:
        try:
            expr = input("Digite uma expressão: ").strip()
            if not expr:
                break
            tokens = tokenize(expr)
            print("Tokens:", tokens)
            parser = Parser(tokens)
            result = parser.parse()
            print("Resultado:", result)
        except Exception as e:
            print("Erro:", e)