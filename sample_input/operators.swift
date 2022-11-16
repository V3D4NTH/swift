var a: Int = 333;
a *= 10;
// a *= 10; // todo tuto nefunguje kvuli: var_modification! -> statement, 1.0var_modification
//
//                                                         /-var, 1.0
//                                                          |
//                                  /variable_declaration, 1.0                              /-a, 1.0
//                                 |                        |                              |
//                                 |                         \var_declaration_expression, 1.0data_type, 1.0-Int, 1.0
//                                 |                                                       |
//                                 |                                                        \expression_term, 1.0factor, 1.0factor_expression, 1.0var_value, 1.0-333, 1.0
// -program, 1.0declaration_list, 1.0
//                                 |                                          /-a, 1.0
//                                 |                                         |
//                                 |                     /var_modification, 1.0-*=, 1.0
//                                 |                    |                    |
//                                 |                    |                     \expression_term, 1.0factor, 1.0factor_expression, 1.0var_value, 1.0-10, 1.0
//                                  \var_modification, 1.0
//                                                      |                                   /-a, 1.0
//                                                      |                                  |
//                                                       \statement, 1.0var_modification, 1.0-*=, 1.0
//                                                                                         |
//                                                                                          \expression_term, 1.0factor, 1.0factor_expression, 1.0var_value, 1.0-10, 1.0
//