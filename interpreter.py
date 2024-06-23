from parser import parser
from type_checker import type_check, symbol_table

def evaluate_expression(node):
    if node[0] == 'int':
        return node[1]
    elif node[0] == 'bool':
        return node[1]
    elif node[0] == 'identifier':
        return symbol_table[node[1]]
    elif node[0] == 'binop':
        op = node[1]
        left = evaluate_expression(node[2])
        right = evaluate_expression(node[3])
        if op == '+':
            return left + right
        elif op == '-':
            return left - right
        elif op == '*':
            return left * right
        elif op == '/':
            return left / right
        elif op == '&&':
            return left and right
        elif op == '||':
            return left or right
    elif node[0] == 'not':
        return not evaluate_expression(node[1])

def execute_statement(node):
    if node[0] == 'let':
        var_name = node[1]
        expr = node[3]
        value = evaluate_expression(expr)
        symbol_table[var_name] = value
    elif node[0] == 'print':
        expr = node[1]
        value = evaluate_expression(expr)
        print(value)

def execute_program(program):
    for statement in program:
        execute_statement(statement)

if __name__ == "__main__":
    program_code = '''
    let x: int = 5;
    let y: int = x + 10;
    let z: bool = true && false;
    print(x + y);
    print(z);
    '''
    parsed_program = parser.parse(program_code)
    if parsed_program:
        for statement in parsed_program:
            type_check(statement)
        execute_program(parsed_program)
