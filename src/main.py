#  date: 8. 11. 2022
#  authors: Daniel Schnurpfeil,  Jiri Trefil
#
import sys

import ply.lex
import ply.yacc as yy
import src.syntax_analyzer as syntax
import src.lex_analyzer as lexical
import src.pl0_code_generator as gen
from src.syntax_analyzer.utils import generate_table_of_symbols


def main(input_file_name: str):
    with open(input_file_name) as f:
        code = f.read()
    print("input_code:")
    print(code)
    code = code.replace("\n", " ")
    # Parsing the code_input.
    lexer = ply.lex.lex(module=lexical)
    y = yy.yacc(module=syntax, debug=True)
    dst = y.parse(code)


    # with open("../output/tokens.txt", mode="w") as f:
    #     sys.stdout = f
    #     ply.lex.runmain(lexer, code)
    # sys.stdout = sys.__stdout__
    print(dst.get_ascii(attributes=["name", "dist", "label", "complex"]))
    print(dst)
    table_of_symbols = {}
    generate_table_of_symbols(table_of_symbols, symbols=dst.get_leaves())

    # Generating the code for the PL/0 compiler.
    #generated_code = gen.Pl0(dst, table_of_symbols)
    #generated_code.generate_code(sub_tree=generated_code.clear_tree(generated_code.ast.iter_prepostorder()))
    # It prints the symbol table and the generated code.
    #generated_code.print_symbol_table()
    print("----------generated code------------")
    #generated_code.print_code()
    print("------------------------------------")
    return ""


if __name__ == '__main__':
    main("../sample_input/program.swift")
