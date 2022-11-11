from ete3 import Tree


def make_node(node_name: str, children=None) -> Tree:
    ast = Tree(name=node_name)

    if children is None:
        return ast
    for i in children:
        if i.__class__.__name__ == 'TreeNode':
            ast.add_child(child=i)
        else:
            ast.add_child(name=i)
    return ast