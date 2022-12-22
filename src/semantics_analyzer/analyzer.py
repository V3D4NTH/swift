# class responsible from semantical analysis
# TODO type checking, scope checking, semantics of the program
# TODO scopes
from numpy.testing._private.parameterized import param


class Analyzer:
    def __init__(self, dst, symbol_table):
        self.__dst = dst
        self.__symbol_table = symbol_table
        self.__visited_nodes = set()
        self.__var_types = {"let", "var"}
        self.__data_types = {"Int", "Bool"}
        # scope hierarchie
        self.__scope_stack = ["0"]

        # po vyhodnoceni nejakeho vyrazu se sem placne datovy typ toho vyrazu
        # tedy jestli je to boolean, int, ...
        # slouzi pro porovnani s datovym typem, tedy do booleanu nemuzu dat int expression atd
        self.__subtree_leaf_dtype = None
        self.__subtree_leaf_value = None
        self.__identifier_table_entry = None

    # preorder tree traversal
    # build symbol table
    # check for semantics
    def Analyze(self) -> bool:
        root = self.__dst
        # traverse the tree, parent -> left subtree -> right subtree
        for node in root.traverse("preorder"):
            # subtree already visited
            if node in self.__visited_nodes:
                continue
            is_okay = self.__eval_node(node)
            if not is_okay:
                print("Semantic analysis found an error")
                return False
        return True

    # method evaluates semantic "correctness" of tree node
    # if the node is not correct, False value is returned
    def __eval_node(self, node) -> bool:
        node_name = node.name
        subtree_okay = True
        if node_name == "variable_declaration":
            subtree_okay = self.__eval_var_declaration(node)
        elif node_name == "var_declaration_expression":
            subtree_okay = self.__eval_var_declaration_expression(node)
        elif node_name == "data_type":
            subtree_okay = self.__eval_data_type(node)

        elif node_name == "expression_term":
            subtree_okay = self.__eval_expression_term(node)
        elif node_name == "expression_multiply":
            subtree_okay = self.__eval_expression_multiply(node)
        elif node_name == "factor_expression":
            subtree_okay = self.__eval_factor_expression(node)
        elif node_name == "factor":
            subtree_okay = self.__eval_factor(node)

        elif node_name == "function_call":
            subtree_okay = self.__eval_function_call(node)

        elif node_name == "var_value":
            subtree_okay = self.__eval_var_value(node)

        self.__mark_visited(node)
        return subtree_okay

    # check if variable declaration is semantically correct
    # ie if integer is really an integer and if the variable does not exist in the current scope
    def __eval_var_declaration(self, node):
        children = node.get_children()
        var_type = children[0]
        # check variable type
        if var_type.name not in self.__var_types:
            print(f"Faulty variable declaration, unknown variable type {var_type}. Allowed types: {self.__var_types}")
            return False
        # continue evaluation
        return self.__eval_node(children[1])

    def __eval_var_declaration_expression(self, node):
        children = node.get_children()
        ''' reseno pri staveni tabulky symbolu
        identifier = children[0]
        identifier_exists = self.__check_identifier(identifier,scope)
        if not identifier_exists:
            print(f"Undeclared variable {identifier}")
            return False
        '''
        data_type = children[1]
        data_type_valid = self.__eval_node(data_type)
        if not data_type_valid:
            print(f"Invalid data type {data_type.name}, allowed data types: {self.__data_types}")
            return False
        data_type = data_type.get_children()[0]
        expression = children[2]
        # type_operation_valid = self.__check_type_value_compatibility(data_type.name,expression)
        expression_valid = self.__eval_node(expression)

        if not expression_valid:
            print(f"Invalid expression value in variable declaration")
            return False
        data_type_compatible = data_type.name == self.__subtree_leaf_dtype
        if not data_type_compatible:
            print(f"Type mismatch, cannot assign expression of type {self.__subtree_leaf_dtype}"
                  f" to variable with type {data_type.name}")
        return data_type_compatible

    def __eval_expression_term(self, node):
        children = node.get_children()
        expression = children[0]
        expression_valid = self.__eval_node(expression)
        if not expression_valid:
            print(f"Invalid expression")
        return expression_valid

    # muzu nasobit jenom inty
    def __eval_expression_multiply(self, node):
        children = node.get_children()
        factor_valid = self.__eval_node(children[0])
        # uloz par hodnota, datovy typ vyhodnoceni podstromu
        subtree_value = (self.__subtree_leaf_value, self.__subtree_leaf_dtype)
        if not factor_valid:
            print(f"Invalid multiplication expression")
            return False

        factor_expression_valid = self.__eval_node(children[1])
        if not factor_expression_valid:
            print(f"Invalid value in multiplication expression")
            return False
        subsubtree_value = (self.__subtree_leaf_value, self.__subtree_leaf_dtype)
        if subtree_value[1] != subsubtree_value[1]:
            print(f"Type mismatch, cannot multiply types: {subsubtree_value[1]}, {subsubtree_value[1]}")
            return False

        return True

    def __eval_factor_expression(self, node):
        children = node.get_children()
        value_valid = self.__eval_node(children[0])
        if not value_valid:
            print("Invalid variable value")
        return value_valid

    def __eval_factor(self, node):
        children = node.get_children()

        factor_value_valid = self.__eval_node(children[0])
        if not factor_value_valid:
            print(f"Invalid value")
            return False

        return True

    def __eval_var_value(self, node):
        value = node.get_children()[0].name
        self.__subtree_leaf_value = value
        if type(value) is int:
            self.__subtree_leaf_dtype = "Int"
            return True

        valid_identifier = self.__find_identifier(value)
        if not valid_identifier:
            print(f"Invalid identifier {value}")
            return False
        return True

    def __eval_function_call(self, node):
        children = node.get_children()
        function_name = children[0].name
        is_valid_identifier = self.__find_identifier(function_name)
        if not is_valid_identifier:
            print(f"Function {function_name} is not declared")
            return False
        function_prototype = self.__identifier_table_entry
        function_arguments = children[1]

        function_params = function_prototype.params
        function_call_ok = self.__check_function_call(function_params, function_arguments)
        if not function_call_ok:
            print(f"Error when calling a function {function_name}")
        self.__subtree_leaf_value, self.__subtree_leaf_dtype = function_prototype.name, function_prototype.return_type
        return function_call_ok

    def __eval_data_type(self, node):
        data_type = node.get_children()[0]
        if data_type.name not in self.__data_types:
            return False
        return True

    # mark node as visited
    def __mark_visited(self, node):
        self.__visited_nodes.add(node)

    def __check_function_call(self, function_params, function_arguments):
        tmp = list(function_params.keys())
        walker = 0
        param_count = len(tmp)
        kiddos = function_arguments.get_children()
        # argument list
        if len(kiddos) == 2:
            while True:
                if walker >= param_count:
                    print(f"Too many arguments, expected {param_count}, got at least {walker}")
                    return False

                # single argument
                if len(kiddos) == 1:
                    kiddos = kiddos[0]
                    break
                argument_ok = self.__compare_argument_and_parameter(kiddos[0], function_params[tmp[walker]])
                if not argument_ok:
                    return False
                self.__mark_visited(kiddos[1])
                kiddos = kiddos[1].get_children()
                walker += 1
        # single argument of function
        else:
            kiddos = kiddos[0]
            # no arguments provided
            if kiddos.name == '':
                if param_count != 0:
                    print(f"No arguments provided in function call, expected {param_count} arguments")
                    return False
                return True

        argument = kiddos
        argument_ok = self.__compare_argument_and_parameter(argument, function_params[tmp[walker]])
        walker += 1
        if walker != param_count:
            print(f"Invalid number of argument in function call, expected {param_count}, instead got {walker}")
            return False

        return argument_ok

    def __compare_argument_and_parameter(self, argument, parameter):
        value_ok = self.__eval_node(argument)
        if not value_ok:
            return False
        argument_type = self.__subtree_leaf_dtype
        function_param_type = parameter.type
        if function_param_type != argument_type:
            print(f"Argument missmatch, expected argument with type {function_param_type} for parameter {parameter.name},\
             instead got argument with type {argument_type}")
            return False
        return True

    def __check_identifier(self, identifier, scope):
        # im inside some scope, not a global one, check my existence there first
        # self.__subtree_leaf_dtype = "Int"

        if scope == "0":
            if identifier in self.__symbol_table:
                self.__save_ident_values(self.__symbol_table[identifier])
                return True
            return False

        local_scope = self.__symbol_table[scope]

        if identifier in local_scope["locals"] or identifier in local_scope["params"]:
            self.__save_ident_values(local_scope[identifier])
            return True

        return False

    # jdi od myho lokalniho scopeu az po globalni, jestli tu promennou nenajdes
    def __find_identifier(self, identifier):
        i = len(self.__scope_stack)
        while i > 0:
            if self.__check_identifier(identifier, self.__scope_stack[i - 1]):
                return True
            i -= 1
        print(f"Unknown identifier {identifier}")
        return False

    # util function, saves information about identifier
    def __save_ident_values(self, symbol_table_record):
        self.__identifier_table_entry = symbol_table_record
        '''
        #function vyhybka
        if symbol_table_record.type == "func":
            self.__identifier_table_entry = symbol_table_record
            self.__subtree_leaf_dtype = symbol_table_record.return_type
        else:
            self.__subtree_leaf_dtype = symbol_table_record.type
        self.__subtree_leaf_value = symbol_table_record.name
        '''
