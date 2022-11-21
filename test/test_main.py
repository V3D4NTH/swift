#  date: 13. 11. 2022
#  author: Daniel Schnurpfeil
#

from unittest import TestCase

from src.main import main


class Test(TestCase):

    def test_operation(self):
        code = main("../sample_input/operation.swift")
        self.assertEqual(
            """0 INT 0 3
1 INT 0 1
2 LIT 0 222
3 LIT 0 333
4 OPR 0 2
5 STO 0 3
6 RET 0 0
""", code, "operation")

    def test_declaration(self):
        code = main("../sample_input/declaration.swift")
        self.assertEqual("""0 INT 0 3
1 INT 0 1
2 LIT 0 222
3 LIT 0 333
4 OPR 0 2
5 STO 0 3
6 INT 0 1
7 LOD 0 3
8 LIT 0 10
9 OPR 0 2
10 STO 0 4
11 RET 0 0
"""
                         , code, "operation")

    def test_operators(self):
        code = main("../sample_input/operators.swift")
        self.assertEqual("""0 INT 0 3
1 INT 0 1
2 LIT 0 40
3 STO 0 3
4 INT 0 1
5 LIT 0 10
6 LIT 0 20
7 OPR 0 2
8 LIT 0 10
9 STO 0 4
10 RET 0 0
""", code, "operators")

    def test_if(self):
        code = main("../sample_input/if.swift")
        self.assertEqual("""0 INT 0 3
1 INT 0 1
2 LIT 0 0
3 STO 0 3
4 LIT 0 52
5 LIT 0 43
6 OPR 0 12
7 JMC 0 12
8 LIT 0 32
9 LOD 0 3
10 OPR 0 4
11 STO 0 3
12 RET 0 0
""", code, "if")

    def test_if_else(self):
        code = main("../sample_input/if_else.swift")
        self.assertEqual("""0 INT 0 3
1 INT 0 1
2 LIT 0 0
3 STO 0 3
4 LIT 0 52
5 LIT 0 43
6 OPR 0 10
7 JMC 0 13
8 LIT 0 32
9 LOD 0 3
10 OPR 0 4
11 STO 0 3
12 JMP 0 17
13 LIT 0 4
14 LOD 0 3
15 OPR 0 3
16 STO 0 3
17 RET 0 0
""", code, "if_else")

    def test_if_if_else(self):
        code = main("../sample_input/if_if_else.swift")
        self.assertEqual("""0 INT 0 3
1 INT 0 1
2 LIT 0 1
3 STO 0 3
4 LIT 0 52
5 LIT 0 43
6 OPR 0 10
7 JMC 0 17
8 LIT 0 100
9 LIT 0 43
10 OPR 0 10
11 JMC 0 16
12 LIT 0 32
13 LOD 0 3
14 OPR 0 4
15 STO 0 3
16 JMP 0 21
17 LIT 0 4
18 LOD 0 3
19 OPR 0 3
20 STO 0 3
21 RET 0 0
""", code, "if_if_else")

    def test_multiple_decl(self):
        code = main("../sample_input/multiple_decl.swift")
        self.assertEqual("""0 INT 0 3
1 INT 0 1
2 LIT 0 40
3 STO 0 3
4 INT 0 1
5 STO 0 4
6 INT 0 1
7 STO 0 5
8 INT 0 1
9 OPR 0 2
10 STO 0 6
11 RET 0 0
""", code, "multiple_decl")

    # def test_while(self):
    #     code = main("../sample_input/while.swift")
    #     self.assertEqual(" ", code, "while")

    #
    # def test_for_in_func(self):
    #     code = main("../sample_input/for_in_func.swift")
    #     self.assertEqual(" ", code, "for_in_func")
    #
    # def test_func(self):
    #     code = main("../sample_input/func.swift")
    #     self.assertEqual(" ", code, "func")
    #
    # def test_func_simple(self):
    #     code = main("../sample_input/func_simple.swift")
    #     self.assertEqual("", code, "func_simple")
