import ply.lex as lex

tokens = (
    'LET', 'IDENTIFIER', 'TYPE', 'EQUALS', 'SEMICOLON', 'PRINT',
    'LPAREN', 'RPAREN', 'INT', 'BOOL', 'INT_OP', 'BOOL_OP', 'NOT', 'COLON'
)

t_LET = r'let'
t_EQUALS = r'='
t_SEMICOLON = r';'
t_PRINT = r'print'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_INT_OP = r'\+|\-|\*|\/'
t_BOOL_OP = r'&&|\|\|'
t_NOT = r'!'
t_COLON = r':'
t_ignore = ' \t'

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value == 'let':
        t.type = 'LET'
    elif t.value == 'print':
        t.type = 'PRINT'
    elif t.value in ('int', 'bool'):
        t.type = 'TYPE'
    elif t.value in ('true', 'false'):
        t.type = 'BOOL'
        t.value = (t.value == 'true')
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
