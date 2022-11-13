#  date: 13. 11. 2022
#  author: Daniel Schnurpfeil
#

from unittest import TestCase

from src.main import main


class Test(TestCase):

    def test_operation(self):
        code = main("../sample_input/operation.swift")
        self.assertEqual("", code, "operation")

    def test_declaration(self):
        code = main("../sample_input/declaration.swift")
        self.assertEqual(" ", code, "operation")

    def test_for(self):
        code = main("../sample_input/for.swift")
        self.assertEqual(" ", code, "for")

    def test_func(self):
        code = main("../sample_input/func.swift")
        self.assertEqual(" ", code, "func")

    def test_func_simple(self):
        code = main("../sample_input/func_simple.swift")
        self.assertEqual("", code, "func_simple")
