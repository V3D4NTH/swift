import ply.lex as lex

# Reserved words
reserved = (
    'FUNC', 'RETURN', 'IF', 'LET', 'WHILE', 'VAR',

    # Assignment (*=, /=, %=, +=, -=)
    'TIMES_EQUAL', 'DIV_EQUAL', 'MOD_EQUAL', 'PLUS_EQUAL', 'MINUS_EQUAL',
    'ARROW', 'EQUAL_EQUAL'
)
# Literals
literals = "+-*/%^<>=!?()[]{}.,;:\\\'\""

special_reserved = (
    'INT', 'ID', 'INT_LITERAL', 'OR', 'AND'

)
# Completely ignored characters
t_ignore = ' \t\x0c'
# Assignment operators
t_EQUAL_EQUAL = r'=='
t_TIMES_EQUAL = r'\*='
t_DIV_EQUAL = r'/='
t_MOD_EQUAL = r'%='
t_PLUS_EQUAL = r'\+='
t_MINUS_EQUAL = r'-='
t_ARROW = r'->'

tokens = reserved + special_reserved
# Identifiers and reserved words
reserved_map = {}
for r in reserved:
    reserved_map[r.lower()] = r


def t_NEWLINE(t):
    r"\n+"
    t.lexer.lineno += t.value.count("\n")


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


def t_INT_LITERAL(t):
    r'[\d]+'
    t.type = reserved_map.get(t.value, "INT_LITERAL")
    return t


def t_OR(t):
    r'\|\|'
    t.type = reserved_map.get(t.value, "OR")
    return t


def t_AND(t):
    r'&&'
    t.type = reserved_map.get(t.value, "AND")
    return t


def t_error(t):
    print("Illegal character %s" % repr(t.value[0]))
    t.lexer.skip(1)


lexer = lex.lex()
if __name__ == "__main__":
    with open("sample_input/sample.swift") as f:
        code = f.read()
    lex.runmain(lexer, code)
