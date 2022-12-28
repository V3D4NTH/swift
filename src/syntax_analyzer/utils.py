#  date: 11. 11. 2022
#  author: Daniel Schnurpfeil
#

from ete3 import Tree

from src.pl0_code_generator import SymbolRecord

#[JT] lineno = number of line where the statement is declared
def make_node(node_name: str, children=None,lineno=0) -> Tree:
    """
    It takes a node name and a list of children, and returns a tree

    :param node_name: The name of the node
    :type node_name: str
    :param children: A list of children to add to the node
    :return: A tree with the name of the node and the children
    """
    ast = Tree(name=node_name,support=lineno)

    if children is None:
        return ast
    for i in children:
        if i.__class__.__name__ == 'TreeNode':
            ast.add_child(child=i)
        else:
            ast.add_child(name=i)
    return ast

# wrapper function that checks if node represents numerical value
# returns true if leaf is an integer
def is_integer(node):
    leafs = node.get_leaf_names()
    if len(leafs) > 1:
        return False
    return isinstance(node.get_leaf_names()[0],int)

def get_integer_node_value(node):
    return node.get_leaf_names()[0]


def find_real_level(symbols, index):
    real_level_result = 0
    for i in symbols[index].get_ancestors():
        if i.name == "compound_block":
            real_level_result += 1
    return real_level_result


def find_entry_in_symbol_table(symbol_table,level,real_level,symbol_name):
    #[JT] global scope
    if real_level == 0:
        return symbol_table[symbol_name]
    #[JT] we are searching for entry of identifier in glob al scope
    if level == 0:
        #[JT] we are indented in some block
        #start searching bottom - up in indented scopes
        scope_count = len(symbol_table['_scopes'])
        while real_level > 0:
            #no variables are indented in this block, the symbol must exist in global scope
            if scope_count == 0:
                break
            real_level -= 1
            #current identation does not have any local variables, go up
            if real_level >= scope_count:
                continue
            indent_dic = symbol_table['_scopes'][real_level]
            if symbol_name in indent_dic:
                return indent_dic[symbol_name]
        #we did not find the variable in indented blocks => it must be in global scope
        return symbol_table[symbol_name]
    else:
        #retrieve variables in the function block
        function_symbol_table = symbol_table[level]
        scope_count = len(function_symbol_table.locals) if function_symbol_table.locals is not None else 0
        #again we have to search bottom up from our current indentation
        while real_level > 0:
            real_level -= 1
            if real_level >= scope_count:
                continue
            indent_dic = function_symbol_table.locals[real_level]
            if symbol_name in indent_dic:
                return indent_dic[symbol_name]
            #if we did not find the variable indented, then the variable must be a parameter or in global scope
        return function_symbol_table.params[symbol_name] if symbol_name in function_symbol_table.params \
            else symbol_table[symbol_name]

def generate_table_of_symbols(symbol_table, symbols: list, level="0", real_level=0, address=3, index=0):
    """
        It generates a table of symbols
        """
    position_in_tree = index
    index = 0
    #[JT] indented scopes in global scope
    symbol_table["_scopes"] = []
    while index < len(symbols):
        ancestor = symbols[index].get_ancestors()[0]
        if ancestor.name == "function_signature":
            real_level = find_real_level(symbols, index)
            if symbols[index].name in symbol_table.keys():
                raise Exception("Duplicate symbol:", symbols[index].name, "in", symbol_table.keys())
            params = {}
            local_address = 3
            ids_and_types = symbols[index].get_sisters()[0].get_leaf_names()
            if len(ids_and_types) > 1:
                for i in range(0, len(ids_and_types), 2):
                    if ids_and_types[i] in params.keys():
                        raise Exception("Duplicate symbol:", ids_and_types[i], "in", params.keys())
                    params[ids_and_types[i]] = (
                        SymbolRecord(ids_and_types[i], ids_and_types[i + 1], param=True, level=level,tree_position=position_in_tree+index,
                                     real_level=real_level,
                                     address=local_address))

                    local_address += 1
            func_name = symbols[index].name
            symbol_table[func_name] = (
                SymbolRecord(symbols[index].name, "func", params=params, level=level, real_level=real_level,tree_position=position_in_tree+index,
                             address=address,
                             return_type=symbols[index].get_sisters()[1].get_leaf_names()[0]))
            address += 1
            func_body = symbols[index].get_sisters()[2].get_leaves()
            # shifting index to skip duplicates
            index += len(func_body)
            # recursive call
            generate_table_of_symbols(symbol_table, level=symbol_table[func_name].name, real_level=real_level,
                                      symbols=func_body, address=local_address, index=index)
        if ancestor.name == "var_declaration_expression":
            real_level = find_real_level(symbols, index)
            if level != "0" and symbol_table[level].locals is None:
                #slovniky lokalnich promennych podle urovne zanoreni v tele fce
                symbol_table[level].locals = []
                #pushni do stacku scope fce
                symbol_table[level].locals.append({symbols[index].name: (SymbolRecord(symbols[index].name,
                                                                                 symbol_type=
                                                                                 symbols[index].get_sisters()[0].
                                                                                 children[0].name,
                                                                                 level=level,
                                                                                 real_level=real_level,
                                                                                 tree_position=position_in_tree+index,
                                                                                 address=address))})
                if ancestor.get_sisters()[0].name == "let":
                    symbol_table[level].locals[real_level-1][symbols[index].name].const = True
            #deklaruju promennou, ktera neni na globalni urovni
            elif level != "0":
                #vstupuje novy vnoreny scope, vlozim do zasobniku
                if real_level > len(symbol_table[level].locals):
                    symbol_table[level].locals.append({})
                current_scope_dic = symbol_table[level].locals[real_level-1]
                if symbols[index].name in current_scope_dic.keys():
                    raise Exception("Duplicate symbol:", symbols[index].name, "in", current_scope_dic.keys())
                current_scope_dic[symbols[index].name] = (SymbolRecord(symbols[index].name,
                                                                                 symbol_type=
                                                                                 symbols[index].get_sisters()[0].
                                                                                 children[0].name,
                                                                                 level=level,
                                                                                 real_level=real_level,
                                                                                 tree_position=position_in_tree + index,
                                                                                 address=address))
                if ancestor.get_sisters()[0].name == "let":
                    current_scope_dic[symbols[index].name].const = True
            else:
                #vytvorim zasabni pro mozne vnorene scopes v globalnim scopeu
                #if len(symbol_table.keys()) == 0:
                #    symbol_table["_scopes"] = []
                dic = symbol_table
                if real_level != 0:
                    if real_level > len( symbol_table["_scopes"]):
                        symbol_table["_scopes"].append({})
                    dic = symbol_table["_scopes"][real_level-1]
                #spravne semanticka chyba pri vytvareni zaznamu -> bijou se nazvy v globalnim scopeu
                if symbols[index].name in dic.keys():
                    raise Exception("Duplicate symbol:", symbols[index].name, "in", symbol_table.keys())
                dic[symbols[index].name] = (SymbolRecord(symbols[index].name,
                                                                  symbol_type=symbols[index].get_sisters()[0].
                                                                  children[0].name,
                                                                  level=level,
                                                                  real_level=real_level,
                                                                  tree_position=position_in_tree + index,
                                                                  address=address))

                if ancestor.get_sisters()[0].name == "let":
                    dic[symbols[index].name].const = True
            address += 1
        index += 1
