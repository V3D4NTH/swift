#  date: 8. 11. 2022
#  author: Daniel Schnurpfeil
#

from enum import Enum


# It's a class that holds the constants used by the PL/0 compiler
class Pl0Const:

    def __init__(self):
        self.reserved = ['=', '==', '+=', '-=', '+', '-', '/', '*', ';', '(', ')', '<', '!=', '<=', '>', '>=', '->',
                         '}',
                         '{', ':',
                         ',', 'Int', 'var', 'let']

        self.types = [int]

        self.expressions = {"expression_sum": self.gen_opr_add, "expression_minus": self.gen_opr_sub,
                            "expression_multiply": self.gen_opr_mul, "expression_divide": self.gen_opr_div,
                            "expression_term": self.gen_term}

        self.var_modifications = {"-=": self.gen_sub, "+=": self.gen_add, "*=": self.gen_mulby,
                                  "/=": self.gen_divby, "=": self.gen_equals}

        self.cond_expressions = {"<": self.gen_lesser, "!=": self.gen_not_equal, "<=": self.gen_lesser_equals,
                                 ">": self.gen_greater, ">=": self.gen_greater_equals, "==": self.gen_dos_equals, }

    def gen_lesser(self):
        raise NotImplementedError("Method not yet implemented.")

    def gen_not_equal(self):
        raise NotImplementedError("Method not yet implemented.")

    def gen_lesser_equals(self):
        raise NotImplementedError("Method not yet implemented.")

    def gen_greater(self):
        raise NotImplementedError("Method not yet implemented.")

    def gen_greater_equals(self):
        raise NotImplementedError("Method not yet implemented.")

    def gen_dos_equals(self):
        raise NotImplementedError("Method not yet implemented.")

    def gen_sub(self, operator):
        raise NotImplementedError("Method not yet implemented.")

    def gen_add(self, operator):
        raise NotImplementedError("Method not yet implemented.")

    def gen_mulby(self, operator):
        raise NotImplementedError("Method not yet implemented.")

    def gen_divby(self, operator):
        raise NotImplementedError("Method not yet implemented.")

    def gen_equals(self, operator):
        raise NotImplementedError("Method not yet implemented.")

    def gen_term(self, operator):
        """
        It adds two numbers.

        :param const1: The first constant to add
        :param const2: The second constant to add to the first
        """
        raise NotImplementedError("Method not yet implemented.")

    def gen_opr_add(self, const1, const2):
        """
        It adds two numbers.

        :param const1: The first constant to add
        :param const2: The second constant to add to the first
        """
        raise NotImplementedError("Method not yet implemented.")

    def gen_opr_sub(self, const1, const2):
        """
        It subtracts two numbers.

        :param const1: The first constant to be used in the operation
        :param const2: The constant to be subtracted from
        """
        raise NotImplementedError("Method not yet implemented.")

    def gen_opr_mul(self, const1, const2):
        """
        It generates a new constant
        that is the product of two other constants

        :param const1: The first constant to be multiplied
        :param const2: The second constant to be multiplied
        """
        raise NotImplementedError("Method not yet implemented.")

    def gen_opr_div(self, const1, const2):
        """
        It divides two numbers.

        :param const1: The first constant to be used in the operation
        :param const2: The constant to divide by
        """
        raise NotImplementedError("Method not yet implemented.")


# This class is used to store information about a symbol in table
class SymbolRecord:

    def __init__(self, name, symbol_type, const=False, level=0, address=3, size=0,
                 params=None, return_type=None, param=False, locals_vars=None):
        """
        This function initializes the symbol record

        :param name: The name of the symbol
        :param symbol_type: The type of the symbol
        :param const: True if the symbol is a constant, defaults to False (optional)
        :param level: the level of the symbol (0 for global, 1 for local, etc.), defaults to 0 (optional)
        :param address: The address of the symbol in memory, defaults to 0 (optional)
        :param size: size of the variable in bytes, defaults to 0 (optional)
        :param params: a list of parameters
        :param return_type: The return type of the function
        :param param: name of the variable, defaults to False (optional)
        """
        self.id = id(self)
        self.name = name
        self.type = symbol_type
        self.const = const
        self.level = level
        self.address = address
        self.size = size
        self.param = param
        if self.type == "func":
            self.params = params
            self.return_type = return_type
            self.locals = locals_vars

    def __str__(self):
        ret_val = ""
        ret_val += "--------record------\n"
        ret_val += (str(self.id) + "\t|" + "id\n")
        ret_val += (str(self.name) + "\t\t\t\t|" + "name\n")
        ret_val += (str(self.type) + "\t\t\t|" + "symbol_type\n")
        ret_val += (str(self.const) + "\t\t\t|" + "const\n")
        ret_val += (str(self.level) + "\t\t\t\t|" + "level\n")
        ret_val += (str(self.address) + "\t\t\t\t|" + "address\n")
        ret_val += (str(self.size) + "\t\t\t\t|" + "size\n")
        if self.type == "func":
            ret_val += (str(self.return_type) + "\t\t\t\t|" + "return_type\n")
        if self.param:
            ret_val += (str(self.param) + "\t\t\t\t|" + "param\n")
        ret_val += "--------------------\n"
        return ret_val


# > The `Inst` class is an enumeration of the instructions that the PL/0 compiler will generate
class Inst(Enum):
    lit = "LIT"
    opr = "OPR"
    lod = "LOD"
    sto = "STO"
    cal = "CAL"
    ret = "RET"
    int = "INT"
    jmp = "JMP"
    jmc = "JMC"


# The Op class is an enumeration of the possible operations that can be performed on the stack.
class Op(Enum):
    """
    1    unary minus
    2    +
    3    -
    4    *
    5    div - /
    6    mod - modulo  %
    7    odd 1,2,3,5... test
    8    equality
    9    unequality <>
    10    <
    11    >=
    12    >
    13    <=
    """
    # Defining the operations that can be performed on the stack.
    neg = 1
    add = 2
    sub = 3
    mul = 4
    div = 5
    mod = 6
    odd = 7
    eq = 8
    ne = 9
    lt = 10
    ge = 11
    gt = 12
    le = 13
