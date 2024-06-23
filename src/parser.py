import ply.yacc as yacc
from lexer import tokens

def p_program(p):
    '''program : statement_list'''
    p[0] = p[1]

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_statement(p):
    '''statement : let_statement
                 | print_statement'''
    p[0] = p[1]

def p_let_statement(p):
    '''let_statement : LET IDENTIFIER COLON TYPE EQUALS expression SEMICOLON'''
    p[0] = ('let', p[2], p[4], p[6])

def p_print_statement(p):
    '''print_statement : PRINT LPAREN expression RPAREN SEMICOLON'''
    p[0] = ('print', p[3])

def p_expression_binop(p):
    '''expression : expression INT_OP expression
                  | expression BOOL_OP expression'''
    p[0] = ('binop', p[2], p[1], p[3])

def p_expression_not(p):
    '''expression : NOT expression'''
    p[0] = ('not', p[2])

def p_expression_group(p):
    '''expression : LPAREN expression RPAREN'''
    p[0] = p[2]

def p_expression_identifier(p):
    '''expression : IDENTIFIER'''
    p[0] = ('identifier', p[1])

def p_expression_int(p):
    '''expression : INT'''
    p[0] = ('int', p[1])

def p_expression_bool(p):
    '''expression : BOOL'''
    p[0] = ('bool', p[1])

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()
