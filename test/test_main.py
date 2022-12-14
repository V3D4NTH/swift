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
2 LIT 0 555
3 STO 0 3
4 RET 0 0
""", code, "operation")

    def test_declaration(self):
        """
        It tests the declaration of a variable.
        """
        code = main("../sample_input/declaration.swift")
        self.assertEqual("""0 INT 0 3
1 INT 0 1
2 LIT 0 555
3 STO 0 3
4 INT 0 1
5 LOD 0 3
6 LIT 0 10
7 OPR 0 2
8 STO 0 4
9 RET 0 0
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
5 LIT 0 230
6 LOD 0 3
7 OPR 0 3
8 STO 0 4
9 INT 0 1
10 LIT 0 60
11 STO 0 5
12 RET 0 0
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

    def test_ternary_operator(self):
        code = main("../sample_input/ternary_operator.swift")
        self.assertEqual("""0 INT 0 3
1 INT 0 1
2 LIT 0 100
3 STO 0 3
4 LOD 0 3
5 LIT 0 43
6 OPR 0 10
7 JMC 0 12
8 LOD 0 3
9 LIT 0 9
10 OPR 0 2
11 JMP 0 15
12 LOD 0 3
13 LIT 0 5
14 OPR 0 2
15 STO 0 3
16 RET 0 0
""", code, "ternary_operator")

    def test_for_in_func(self):
            code = main("../sample_input/for_in_func.swift")
            self.assertEqual("""0 INT 0 3
1 INT 0 1
2 LIT 0 52
3 STO 0 3
4 JMP 0 26
5 INT 0 3
6 LOD 0 -1
7 INT 0 1
8 LIT 0 0
9 STO 0 3
10 LOD 0 3
11 LIT 0 1344
12 OPR 0 10
13 JMC 0 23
14 LIT 0 1
15 LOD 0 2
16 OPR 0 2
17 STO 0 2
18 LIT 0 1
19 LOD 0 3
20 OPR 0 2
21 STO 0 3
22 JMP 0 10
23 LOD 0 2
24 STO 0 -2
25 RET 0 0
26 INT 0 1
27 LOD 0 3
28 CAL 0 5
29 INT 0 -1
30 STO 0 3
31 RET 0 0
""", code, "for_in_func")

    def test_program(self):
        code = main("../sample_input/program.swift")
        self.assertEqual("""0 INT 0 3
1 JMP 0 25
2 INT 0 3
3 LOD 0 -1
4 INT 0 1
5 LIT 0 20
6 STO 0 7
7 LIT 0 52
8 LIT 0 43
9 OPR 0 12
10 JMC 0 22
11 INT 0 1
12 LOD 0 6
13 STO 0 8
14 LIT 0 20
15 STO 0 8
16 LIT 0 32
17 LOD 0 7
18 OPR 0 4
19 STO 0 7
20 LOD 0 7
21 JMP 0 23
22 LOD 0 7
23 STO 0 -2
24 RET 0 0
25 JMP 0 47
26 INT 0 3
27 LOD 0 -1
28 INT 0 1
29 LIT 0 1
30 STO 0 7
31 LOD 0 7
32 LIT 0 21
33 OPR 0 10
34 JMC 0 44
35 LOD 0 7
36 LIT 0 5
37 OPR 0 2
38 STO 0 6
39 LIT 0 1
40 LOD 0 7
41 OPR 0 2
42 STO 0 7
43 JMP 0 31
44 LOD 0 6
45 STO 0 -2
46 RET 0 0
47 JMP 0 74
48 INT 0 3
49 LOD 0 -2
50 LOD 0 -1
51 INT 0 1
52 LIT 0 1
53 STO 0 8
54 LOD 0 8
55 LIT 0 20
56 OPR 0 10
57 JMC 0 71
58 LIT 0 1
59 LOD 0 6
60 OPR 0 2
61 STO 0 6
62 LIT 0 2
63 LOD 0 7
64 OPR 0 2
65 STO 0 7
66 LIT 0 1
67 LOD 0 8
68 OPR 0 2
69 STO 0 8
70 JMP 0 54
71 LOD 0 6
72 STO 0 -3
73 RET 0 0
74 JMP 0 124
75 INT 0 3
76 LOD 0 -4
77 LOD 0 -3
78 LOD 0 -2
79 LOD 0 -1
80 INT 0 1
81 LIT 0 42
82 STO 0 10
83 INT 0 1
84 LIT 0 1
85 STO 0 11
86 LOD 0 11
87 LIT 0 3
88 OPR 0 10
89 JMC 0 121
90 INT 0 1
91 LIT 0 1
92 STO 0 12
93 LOD 0 12
94 LIT 0 3
95 OPR 0 10
96 JMC 0 116
97 LOD 0 6
98 LOD 0 7
99 OPR 0 4
100 LOD 0 8
101 OPR 0 3
102 LOD 0 9
103 OPR 0 3
104 LOD 0 11
105 OPR 0 2
106 LOD 0 12
107 OPR 0 2
108 LOD 0 10
109 OPR 0 2
110 STO 0 10
111 LIT 0 1
112 LOD 0 12
113 OPR 0 2
114 STO 0 12
115 JMP 0 93
116 LIT 0 1
117 LOD 0 11
118 OPR 0 2
119 STO 0 11
120 JMP 0 86
121 LOD 0 10
122 STO 0 -5
123 RET 0 0
124 INT 0 1
125 LIT 0 0
126 STO 0 7
127 INT 0 1
128 LIT 0 0
129 STO 0 8
130 INT 0 1
131 LIT 0 43
132 CAL 0 2
133 INT 0 -1
134 STO 0 8
135 INT 0 1
136 LOD 0 7
137 LOD 0 8
138 CAL 0 48
139 INT 0 -2
140 STO 0 7
141 RET 0 0
""", code, "program")
