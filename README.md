# SimLangTypeChecker

## Program Overview

The program is designed to lexically analyze, parse, type-check, and execute code written in a custom programming language called SimLang. This process involves several steps:
1. **Lexical Analysis**: Tokenizes the input code into meaningful symbols.
2. **Syntactic Analysis (Parsing)**: Checks the syntax of the tokens and generates an Abstract Syntax Tree (AST).
3. **Semantic Analysis (Type Checking)**: Ensures that the operations in the code are semantically correct (e.g., variable types match their usage).
4. **Execution**: Runs the code based on the parsed and type-checked AST.

The program uses the PLY (Python Lex-Yacc) library for lexical and syntactic analysis.

## Steps to Activate the Virtual Environment and Run the Program

### 1. Activate the Virtual Environment

To activate your virtual environment, navigate to the project directory and run the following command:

```sh
source venv/bin/activate
```

This command activates the virtual environment, ensuring that all dependencies specified in the virtual environment are used.

### 2. Run the Python Script

Once the virtual environment is activated, you can run the main Python script to lexically analyze, parse, type-check, and execute the SimLang program:

```sh
python main.py
```

By following these steps, you will be able to execute the SimLang programs and see the results, including any type errors detected during the type-checking phase.
