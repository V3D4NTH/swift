# kiv-fjp

School Project: **Not so Swift Language** compiler

## Description
- input - significantly simplified Swift language constructions
- output - PL/0 instructions
- technology - PLY (Python lex-(Yacc/recursive descent)) / C++ (flex, bison/recursive descent)

# Additional features
- parameters in func can be literal
- return value
- else branch
- for (c like)
- while
- repeat while
- ternary operator
- boolean
-------
todo

[comment]: <> (- for defined in https://docs.swift.org/swift-book/LanguageGuide/ControlFlow.html)


[comment]: <> (    for index in 1...5 { some code })


- array
- string



### project status
**finished**

usage: not_so_swift_compiler.py [-h] -i F_INPUT [-o OUT]
                                [-qt SHOW_TREE_WITH_PYQT5]

Not so swift compiler.

optional arguments:
  -h, --help            show this help message and exit
  -i F_INPUT, --f_input F_INPUT **(mandatory)**
                        path to input file...
  -o OUT, --out OUT     path to output dir...
  -qt SHOW_TREE_WITH_PYQT5, --show_tree_with_pyqt5 SHOW_TREE_WITH_PYQT5
                        True/False (**note** - need pyqt5~=5.15 if True)

