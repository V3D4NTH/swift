#  date: 8. 11. 2022
#  authors: Daniel Schnurpfeil,  Jiri Trefil
#
import os
from copy import copy

import ply.lex
import ply.yacc as yy
# from ete3 import TreeStyle

import src.syntax_analyzer as syntax
import src.lex_analyzer as lexical
import src.pl0_code_generator as gen
from src.syntax_analyzer.utils import generate_table_of_symbols


def generate_output_files(dst, generated_code):
    if "output" not in os.listdir("../"):
        os.mkdir("../output")
    with open("../output/full_tree.txt", mode="w") as tree:
        tree.writelines(dst.get_ascii(attributes=["name", "dist", "label", "complex"]))
    with open("../output/tree.txt", mode="w") as tree:
        tree.writelines(str(dst))
    with open("../output/symbol_table.txt", mode="w") as table:
        generated_code.print_symbol_table(table.writelines)


def main(input_file_name: str):
    """
    "This function takes a file name as input and returns a list of the words in the file."

    :param input_file_name: The name of the file that contains the input data
    :type input_file_name: str
    """

    with open(input_file_name) as f:
        code = f.read()
    # print("input_code:")
    # print(code)
    formatted_input_code = copy(code)
    code = code.replace("\n", " ")
    # Parsing the code_input.
    lexer = \
    ply.lex.lex(module=lexical)
    y = yy.yacc(module=syntax, debug=True)
    dst = y.parse(code)

    # Generating a table of symbols.
    table_of_symbols = {}
    generate_table_of_symbols(table_of_symbols, symbols=dst.get_leaves())
    generated_code = gen.Pl0(dst, table_of_symbols)

    # Generating the output files.
    generate_output_files(dst, generated_code)

    # Showing the tree. with pyqt5
    # tree_style = TreeStyle()
    # tree_style.show_leaf_name = True
    # tree_style.mode = "c"
    # tree_style.arc_start = -180  # 0 degrees = 3 o'clock
    # dst.show(
        # tree_style=tree_style
    # )

    # Generating the instructions for the PL/0 compiler.
    generated_code.generate_instructions()

    if generated_code.return_code() != "":
        # Writing the generated code to a file.
        with open("../output/generated_code.txt", mode="w") as txt:
            txt.writelines("----------input code----------------\n")
            txt.writelines(formatted_input_code)
            txt.writelines("\n")
            txt.writelines("----------generated code------------\n")
            txt.writelines(generated_code.return_code())
            txt.writelines("------------------------------------")

    return generated_code.return_code()


if __name__ == '__main__':
    main("../sample_input/program.swift")
