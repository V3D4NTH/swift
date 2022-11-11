#  date: 11. 11. 2022
#  author: Daniel Schnurpfeil
#
from src.pl0_code_generator.const import Inst as t, Op as o


def inst(instruction: t):
    """
    It takes an instruction and returns its value

    :param instruction: The instruction to be executed
    :type instruction: t
    :return: The value of the instruction.
    """
    return instruction.value


def op(operation: o):
    """
    Return the value of the operation.

    :param operation: The operation to perform
    :type operation: o
    :return: The value of the operation.
    """
    return operation.value
