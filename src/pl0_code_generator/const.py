from enum import Enum


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


class Op(Enum):
    """
    1    unární minus
    2    +
    3    -
    4    *
    5    div - celočíselné dělení (znak /)
    6    mod - dělení modulo (znak %)
    7    odd - test zda je číslo liché
    8    test rovnosti (znak =)
    9    test nerovnosti (znaky <>)
    10    <
    11    >=
    12    >
    13    <=
    """
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
