import ply.yacc as yacc
import lexer as lex
#vytahnu tokeny, ktere jsem zadefinoval
from lexer import tokens
'''
syntakticky parser, pouziva lex pro semanticke vyhodnoceni 
hodne work in progess
lexer provadi lexikalni analyzu a evaluaci hodnoty integeru a boolu
'''
'''
TODO [JT] - vsechna pravidla gramatiky, vytvareni tabulky symbolu, trida pro reprezetnaci uzlu v AST
vysledek syntakticke/semanticke analyzy bude vnitrni reprezentace AST, ze ktereho bude nasledne mozne generovat PL/0
TODO [JT] vytvoreni tridy pro reprezentaci identifikatoru
'''
#tabulka symbolu
table = dict()
#delka kodu pl0 - pouzito pro generovani cisla radku prikazu
code_len = 0

def p_program(p):
    'program : dekl_list'
    p[0] = p[1]

def p_dekl_list(p):
    '''
    dekl_list : dekl
              | expr
              | dekl dekl_list
    '''

    if len(p) == 2:
        p[0] = p[1]

def p_dekl(p):
    '''dekl: var var_dekl'''


#prazdne pravidlo, pouzito u parametru fce
def p_empty(p):
    'empty:'
    pass






#todo error handler
def p_error(p):
    if not p:
        print("syntax error")

'''
CFG of Not so Swift language
[program] := [dekl_list]
[dekl_list] := [dekl] || [expr] || [dekl][dekl_list]
[dekl] := var [var_dekl]; || let [var_dekl];|| [fun_dekl]
[var_dekl] :=  id : [dtype] || id : [dtype] = [expr]
[fun_dekl] := func id([params]) -> [dtype][comp_block]
[params] := [params_var]|| empty
[params_var] :=  id : [dtype],[params_var] ||  id : [dtype]
[expr] := [term]+[term] || [term]-[term] || [term]
[term] := [expr] * [factor] || [exp] / [factor] || [factor]
[factor] := ([expr]) || -[exp] || [val] || [call]
[call] := id([arguments]); || id();
[arguments] := [val],[arguments] || [val]
[block] := [comp_block] || [loop_block] || [cond_block] || [ass_exp];[block] || return [expr];
[comp_block] := {[block]}
[loop_block] := for([loop_var];[condition];[step];)[comp_block]
[cond_block] := if([condition])[comp_block] || if([condition])[comp_block]else[comp_block]
[loop_var] := [var_dekl] || id
[step] := id += digit || id -= digit
[condition] := [expr] [relation_operator] [expr]
[ass_exp] :=  var id : [dtype] = [expr] || let id : [dtype] = [expr] || id = [expr]
[relation_operator] := == || < || > || >= || <= || !=
[val] := id || digit
[dtype] := int || bool
'''

