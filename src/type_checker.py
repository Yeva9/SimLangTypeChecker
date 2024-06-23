from parser import parser

symbol_table = {}

def type_check(node):
    if isinstance(node, tuple):
        if node[0] == 'let':
            var_name = node[1]
            var_type = node[2]
            expr = node[3]
            expr_type = type_check(expr)
            if var_type != expr_type:
                print(f"Type error: variable '{var_name}' declared as {var_type} but assigned a {expr_type}")
                return None
            else:
                symbol_table[var_name] = var_type
                return var_type
        elif node[0] == 'print':
            expr = node[1]
            expr_type = type_check(expr)
            if expr_type not in ('int', 'bool'):
                print(f"Type error: print statement has invalid type {expr_type}")
                return None
            return expr_type
        elif node[0] == 'binop':
            op = node[1]
            left = type_check(node[2])
            right = type_check(node[3])
            if op in ('+', '-', '*', '/'):
                if left != 'int' or right != 'int':
                    print(f"Type error: operator '{op}' requires integers")
                    return None
                return 'int'
            elif op in ('&&', '||'):
                if left != 'bool' or right != 'bool':
                    print(f"Type error: operator '{op}' requires booleans")
                    return None
                return 'bool'
        elif node[0] == 'not':
            expr = type_check(node[1])
            if expr != 'bool':
                print("Type error: operator '!' requires a boolean")
                return None
            return 'bool'
        elif node[0] == 'identifier':
            var_name = node[1]
            if var_name not in symbol_table:
                print(f"Type error: variable '{var_name}' is not declared")
                return 'unknown'
            return symbol_table[var_name]
        elif node[0] == 'int':
            return 'int'
        elif node[0] == 'bool':
            return 'bool'
    else:
        return 'unknown'

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
