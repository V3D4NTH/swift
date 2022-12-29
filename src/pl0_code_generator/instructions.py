#  date: 29. 12. 2022
#  author: Daniel Schnurpfeil
#
from enum import Enum


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


def inst(instruction: Inst):
    """
    It takes an instruction and returns its value

    :param instruction: The instruction to be executed
    :type instruction: t
    :return: The value of the instruction.
    """
    return instruction.value


def op(operation: Op):
    """
    Return the value of the operation.

    :param operation: The operation to perform
    :type operation: o
    :return: The value of the operation.
    """
    return operation.value
