# class responsible from semantical analysis
# TODO type checking, scope checking, semantics of the program
import src.syntax_analyzer.utils as utils


class Analyzer:
    def __init__(self, dst, symbol_table):
        self.__dst = dst
        self.__symbol_table = symbol_table
        self.__visited_nodes = set()
        self.__var_types = {"let", "var"}
        self.__data_types = {"Int", "Boolean","Array","String"}
        # aktualni zanoreni
        self.real_level = 0
        # global scope (0) nebo jmeno funkce
        self.level = 0
        # pocet returnu ve funkci, maximalne povolen 1
        self.ret_statement_count = 0
        # co se z funkce vraci
        self.ret_value = None
        # po vyhodnoceni nejakeho vyrazu se sem placne datovy typ toho vyrazu
        # tedy jestli je to boolean, int, ...
        # slouzi pro porovnani s datovym typem, tedy do booleanu nemuzu dat int expression atd
        self.__subtree_leaf_dtype = None
        self.__subtree_leaf_value = None
        self.__identifier_table_entry = None
        # nazev posledniho nodeu v tele bloku -> u bloku funkce toto nezbytne musi byt return statement.
        self.__last_stmt_in_block = None

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
        elif node_name == "expression_sum":
            subtree_okay = self.__eval_expression_sum(node)
        elif node_name == "expression_minus":
            subtree_okay = self.__eval_expression_minus(node)
        elif node_name == "expression_divide":
            subtree_okay = self.__eval_expression_divide(node)
        elif node_name == "expression_in_parent":
            subtree_okay = self.__eval_expression_in_parenthesis(node)
        elif node_name == "factor_expression":
            subtree_okay = self.__eval_factor_expression(node)
        elif node_name == "factor":
            subtree_okay = self.__eval_factor(node)
        elif node_name == "function_call":
            subtree_okay = self.__eval_function_call(node)
        elif node_name == "var_value":
            subtree_okay = self.__eval_var_value(node)
        elif node_name == "function_declaration":
            subtree_okay = self.__eval_function_declaration(node)
        elif node_name == "params":
            subtree_okay = self.__eval_function_parameters(node)
        elif node_name == "function_signature":
            subtree_okay = self.__eval_function_signature(node)
        elif node_name == "compound_block":
            subtree_okay = self.__eval_comp_block(node)
        # [JT] names of all nodes whose children represent a block, either a function body, if/if-else body or loop body
        elif node_name == "block" or node_name == "block_var_dekl" or node_name == "block_expression" or node_name == "block_statement":
            subtree_okay = self.__eval_block(node)
        elif node_name == "for_loop_block":
            subtree_okay = self.__eval_for_loop_block(node)
        elif node_name == "loop_step":
            subtree_okay = self.__eval_loop_step(node)
        elif node_name == "loop_var":
            subtree_okay = self.__eval_loop_var(node)
        elif node_name == "condition":
            subtree_okay = self.__eval_condition(node)
        elif node_name == "compound_condition":
            subtree_okay = self.__eval_compound_condition(node)
        elif node_name == "simple_condition":
            subtree_okay = self.__eval_simple_condition(node)
        elif node_name == "id_compound_condition":
            subtree_okay = self.__eval_id_compound_condition(node)
        elif node_name == "var_modification":
            subtree_okay = self.__eval_var_modification(node)
        elif node_name == "if_stmt":
            subtree_okay = self.__eval_if_stmt(node)
        elif node_name == "if_else_stmt":
            subtree_okay = self.__eval_if_else_stmt(node)
        elif node_name == "return_statement":
            subtree_okay = self.__eval_return_statement(node)
        elif node_name == "while_loop_block":
            subtree_okay = self.__eval_while_statement(node)
        elif node_name == "repeat_loop_block":
            subtree_okay = self.__eval_repeat_statement(node)
        elif node_name == "unary_minus":
            subtree_okay = self.__eval_unary_minus(node)
        elif node_name == "negation_condition":
            subtree_okay = self.__eval_negation_condition(node)
        elif node_name == "const_expression_term":
            subtree_okay = True

        self.__mark_visited(node)
        return subtree_okay


    def __eval_negation_condition(self,node):
        children = node.get_children()
        condition = children[0]
        condition_ok = self.__eval_node(condition)
        if not condition_ok:
            print("Condition contains an error. Negation is not possible.")
            return False
        if self.__subtree_leaf_dtype != "Int" and self.__subtree_leaf_dtype != "Boolean":
            print(f"Error. Negation is only defined for integers or booleans. Got {self.__subtree_leaf_dtype}")
            return False
        return True


    def __eval_expression_in_parenthesis(self,node):
        children = node.get_children()
        expression = children[0]
        is_expression_okay = self.__eval_node(expression)
        if not is_expression_okay:
            print("Error. Expression in parenthesis contains an error.")
            return False
        return True

    def __eval_unary_minus(self,node):
        children = node.get_children()
        expression = children[1]
        is_expression_okay = self.__eval_node(expression)
        if not is_expression_okay:
            print("Error in unary minus operation. Expression is not valid.")
            return False
        if self.__subtree_leaf_dtype != "Int":
            print("Error in unary minus operation. Unary minus can only be performed on integers.")
            return False
        return True

    def __eval_compound_condition(self,node):
        children = node.get_children()
        left_side = children[0]
        right_side = children[2]
        chained_condition = children[4]

        left_side_okay = self.__eval_node(left_side)
        if not left_side_okay:
            print("Error, left side of condition is not correct.")
            return False
        left_side_info = (self.__subtree_leaf_value, self.__subtree_leaf_dtype)
        is_function_call = self.__check_if_is_function()
        if is_function_call:
            print("Error, function call cannot be used in condition!")
            return False
        right_side_okay = self.__eval_node(right_side)
        if not right_side_okay:
            print("Error, right side of condition is not correct.")
            return False
        is_function_call = self.__check_if_is_function()
        if is_function_call:
            print("Error, function call cannot be used in condition!")
            return False
        right_side_info = (self.__subtree_leaf_value, self.__subtree_leaf_dtype)

        if left_side_info[1] != right_side_info[1]:
            print("Type mismatch in addition. Addition can only be performed with integers.")
            return False
        is_chained_condition_okay = self.__eval_node(chained_condition)
        if not is_chained_condition_okay:
            print("Error, chained condition contains and error.")
            return False

        return True

    def __eval_while_statement(self,node):
        children = node.get_children()
        condition = children[0]
        body = children[1]
        is_condition_okay = self.__eval_node(condition)
        if not is_condition_okay:
            print("Error, condition in while loop is not correct!")
            return False
        is_body_okay = self.__eval_node(body)
        if not is_body_okay:
            print("Error, body of while loop contains an error.")
            return False
        return True

    def __eval_repeat_statement(self,node):
        children = node.get_children()
        body = children[0]
        condition = children[1]
        is_condition_okay = self.__eval_node(condition)
        if not is_condition_okay:
            print("Error in condition of repeat statement.")
            return False
        is_body_okay = self.__eval_node(body)
        if not is_body_okay:
            print("Body of repeat statement contains an error.")
            return False
        return True


    def __eval_return_statement(self, node):
        children = node.get_children()
        expression = children[0]
        is_expression_okay = self.__eval_node(expression)
        if not is_expression_okay:
            print("Error in return value")
            return False
        self.ret_statement_count += 1
        self.ret_value = expression
        return True

    def __eval_expression_sum(self, node):
        children = node.get_children()
        term = children[0]
        factor = children[1]
        is_term_expression_okay = self.__eval_node(term)
        left_side_info = (self.__subtree_leaf_value, self.__subtree_leaf_dtype)

        if not is_term_expression_okay:
            print("Error in addition.")
        is_factor_okay = self.__eval_node(factor)
        right_side_info = (self.__subtree_leaf_value, self.__subtree_leaf_dtype)
        if not is_factor_okay:
            print("Error in factor expression.")

        if left_side_info[1] != right_side_info[1]:
            print("Type mismatch in addition. Addition can only be performed with integers.")
            if right_side_info[1] == "func" or right_side_info[1] == "func":
                print("If you intended to use function call in expression."
                      " Store the return value of function in a variable.")
            return False

        return True

    def __eval_expression_divide(self, node):
        children = node.get_children()
        factor = children[0]
        expression = children[1]
        is_dividend_okay = self.__eval_node(factor)
        dividend_info = (self.__subtree_leaf_value, self.__subtree_leaf_dtype)
        if not is_dividend_okay:
            print("Error in division. Dividend is not a valid expression.")
            return False
        is_divisor_okay = self.__eval_node(expression)
        divisor_info = (self.__subtree_leaf_value, self.__subtree_leaf_dtype)
        if dividend_info[1] != divisor_info[1]:
            print("Type mismatch in division. Division can only be performed with integers.")
            if divisor_info[1] == "func" or dividend_info[1] == "func":
                print("If you intended to use function call in expression."
                      " Store the return value of function in a variable.")
            return False
        if not is_divisor_okay:
            print("Error in division. Divisor is not a valid expression.")
            return False
        if type(self.__subtree_leaf_value) is int and self.__subtree_leaf_value == 0:
            print("Error. Division by zero is not defined.")
            return False

        return True

    def __eval_expression_minus(self, node):
        children = node.get_children()
        term = children[0]
        factor = children[1]
        is_term_expression_okay = self.__eval_node(term)
        left_side_info = (self.__subtree_leaf_value, self.__subtree_leaf_dtype)
        if not is_term_expression_okay:
            print("Error in minus expression.")
        is_factor_okay = self.__eval_node(factor)
        if not is_factor_okay:
            print("Error in factor expression.")

        right_side_info = (self.__subtree_leaf_value, self.__subtree_leaf_dtype)
        if left_side_info[1] != right_side_info[1]:
            print("Type mismatch in subtraction. Subtraction can only be performed with integers.")
            if right_side_info[1] == "func" or right_side_info[1] == "func":
                print("If you intended to use function call in expression."
                      " Store the return value of function in a variable.")
            return False

        return True

    def __eval_if_else_stmt(self, node):
        children = node.get_children()
        condition = children[0]
        if_body = children[1]
        else_body = children[2]
        is_condition_okay = self.__eval_node(condition)
        if not is_condition_okay:
            print("Error in if statement condition")
            return False

        is_if_body_okay = self.__eval_node(if_body)
        if not is_if_body_okay:
            print("Error in body of if statement")
            return False
        is_else_body_okay = self.__eval_node(else_body)
        if not is_else_body_okay:
            print("Error in body of else statement")
            return False
        return True

    def __eval_if_stmt(self, node):
        children = node.get_children()
        condition = children[0]
        body = children[1]
        is_condition_okay = self.__eval_node(condition)
        if not is_condition_okay:
            print("Error in if statement condition")
            return False
        is_if_body_okay = self.__eval_node(body)
        if not is_if_body_okay:
            print("Error in body of if statement")
            return False
        return True

    def __eval_var_modification(self, node):
        children = node.get_children()
        identifier = children[0].name
        modification_operator = children[1].name
        expression = children[2]
        is_valid_identifier = self.__find_identifier(identifier)
        if not is_valid_identifier:
            print(f"Error in variable modification, identifier {identifier} is not defined.")
            return False
        if self.__identifier_table_entry.const:
            print(f"Error in variable modification, identifier {identifier} is a constant. "
                  f"Its value cannot be adjusted at runtime")
            return False
        is_valid_expression = self.__eval_node(expression)
        if not is_valid_expression:
            print(f"Error in variable modification when updating value of variable {identifier}. "
                  f"The assigned expression is not valid.")
            return False
        if modification_operator != "=" and self.__check_if_is_function():
            print(f"Error in variable modification when udpating value of variable {identifier}."
                  f" Function call can be only used with assignment operator, '='.")
            return False
        return True

    def __eval_function_declaration(self, node):
        children = node.get_children()
        is_function_okay = self.__eval_node(children[0])
        if not is_function_okay:
            print(f"Function declaration contains an error")
            return False
        return True

    def __eval_for_loop_block(self, node):
        children = node.get_children()
        loop_var = children[0]
        condition = children[1]
        step = children[2]
        body = children[3]

        is_loop_var_okay = self.__eval_node(loop_var)
        if not is_loop_var_okay:
            print("Error in declaration of controlling variable in for loop statement")
            return False
        is_loop_condition_okay = self.__eval_node(condition)
        if not is_loop_condition_okay:
            print("Error, for loop condition is not correct")
            return False
        is_step_okay = self.__eval_node(step)
        if not is_step_okay:
            print("Error, step statement of for loop is not correct")
            return False
        is_body_okay = self.__eval_node(body)
        if not is_body_okay:
            print("Error in body of for loop")
            return False

        return True

    def __eval_condition(self, node):
        children = node.get_children()
        left_side = children[0]
        right_side = children[2]
        is_left_side_okay = self.__eval_node(left_side)
        if not is_left_side_okay:
            print("Error in the expression on left side of condition")
            return False
        is_function_call = self.__check_if_is_function()
        if is_function_call:
            print("Error, condition cannot contain function call")
            return False

        is_right_side_okay = self.__eval_node(right_side)

        is_function_call = self.__check_if_is_function()
        if is_function_call:
            print("Error, condition cannot contain function call")
            return False

        if not is_right_side_okay:
            print("Error in the expression on right side of condition")
            return False

        return True

    def __eval_loop_step(self, node):
        children = node.get_children()
        identifier = children[0].name
        is_valid_identifier = self.__find_identifier(identifier)
        if not is_valid_identifier:
            print(f"Error in for loop step, {identifier} was not found")
            return False
        if self.__identifier_table_entry.const:
            print(f"Error in for loop step, {identifier} is a constant. Value cannot be changed.")
            return False
        return True

    def __eval_loop_var(self, node):
        children = node.get_children()
        expr = children[0]
        if len(children) == 2:
            expr = children[1]
        is_variable_okay = self.__eval_node(expr)
        if not is_variable_okay:
            print("Error in declaration of for loop variable")
            return False
        return True

    def __eval_function_signature(self, node):
        children = node.get_children()
        function_name = children[0].name
        params = children[1]
        return_type = children[2]
        body = children[3]
        # save previous scope
        previous_level = self.level
        previous_return_count = self.ret_statement_count
        previous_return_val = self.ret_value
        # update scope
        self.level = function_name
        params_ok = self.__eval_node(params)

        if not params_ok:
            print(f"Parameters of function {function_name} are not okay.")
            return False
        return_type_val = return_type.name
        if return_type_val != "Void":
            return_type_okay = self.__eval_node(return_type)
            if not return_type_okay:
                print(f"Return type of function {function_name} is not valid.")
                return False
            return_type_val = return_type.get_children()[0].name
        else:
            self.__mark_visited(return_type)
        body_ok = self.__eval_node(body)
        if not body_ok:
            print(f"Error in body of function {function_name}.")
            return False
        last_stmt_in_body = self.__last_stmt_in_block
        if return_type_val != "Void":
            if self.ret_statement_count == 0:
                print("Return statement in function was expected, none found. Add one return statement")
            elif self.ret_statement_count > 1:
                print("Function can have only one return statement.")
                return False
            elif last_stmt_in_body != "return_statement":
                print(f"Last statement in function block which is of type {return_type_val} must be a return statement")
                return False

        # restore previous scope
        self.level = previous_level
        self.ret_statement_count = previous_return_count
        self.ret_value = previous_return_val
        return True

    # zde neni nic moc k overeni
    def __eval_function_parameters(self, node):
        # children = node.get_children()
        return True

    def __eval_block(self, node):
        tmp_node = node
        # projedu cely podstrom bloku
        while True:
            # vyhodnot podstrom
            children = tmp_node.get_children()
            n = len(children)
            tmp = children[0]
            # block variable declaration, the relevant subtree is on index 1 instead of 0
            if n == 3:
                tmp = children[1]
            is_statement_okay = self.__eval_node(tmp)
            if not is_statement_okay:
                print("Error in block")
                return False

            # konec vetveni stromu
            if len(children) == 1:
                if tmp.name != "block":
                    self.__last_stmt_in_block = tmp.name
                break
            # jdi dal stromem bloku
            tmp_node = children[1]
            if n == 3:
                tmp_node = children[2]

        return True

    def __eval_comp_block(self, node):
        self.real_level += 1
        block_node = node.get_children()[0]
        is_block_okay = self.__eval_node(block_node)
        if not is_block_okay:
            print("Error in compound block")
            return False
        self.real_level -= 1
        return True

    # check if variable declaration is semantically correct
    # ie if integer is really an integer and if the variable does not exist in the current scope
    def __eval_var_declaration(self, node):
        children = node.get_children()
        var_type = children[0]
        self.__mark_visited(var_type)
        # check variable type
        if var_type.name not in self.__var_types:
            print(
                f"Faulty variable declaration, unknown variable type {var_type.name}. Allowed types: {self.__var_types}")
            return False
        # continue evaluation
        return self.__eval_node(children[1])

    def __eval_var_declaration_expression(self, node):
        children = node.get_children()

        data_type = children[1]
        data_type_valid = self.__eval_node(data_type)
        if not data_type_valid:
            print(f"Invalid data type when declaring a variable")
            return False
        data_type = data_type.get_children()[0]
        expression = children[2]
        # type_operation_valid = self.__check_type_value_compatibility(data_type.name,expression)
        expression_valid = self.__eval_node(expression)
        if data_type.name == "Boolean" and (self.__subtree_leaf_value == 1 or self.__subtree_leaf_value == 0):
            self.__subtree_leaf_dtype = "Boolean"

        if not expression_valid:
            print(f"Invalid expression value in variable declaration")
            return False
        #neresim to dal - vim, ze je to spravne, protoze to je vyhodnoceno v ramci gramatiky
        if expression.name == "const_expression_term":
            return True
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
        return True

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
            print(f"Type mismatch, cannot multiply types: {subtree_value[1]}, {subsubtree_value[1]}."
                  f" Multiplication is only allowed with Int data type. ")
            if subsubtree_value[1] == "func":
                print("You intended to use function call in expression. "
                      "Store the result of function call a variable first and use that variable in expression.")
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
        self.__mark_visited(node.get_children()[0])
        self.__subtree_leaf_value = value
        if type(value) is int:
            self.__subtree_leaf_dtype = "Int"
            return True

        valid_identifier = self.__find_identifier(value)
        if not valid_identifier:
            print(f"Invalid identifier {value}")
            return False
        self.__subtree_leaf_value = self.__identifier_table_entry

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
        self.__mark_visited(node.get_children()[0])
        if data_type.name not in self.__data_types:
            print(f"Invalid data type {data_type.name}. Valid data types: Int, Boolean")
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
            print(f"Invalid argument value {argument.get_children()[0].name} for parameter {parameter.name}")
            return False
        argument_type = self.__subtree_leaf_dtype
        function_param_type = parameter.type
        if function_param_type != argument_type:
            print(f"Argument missmatch, expected argument with type {function_param_type} for parameter {parameter.name},\
             instead got argument with type {argument_type}")
            return False
        return True

    # jdi od myho lokalniho scopeu az po globalni, jestli tu promennou nenajdes
    # TODO rozhodnout, kdy vidim a kdy nevidim na identifikator
    def __find_identifier(self, identifier):
        symbol = utils.find_entry_in_symbol_table(self.__symbol_table, self.level, self.real_level, identifier)
        if symbol is None:
            print(f"Identifier {identifier} not declared!")
            return False
        self.__identifier_table_entry = symbol
        self.__subtree_leaf_dtype = symbol.type
        return True

    # util function, saves information about identifier
    def __save_ident_values(self, symbol_table_record):
        self.__identifier_table_entry = symbol_table_record

    def __check_if_is_function(self):
        val = self.__identifier_table_entry
        if not val:
            return False
        if val.type == "func":
            return True
        return False
