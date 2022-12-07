#  date: 13. 11. 2022
#  author: Daniel Schnurpfeil
#
# all testcases are validated with https://home.zcu.cz/~lipka/fjp/pl0/

from unittest import TestCase

from src.main import main


# It's a class that inherits from the TestCase class, and it's called Test
class Test(TestCase):

    def test_operation(self):
        """
        It tests the operation of the function.
        """
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
        """
        It tests the declaration of a variable.
        """
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
""", code, "operation")

    def test_operators(self):
        """
        It tests the operators
        """
        code = main("../sample_input/operators.swift")
        self.assertEqual("""0 INT 0 3
1 INT 0 1
2 LIT 0 40
3 STO 0 3
4 INT 0 1
5 LIT 0 10
6 LIT 0 20
7 OPR 0 4
8 LIT 0 30
9 OPR 0 2
10 LOD 0 3
11 OPR 0 3
12 STO 0 4
13 INT 0 1
14 LIT 0 60
15 STO 0 5
16 RET 0 0
""", code, "operators")

    def test_if(self):
        """
        It tests if the
        condition is true.
        """
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
5 LOD 0 3
6 STO 0 4
7 INT 0 1
8 LOD 0 4
9 STO 0 5
10 INT 0 1
11 LOD 0 4
12 LOD 0 5
13 OPR 0 2
14 STO 0 6
15 RET 0 0
""", code, "multiple_decl")

    def test_while(self):
        code = main("../sample_input/while.swift")
        self.assertEqual("""0 INT 0 3
1 INT 0 1
2 LIT 0 100
3 STO 0 3
4 LOD 0 3
5 LIT 0 1
6 OPR 0 12
7 JMC 0 13
8 LOD 0 3
9 LIT 0 1
10 OPR 0 3
11 STO 0 3
12 JMP 0 4
13 RET 0 0
""", code, "while")

    def test_repeat_while(self):
        code = main("../sample_input/repeat.swift")
        self.assertEqual("""0 INT 0 3
1 INT 0 1
2 LIT 0 100
3 STO 0 3
4 LOD 0 3
5 LIT 0 1
6 OPR 0 3
7 STO 0 3
8 LOD 0 3
9 LIT 0 50
10 OPR 0 12
11 JMC 0 13
12 JMP 0 4
13 RET 0 0
""", code, "test_repeat_while")

    def test_for(self):
        code = main("../sample_input/for.swift")
        self.assertEqual("""0 INT 0 3
1 INT 0 1
2 LIT 0 0
3 STO 0 3
4 INT 0 1
5 LIT 0 1
6 STO 0 4
7 LOD 0 4
8 LIT 0 20
9 OPR 0 10
10 JMC 0 20
11 LIT 0 1
12 LOD 0 3
13 OPR 0 2
14 STO 0 3
15 LIT 0 1
16 LOD 0 4
17 OPR 0 2
18 STO 0 4
19 JMP 0 7
20 RET 0 0
""", code, "for")

    def test_func(self):
        code = main("../sample_input/func_simple.swift")
        self.assertEqual("""0 INT 0 3
1 JMP 0 22
2 INT 0 3
3 LOD 0 -3
4 LOD 0 -2
5 LOD 0 -1
6 INT 0 1
7 LIT 0 6666
8 STO 0 6
9 LOD 0 5
10 LIT 0 1000
11 OPR 0 2
12 STO 0 4
13 LIT 0 141
14 LOD 0 5
15 OPR 0 2
16 STO 0 5
17 LOD 0 3
18 LIT 0 1
19 OPR 0 2
20 STO 0 -4
21 RET 0 0
22 INT 0 1
23 LIT 0 99999
24 STO 0 4
25 INT 0 1
26 INT 0 1
27 LOD 0 4
28 LIT 0 30
29 LIT 0 40
30 CAL 0 2
31 INT 0 -3
32 STO 0 5
33 RET 0 0
""", code, "func")

    def test_func_very_simple(self):
        code = main("../sample_input/func_very_simple.swift")
        self.assertEqual("""0 INT 0 3
1 INT 0 1
2 LIT 0 555
3 STO 0 3
4 JMP 0 14
5 INT 0 3
6 LOD 0 -1
7 LIT 0 111
8 LOD 0 3
9 OPR 0 2
10 STO 0 3
11 LOD 0 3
12 STO 0 -2
13 RET 0 0
14 INT 0 1
15 INT 0 1
16 LOD 0 3
17 CAL 0 5
18 INT 0 -1
19 STO 0 5
20 RET 0 0
""", code, "func_very_simple")
