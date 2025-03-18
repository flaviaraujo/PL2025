import sys
import ply.lex as lex

# Lista de tokens
tokens = (
    'SELECT', 'WHERE', 'LIMIT', 'VAR', 'PRED', 'NUMBER', 'DOT', 'STRING', 'LCURLY', 'RCURLY', 'COMMENT'
)

def t_SELECT(t):
    r'(?i:select)'
    return t

def t_WHERE(t):
    r'(?i:where)'
    return t

def t_LIMIT(t):
    r'(?i:limit)'
    return t

def t_VAR(t):
    r'\?\w+'
    return t

def t_PRED(t):
    r'\w+(:\w+)?'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\"([^\"]*)\"(@\w+)?'
    return t

t_DOT = r'\.'
t_LCURLY = r'\{'
t_RCURLY = r'\}'

def t_COMMENT(t):
    r'\#.*'
    pass

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print(f'Caractere ilegal: {t.value[0]}')
    t.lexer.skip(1)

lexer = lex.lex()

if __name__ == "__main__":
    lexer.input(sys.stdin.read())
    for tok in lexer:
        print(tok)
