import ply.lex
import ply.yacc as yy
import src.syntax_analyzer as syntax
import src.lex_analyzer as lexical
import src.pl0_code_generator as gen

if __name__ == '__main__':
    lexer = ply.lex.lex(module=lexical)
    y = yy.yacc(module=syntax, debug=False)

    ast = y.parse('func a() -> int {if (a<5){return 3;} return 10;}')
    print(ast)

    generated_code = gen.Pl0(ast)
    generated_code.generate_code()
    generated_code.print_code()
