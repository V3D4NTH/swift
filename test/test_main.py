#  date: 13. 11. 2022
#  author: Daniel Schnurpfeil
#
# all testcases are validated with https://home.zcu.cz/~lipka/fjp/pl0/

from unittest import TestCase

from src.start_compiler import start_compiler


# It's a class that inherits from the TestCase class, and it's called Test
class Test(TestCase):

    def test_operation(self):
        """
        It tests the operation of the function.
        """
        code = start_compiler("../sample_input/operation.swift")
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
        code = start_compiler("../sample_input/declaration.swift")
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
        code = start_compiler("../sample_input/operators.swift")
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
        code = start_compiler("../sample_input/if.swift")
        self.assertEqual("""0 INT 0 3
1 INT 0 1
2 LIT 0 0
3 STO 0 3
4 LIT 0 52
5 LIT 0 43
6 OPR 0 12
7 JMC 0 13
8 LIT 0 32
9 LOD 0 3
10 OPR 0 4
11 STO 0 3
12 RET 0 0
""", code, "if")

    def test_if_and(self):
            code = start_compiler("../sample_input/if_and.swift")
            self.assertEqual("""0 INT 0 3
1 INT 0 1
2 LIT 0 1
3 STO 0 3
4 LOD 0 3
5 LIT 0 5
6 OPR 0 10
7 JMC 0 21
8 LIT 0 52
9 LIT 0 43
10 OPR 0 12
11 JMC 0 21
12 LOD 0 3
13 LIT 0 5
14 OPR 0 12
15 JMC 0 21
16 LIT 0 32
17 LOD 0 3
18 OPR 0 4
19 STO 0 3
20 LIT 0 32
21 RET 0 0
""", code, "if_and")

    def test_if_and_or(self):
            code = start_compiler("../sample_input/if_and_or.swift")
            self.assertEqual("""0 INT 0 3
1 INT 0 1
2 LIT 0 1
3 STO 0 3
4 LOD 0 3
5 LIT 0 5
6 OPR 0 12
7 LIT 0 -1
8 OPR 0 2
9 JMC 0 18
10 LIT 0 52
11 LIT 0 43
12 OPR 0 12
13 JMC 0 23
14 LOD 0 3
15 LIT 0 5
16 OPR 0 10
17 JMC 0 23
18 LIT 0 32
19 LOD 0 3
20 OPR 0 4
21 STO 0 3
22 LIT 0 32
23 RET 0 0
""", code, "if_and_or")

    def test_if_or(self):
            code = start_compiler("../sample_input/if_or.swift")
            self.assertEqual("""0 INT 0 3
1 INT 0 1
2 LIT 0 1
3 STO 0 3
4 LOD 0 3
5 LIT 0 5
6 OPR 0 12
7 LIT 0 -1
8 OPR 0 2
9 JMC 0 20
10 LIT 0 52
11 LIT 0 43
12 OPR 0 12
13 LIT 0 -1
14 OPR 0 2
15 JMC 0 20
16 LIT 0 1
17 LIT 0 1
18 OPR 0 12
19 JMC 0 25
20 LIT 0 32
21 LOD 0 3
22 OPR 0 4
23 STO 0 3
24 LIT 0 32
25 RET 0 0
""", code, "if_or")

    def test_if_else(self):
        code = start_compiler("../sample_input/if_else.swift")
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
        code = start_compiler("../sample_input/if_if_else.swift")
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
11 JMC 0 17
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
        code = start_compiler("../sample_input/multiple_decl.swift")
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
        code = start_compiler("../sample_input/while.swift")
        self.assertEqual("""0 INT 0 3
1 INT 0 1
2 LIT 0 5
3 STO 0 3
4 LOD 0 3
5 LIT 0 1
6 OPR 0 12
7 JMC 0 17
8 LOD 0 3
9 LIT 0 50
10 OPR 0 10
11 JMC 0 17
12 LOD 0 3
13 LIT 0 1
14 OPR 0 3
15 STO 0 3
16 JMP 0 4
17 RET 0 0
""", code, "while")

    def test_repeat_while(self):
        code = start_compiler("../sample_input/repeat.swift")
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
        code = start_compiler("../sample_input/for.swift")
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
        code = start_compiler("../sample_input/func_simple.swift")
        self.assertEqual("""0 INT 0 3
1 JMP 0 28
2 INT 0 3
3 LOD 0 -3
4 LOD 0 -2
5 LOD 0 -1
6 INT 0 1
7 LIT 0 6666
8 LOD 0 3
9 OPR 0 2
10 STO 0 6
11 LOD 0 5
12 LIT 0 1000
13 OPR 0 2
14 STO 0 4
15 LIT 0 141
16 LOD 0 5
17 OPR 0 2
18 STO 0 5
19 LOD 0 6
20 LOD 0 4
21 OPR 0 2
22 LOD 0 5
23 OPR 0 2
24 STO 0 6
25 LOD 0 6
26 STO 0 -4
27 RET 0 0
28 INT 0 1
29 LIT 0 99999
30 STO 0 4
31 INT 0 1
32 INT 0 1
33 LOD 0 4
34 LIT 0 30
35 LIT 0 40
36 CAL 0 2
37 INT 0 -3
38 STO 0 5
39 RET 0 0
""", code, "func")

    def test_func_very_simple(self):
        code = start_compiler("../sample_input/func_very_simple.swift")
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
        code = start_compiler("../sample_input/ternary_operator.swift")
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
            code = start_compiler("../sample_input/for_in_func.swift")
            self.assertEqual("""0 INT 0 3
1 INT 0 1
2 LIT 0 52
3 STO 0 3
4 JMP 0 26
5 INT 0 3
6 LOD 0 -1
7 INT 0 1
8 LIT 0 0
9 STO 0 4
10 LOD 0 4
11 LIT 0 1344
12 OPR 0 10
13 JMC 0 23
14 LIT 0 1
15 LOD 0 3
16 OPR 0 2
17 STO 0 3
18 LIT 0 1
19 LOD 0 4
20 OPR 0 2
21 STO 0 4
22 JMP 0 10
23 LOD 0 3
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
        code = start_compiler("../sample_input/program.swift")
        self.assertEqual("""0 INT 0 3
1 JMP 0 28
2 INT 0 3
3 LOD 0 -1
4 INT 0 1
5 LIT 0 20
6 STO 0 4
7 LIT 0 52
8 LIT 0 43
9 OPR 0 12
10 JMC 0 21
11 INT 0 1
12 LOD 0 3
13 STO 0 5
14 LIT 0 20
15 STO 0 5
16 LIT 0 32
17 LOD 0 4
18 OPR 0 4
19 STO 0 4
20 JMP 0 25
21 LIT 0 10
22 LOD 0 4
23 OPR 0 4
24 STO 0 4
25 LOD 0 4
26 STO 0 -2
27 RET 0 0
28 JMP 0 50
29 INT 0 3
30 LOD 0 -1
31 INT 0 1
32 LIT 0 1
33 STO 0 4
34 LOD 0 4
35 LIT 0 21
36 OPR 0 10
37 JMC 0 47
38 LOD 0 4
39 LIT 0 5
40 OPR 0 2
41 STO 0 3
42 LIT 0 1
43 LOD 0 4
44 OPR 0 2
45 STO 0 4
46 JMP 0 34
47 LOD 0 3
48 STO 0 -2
49 RET 0 0
50 JMP 0 77
51 INT 0 3
52 LOD 0 -2
53 LOD 0 -1
54 INT 0 1
55 LIT 0 1
56 STO 0 5
57 LOD 0 5
58 LIT 0 20
59 OPR 0 10
60 JMC 0 74
61 LIT 0 1
62 LOD 0 3
63 OPR 0 2
64 STO 0 3
65 LIT 0 2
66 LOD 0 4
67 OPR 0 2
68 STO 0 4
69 LIT 0 1
70 LOD 0 5
71 OPR 0 2
72 STO 0 5
73 JMP 0 57
74 LOD 0 3
75 STO 0 -3
76 RET 0 0
77 JMP 0 127
78 INT 0 3
79 LOD 0 -4
80 LOD 0 -3
81 LOD 0 -2
82 LOD 0 -1
83 INT 0 1
84 LIT 0 42
85 STO 0 7
86 INT 0 1
87 LIT 0 1
88 STO 0 8
89 LOD 0 8
90 LIT 0 3
91 OPR 0 10
92 JMC 0 124
93 INT 0 1
94 LIT 0 1
95 STO 0 9
96 LOD 0 9
97 LIT 0 3
98 OPR 0 10
99 JMC 0 119
100 LOD 0 3
101 LOD 0 4
102 OPR 0 4
103 LOD 0 5
104 OPR 0 3
105 LOD 0 6
106 OPR 0 3
107 LOD 0 8
108 OPR 0 2
109 LOD 0 9
110 OPR 0 2
111 LOD 0 7
112 OPR 0 2
113 STO 0 7
114 LIT 0 1
115 LOD 0 9
116 OPR 0 2
117 STO 0 9
118 JMP 0 96
119 LIT 0 1
120 LOD 0 8
121 OPR 0 2
122 STO 0 8
123 JMP 0 89
124 LOD 0 7
125 STO 0 -5
126 RET 0 0
127 INT 0 1
128 LIT 0 0
129 STO 0 7
130 INT 0 1
131 LIT 0 0
132 STO 0 8
133 INT 0 1
134 LIT 0 43
135 CAL 0 2
136 INT 0 -1
137 STO 0 8
138 INT 0 1
139 LOD 0 7
140 LOD 0 8
141 CAL 0 51
142 INT 0 -2
143 STO 0 7
144 INT 0 1
145 LIT 0 52
146 CAL 0 2
147 INT 0 -1
148 STO 0 7
149 INT 0 1
150 LIT 0 42
151 LIT 0 42
152 LIT 0 42
153 LIT 0 42
154 CAL 0 78
155 INT 0 -4
156 STO 0 8
157 RET 0 0
""", code, "program")

    def test_complex_program(self):
        code = start_compiler("../sample_input/complex_program.swift")
        self.assertEqual("""0 INT 0 3
1 INT 0 1
2 LIT 0 52
3 STO 0 3
4 JMP 0 26
5 INT 0 3
6 LOD 0 -1
7 INT 0 1
8 LIT 0 0
9 STO 0 4
10 LOD 0 4
11 LIT 0 2
12 OPR 0 10
13 JMC 0 23
14 LIT 0 1
15 LOD 0 3
16 OPR 0 2
17 STO 0 3
18 LIT 0 1
19 LOD 0 4
20 OPR 0 2
21 STO 0 4
22 JMP 0 10
23 LOD 0 3
24 STO 0 -2
25 RET 0 0
26 INT 0 1
27 LOD 0 3
28 CAL 0 5
29 INT 0 -1
30 STO 0 3
31 LIT 0 100
32 LOD 0 3
33 OPR 0 10
34 JMC 0 45
35 LOD 0 3
36 LIT 0 1
37 OPR 0 3
38 STO 0 3
39 LOD 0 3
40 LIT 0 50
41 OPR 0 12
42 JMC 0 44
43 JMP 0 35
44 JMP 0 65
45 LIT 0 1
46 LOD 0 3
47 OPR 0 10
48 JMC 0 66
49 LIT 0 32
50 LOD 0 3
51 OPR 0 4
52 STO 0 3
53 LOD 0 3
54 LIT 0 43
55 OPR 0 12
56 JMC 0 61
57 LOD 0 3
58 LIT 0 9
59 OPR 0 2
60 JMP 0 64
61 LOD 0 3
62 LIT 0 5
63 OPR 0 2
64 STO 0 3
65 RET 0 0
""", code, "complex_program")
