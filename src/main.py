import ply.lex
import ply.yacc as yy
import src.syntax_analyzer as syntax
import src.lex_analyzer as lexical
import src.pl0_code_generator as gen


if __name__ == '__main__':

    lexer = ply.lex.lex(module=lexical)
    y = yy.yacc(module=syntax, debug=False)
    ast = y.parse(''
                  'for (let j : int = 52; j < 32; j += 1;){'
                  'var a:int = 5;'
                  'var y: int = a+c;'
                  'return 42;'
                  '}'
                  'return 10;'
                  '')
    '''
    ast = y.parse('func main(a:int,c:int,x:int)->int{'
                  'var a:int = 5;'
                  'var y: int = a+c;'
                  'return 31;'
                  '}'
                  'main(1,2,3);')
    '''

    print(ast.get_ascii(attributes=["name", "dist", "label", "complex"]))
    print(ast)
    '''
    generated_code = gen.Pl0(ast)
    generated_code.generate_code()
    generated_code.print_code()
    '''