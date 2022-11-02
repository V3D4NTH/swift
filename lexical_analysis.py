import ply.lex as lex

# Reserved words
reserved = (
    # todo
    'FUNC',

)

# Literals
special_reserved = (
    # todo
    'INT', 'ID',


)

tokens = reserved + special_reserved

# Completely ignored characters
t_ignore = ' \t\x0c'


def t_NEWLINE(t):
    r"\n+"
    t.lexer.lineno += t.value.count("\n")


# Data Types
t_INT = r'Int'

# Operators
# todo

# Assignment operators
# todo

# # Delimeters

literals = "+-*/%|&~^<>=!?()[]{}.,;:\\\'\""

# Identifiers and reserved words

reserved_map = {}
for r in reserved:
    reserved_map[r.lower()] = r


def t_comment(t):
    r'//.*'
    t.lexer.lineno += t.value.count('\n')


def t_ID(t):
    r'[A-Za-z_][\w_]*'
    t.type = reserved_map.get(t.value, "ID")
    return t


def t_error(t):
    print("Illegal character %s" % repr(t.value[0]))
    t.lexer.skip(1)


lexer = lex.lex()
if __name__ == "__main__":
    with open("sample_input/sample.swift") as f:
        code = f.read()
    lex.runmain(lexer, code)
