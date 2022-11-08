# generic node of AST tree
class Node:
    def __init__(self, node_type, children=None):
        self.__type = node_type
        if children is None:
            self.__children = []
        else:
            self.__children = children

    def __str__(self):
        return self.__type

    def get_children(self):
        return self.__children

    def get_type(self):
        return self.__type

    def add_child_node(self, node):
        self.__children.append(node)


