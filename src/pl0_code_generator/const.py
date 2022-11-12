#  date: 8. 11. 2022
#  author: Daniel Schnurpfeil
#

from enum import Enum

reserved = ['=', '==', '+=', '-=', '+', '-', '/', '*', ';', '(', ')', '<', '!=', '<=', '>', '>=', '->', '}', '{', ':',
            ',', 'Int', 'var', 'let']

types = [int]


class SymbolRecord:

    def __init__(self, name, symbol_type, const=False, level=0, address=0, size=0):
        self.id = id(self)
        self.name = name
        self.type = symbol_type
        self.const = const
        self.level = level
        self.address = address
        self.size = size

    def __str__(self):
        print("--------record------")
        print(self.id, "\t|",  "id")
        print(self.name, "\t\t\t\t|",  "name")
        print(self.type, "\t\t\t|",  "symbol_type")
        print(self.const, "\t\t\t|",  "const")
        print(self.level, "\t\t\t\t|",  "level")
        print(self.address, "\t\t\t\t|",  "address")
        print(self.size, "\t\t\t\t|",  "size")
        print("--------------------")


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
