#klicove slova jazyku, pripadne muzeme rozsirit
keywords = (
    'let', 'var', 'func', 'for', 'while', 'return', 'if', 'else', 'and', 'or'
)
#tokeny, mely by pokryt vsechno, pripadne muzem rozsirit
tokens = keywords + (
    'equals', 'equals_equals', 'plus', 'minus', 'divide', 'multiply', 'int',
    'bool', 'id', 'semicolon', 'rparent', 'lparent', 'lt', 'le', 'gt',
    'ge', 'arrow', 'rcparent', 'lcparent','newline','ddot','comma','add', 'sub','not_equal'
)
#mnozina tokenu a rezervovanych slov
reserved_set = set(tokens)


# chytam identifikatory
# pokud je identifikator klicove slovo, zachyt to do typu
def t_id(t):
    r'[A-Za-z][A-Za-z0-9\_]*'
    if t.value in reserved_set:
        t.type = t.value
    return t

#token newline -> inkrementuj line number
def t_newline(t):
    r'\n'
    t.lexer.lineno += 1
    return t
#neznamy token, zahlas chybu
def t_error(t):
    print(f"Unknown token: {t.value[0]}")
    t.lexer.skip(1)
#zadefinuj token jako funkci - umozni k tomu pribalit nejaky vykonny kod
def t_int(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print(f"Number {t.value} is not integer.")
        t.lexer.skip(1)
    return t
#todo
#booleany - mozna lepsi narvat tam 1 if t.value is true else 0
def t_bool(t):
    r'true|false'
    t.value = bool(t.value)


#tokeny popsane reg. vyrazy

t_equals = r'='
t_equals_equals = r'=='
t_add = r'\+='
t_sub = r'\-='
t_plus = r'\+'
t_minus = r'\-'
t_divide = r'\/'
t_multiply = r'\*'
t_semicolon = r'\;'
t_lparent = r'\('
t_rparent = r'\)'
t_lt = r'\<'
t_not_equal = r'!='
t_le = r'\<\='
t_gt = r'\>'
t_ge = r'\>\='
t_arrow = r'\-\>'
t_rcparent = r'\}'
t_lcparent = r'\{'
t_ddot = r'\:'
t_comma = r'\,'
#tabulatory a mezery nas nezajimaji
t_ignore = r' \t'


'''
data = '{return 5;}'



lexer.input(data)
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)
'''