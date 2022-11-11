#  date: 8. 11. 2022
#  authors: Daniel Schnurpfeil,  Jiri Trefil
#

import ply.lex
import ply.yacc as yy
import src.syntax_analyzer as syntax
import src.lex_analyzer as lexical
import src.pl0_code_generator as gen


if __name__ == '__main__':
    with open("../sample_input/func_simple.swift") as f:
        code = f.read()
    # Parsing the code_input.
    lexer = ply.lex.lex(module=lexical)
    y = yy.yacc(module=syntax, debug=False)
    ast = y.parse(code)

    # Generating the code for the PL/0 compiler.
    generated_code = gen.Pl0(ast)
    generated_code.generate_code()
    generated_code.print_code()

    ply.lex.runmain(lexer, code)
    print(ast.get_ascii(attributes=["name", "dist", "label", "complex"]))
    print(ast)
