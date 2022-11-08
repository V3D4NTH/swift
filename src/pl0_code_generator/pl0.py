from src.pl0_code_generator.const import *


class Pl0:

    def __init__(self, abstract_syntax_tree) -> None:
        self.code = []
        self.ast = abstract_syntax_tree

    def generate_instruction(self, inst_name, param1, param2):
        self.code.append([inst_name, param1, param2])

    def generate_code(self):
        self.generate_instruction(Inst.lit.value, 0, 0)
        self.generate_instruction(Inst.opr.value, Op.eq.value, 1)

    def print_code(self):
        for index, c in enumerate(self.code):
            print(index, "", c[0], c[1], c[2])
