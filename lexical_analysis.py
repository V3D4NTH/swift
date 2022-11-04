import ply.lex as lex

# Reserved words
reserved = (
    'FUNC', 'RETURN', 'IF', 'LET', 'WHILE'

)

# Literals
special_reserved = (
    'INT', 'ID', 'NEW_LINE'


)

tokens = reserved + special_reserved

# Completely ignored characters
t_ignore = ' \t\x0c'


def t_NEW_LINE(t):
    r"\n+"
    t.lexer.lineno += t.value.count("NEW_LINE")
    return t


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

def t_Int(t):
    r'Int'
    t.type = reserved_map.get(t.value, "INT")
    return t


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
