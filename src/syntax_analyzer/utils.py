#  date: 11. 11. 2022
#  author: Daniel Schnurpfeil
#

from ete3 import Tree

from src.pl0_code_generator import SymbolRecord


def make_node(node_name: str, children=None) -> Tree:
    """
    It takes a node name and a list of children, and returns a tree

    :param node_name: The name of the node
    :type node_name: str
    :param children: A list of children to add to the node
    :return: A tree with the name of the node and the children
    """
    ast = Tree(name=node_name)

    if children is None:
        return ast
    for i in children:
        if i.__class__.__name__ == 'TreeNode':
            ast.add_child(child=i)
        else:
            ast.add_child(name=i)
    return ast


def generate_table_of_symbols(symbol_table, symbols: list, level="0", ):
    """
        It generates a table of symbols
        """
    symbols = symbols
    level = level
    index = 0
    address = 3
    while index < len(symbols):
        ancestor = symbols[index].get_ancestors()[0]
        if ancestor.name == "function_signature":
            if symbols[index].name in symbol_table.keys():
                raise Exception("Duplicate symbol:", symbols[index].name, "in", symbol_table.keys())
            params = {}

            ids_and_types = symbols[index].get_sisters()[0].get_leaf_names()
            if len(ids_and_types) > 1:
                for i in range(0, len(ids_and_types), 2):
                    if ids_and_types[i] in params.keys():
                        raise Exception("Duplicate symbol:", ids_and_types[i], "in", params.keys())
                    params[ids_and_types[i]] = (
                        SymbolRecord(ids_and_types[i], ids_and_types[i + 1], param=True, level=level,
                                     address=address))
                    address += 1
            func_name = symbols[index].name
            symbol_table[func_name] = (
                SymbolRecord(symbols[index].name, "func", params=params, level=level,
                             address=address,
                             return_type=symbols[index].get_sisters()[1].get_leaf_names()[0]))
            address += 1
            func_body = symbols[index].get_sisters()[2].get_leaves()
            # shifting index to skip duplicates
            index += len(func_body)
            # recursive call
            generate_table_of_symbols(symbol_table, level=symbol_table[func_name].name, symbols=func_body)
        if ancestor.name == "var_declaration_expression":
            if symbols[index].name in symbol_table.keys() and symbol_table[symbols[index].name].level == "0":
                raise Exception("Duplicate symbol:", symbols[index].name, "in", symbol_table.keys())
            if level != "0" and symbol_table[level].locals is None:
                symbol_table[level].locals = {symbols[index].name: (SymbolRecord(symbols[index].name,
                                                                                 symbol_type=
                                                                                 symbols[index].get_sisters()[0].
                                                                                 children[0].name,
                                                                                 level=level,
                                                                                 address=address))}
            elif level != "0" and symbols[index].name not in symbol_table[level].locals.keys():
                symbol_table[level].locals[symbols[index].name] = (SymbolRecord(symbols[index].name,
                                                                                symbol_type=
                                                                                symbols[index].get_sisters()[0].
                                                                                children[0].name,
                                                                                level=level,
                                                                                address=address))
                if ancestor.get_sisters()[0].name == "let":
                    symbol_table[level].locals[symbols[index].name].const = True
            else:
                symbol_table[symbols[index].name] = (SymbolRecord(symbols[index].name,
                                                                  symbol_type=symbols[index].get_sisters()[0].
                                                                  children[0].name,
                                                                  level=level,
                                                                  address=address))
                if ancestor.get_sisters()[0].name == "let":
                    symbol_table[symbols[index].name].const = True
            address += 1
        index += 1
    # create_levels(symbol_table)
