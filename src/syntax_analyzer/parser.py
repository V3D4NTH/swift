from src.lex_analyzer.lexer import *
#vytahnu tokeny, ktere jsem zadefinoval
'''
syntakticky parser, pouziva lex pro semanticke vyhodnoceni 
hodne work in progess
lexer provadi lexikalni analyzu a evaluaci hodnoty integeru a boolu
TODO JT debug pravidel gramatiky
'''
#set priority of operations - plus minus multiply and divide will branch out the tree to the left
#the cfg is ambigous, therefore precende must be defined
precedence = (('left','plus','minus'),('left','multiply','divide'))
#entry point of program, the 'root' of the tree
def p_program(p):
    'program : dekl_list'
    p[0] = p[1]
#program is just a bunch of declaration statements, this is the core of the grammar
#declartion can produce functions, variables and general expressions, such as function calls or math expressions
def p_dekl_list(p):
    '''
    dekl_list : dekl
              | expression
              | dekl dekl_list
              | block

    '''

    if len(p) == 2:
        p[0] = p[1]
#declaration statement
#here we declare variable, constant or a function
def p_dekl(p):
    '''
    dekl :   var var_dekl
    | let var_dekl
    | fun_dekl
    '''
    if len(p) == 2:
        p[0] = {'operation':'function_declaration','val':p[1]}
    elif len(p) == 3:
        p[0] = {'operation':'declaration','val':p[2]}

#variable declaration
def p_var_dekl(p):
    '''
    var_dekl : id ddot dtype semicolon
    | id ddot dtype equals expression semicolon
    '''
    p[0] = {'operation':'var_declaration','val': {'var': p[1], 'dtype': p[3], 'value': 0}}
    if len(p) > 5:
        p[0]['val']['value'] = p[5]

#data type, can be expanded in the future, so far our language accepts only integers and booleans
def p_dtype(p):
    '''
    dtype : int
    | bool
    '''
    p[0] = p[1]
#general expression - math expressions, variable assignments, functions calls, ...



def p_expression(p):
    '''
    expression : expression minus term
    | expression plus term
    | term
    '''
    if len(p) == 2:
        p[0] = p[1]
    elif p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]

def p_term(p):
    '''
    term : term multiply factor
    |  term divide factor
    | factor
    '''
    if len(p) == 2:
        p[0] = p[1]
    elif p[2] == '*':
       p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] // p[3]

def p_factor(p):
    '''
    factor : lparent expression rparent
    | minus expression
    | val
    | call
    '''
    if len(p) == 4:
        p[0] = p[2]
    elif len(p) == 3:
        p[0] = -p[1]
    elif len(p) == 2:
        p[0] = p[1]

#empty rule, do nothing
def p_empty(p):
    'empty : '
    pass
#function call rule, tree node stores operation and value
#value contains id of called function and function arguments
def p_call(p):
    '''
    call : id lparent arguments rparent semicolon
         | id lparent rparent semicolon
    '''
    p[0] = {'operation':'function_call','val':{'var':p[1]}}
    if len(p) == 6:
        p[0]['val']['args'] = p[3]
#generic rule for value, that is integer or identifier
def p_val(p):
    '''
    val : int
    |   id
    '''
    p[0] = p[1]
#rule for function declaration
#node contains operation and val, val contains the relevant information about function, such as name, params, body and return type
#    'fun_dekl : func id lparent params rparent arrow dtype comp_block'

def p_fun_dekl(p):
    '''
    fun_dekl : func id lparent params rparent arrow dtype comp_block

    '''
    p[0] = {'operation':'function_signature', 'val':{'var':p[2],'params':p[4],'return_type':p[7], 'body':p[8]}}

#rule for function parameters, ie (<this>)
def p_params(p):
    '''
    params : params_var
    | empty
    '''
    p[0] = p[1]
#function parameter declaration
#initial variable value set to 0
def p_params_var(p):
    '''
    params_var : id ddot dtype comma params_var
               | id ddot dtype
    '''
    p[0] = {'operation':'parameter_declaration', 'val':{'var':p[1], 'dtype':p[3], 'val':0}}

#function arguments rule, multiple values separated by comma
def p_arguments(p):
    '''
    arguments : val comma arguments
    |   val
    '''
    p[0] = p[1]

#compound block rule, ie {<block>}
def p_comp_block(p):
    '''
    comp_block : lcparent block rcparent
    '''
    p[0] = p[2]


#generic block statement rule
def p_block(p):
    '''
    block : comp_block block
        | loop_block block
        | cond_block block
        | ass_exp semicolon block
        | dekl block
        | return expression semicolon
    '''
    if len(p) == 4 and p[1] == 'return':
        p[0] = {'operation':'return_statement','val':{'val':p[2]}}
    else:
        p[0] = p[1]


#loop statement, only for cycle for now, will be expanded in future
def p_loop_block(p):
    '''
    loop_block : for lparent loop_var condition semicolon step semicolon rparent
    '''
    p[0] = {'operation' : 'for_loop','val':{'var':p[3],'condition':p[4],'step':p[6],'body':p[9]}}
# condition block, if or if else statement. Switch-case might be added in future
def p_cond_block(p):
    '''
    cond_block : if lparent condition rparent comp_block
    |            if lparent condition rparent comp_block else comp_block
    '''
    p[0] = {'operation':'if_stmt', 'val':{'condition':p[3],'body':p[5]}}
    if len(p) == 8:
        p[0]['operation'] = 'if_else_stmt'
        p[0]['val']['else_body'] = p[7]

#loop variable responsible for loop behavior
def p_loop_var(p):
    '''
    loop_var : var_dekl
    | id
    '''
    p[0] = p[1]
# step in for loop
def p_step(p):
    '''
    step : id add int
    | id sub int
    '''
    if p[2] == '+':
        p[0] += p[3]
    elif p[2] == '-':
        p[0] -= p[3]


#condition statement
def p_condition(p):
    '''
    condition : expression relation_operator expression
    '''
    p[0] = {'operation':'condition','val':{'left_side':p[1],'right_side':p[3],'relation':p[2]}}
# assignment expresion
#either a declaration of variable and assigning a value or assigning value to existing variable
def p_ass_expression(p):
    '''
    ass_exp : var id ddot dtype equals expression
    |   let id ddot dtype equals expression
    | id equals expression
    '''
    if len(p) == 4:
        p[0] = {'operation':'assignment','val':{'var':p[1],'val':p[3]}}
    elif len(p) == 7:
        p[0] = {'operation':'declaration_assign','val':{'var':p[2],'dtype':p[4],'value':p[6]}}
def p_relation_operator(p):
    '''
    relation_operator : equals_equals
    | lt
    | gt
    | le
    | ge
    | not_equal
    '''
    p[0] = p[1]
#todo error handler
def p_error(p):
    if not p:
        print(f"syntax error {p}")



