from lexer import lexer
from parser import parser
from type_checker import type_check, symbol_table
from interpreter import execute_program

def check_program(program_code):
    # Lexical analysis
    lexer.input(program_code)
    for tok in lexer:
        pass

    # Syntactic analysis
    parsed_program = parser.parse(program_code)
    
    # Type checking
    if parsed_program:
        type_errors = False
        for statement in parsed_program:
            if type_check(statement) is None:
                type_errors = True
        if type_errors:
            return False, parsed_program
        return True, parsed_program
    return False, None

if __name__ == "__main__":
    # Example program codes
    program_code1 = '''
    let x: int = 5;
    let y: int = x + 10;
    let z: bool = true && false;
    print(x + y);
    print(z);
    '''

    program_code2 = '''
    let a: int = 3;
    let b: int = 7;
    let c: int = a + b;
    print(c);
    '''

    program_code3 = '''
    let p: bool = true;
    let q: bool = false;
    let r: bool = p && q;
    print(r);
    '''

    program_code4 = '''
    let x: int = 5;
    let y: bool = x + 10;
    print(y);
    '''

    program_code5 = '''
    let x: int = 5;
    let y: int = x - 3;
    let z: int = y * 2;
    print(z);
    '''

    program_code6 = '''
    let x: int = 5;
    let y: int = 10;
    let result: bool = x + y;
    print(result);
    '''

    program_codes = [program_code1, program_code2, program_code3, program_code4, program_code5, program_code6]

    for i, program_code in enumerate(program_codes, 1):
        print(f"Checking program {i}:\n")
        print(program_code)
        success, parsed_program = check_program(program_code)
        
        if success:
            print("No type errors found. Executing program...\n")
            execute_program(parsed_program)
        else:
            print("Type errors were found in the program.\n")
        print("\n" + "="*40 + "\n")
