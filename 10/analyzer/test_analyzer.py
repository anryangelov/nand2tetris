import io

from analyzer import Token, JackTokenizer, CompilationEngine


def test_jack_tokenizer_basic():
    tokenizer = JackTokenizer(io.StringIO('class {}'))
    token = tokenizer.advance()
    assert token.value == 'class'
    assert token.type == 'keyword'


def test_jack_tokenizer():
    tokenizer = JackTokenizer(io.StringIO('''class Bar {
                                                    method Fraction foo(int y) {
                                                        var String bar;
                                                        let bar = "b33 g44";
                                                        var int temp; // a variable
                                                        let temp =  ( xxx+ 12)*-63;
                                                    }
                                                }'''))
    t = tokenizer.advance()
    assert t.value == 'class'
    assert t.type == 'keyword'

    t = tokenizer.advance()
    assert t.type == 'identifier'
    assert t.value == 'Bar'

    t = tokenizer.advance()
    assert t.value == '{'
    assert t.type == 'symbol'

    t = tokenizer.advance()
    assert t.value == 'method'
    assert t.type == 'keyword'

    t = tokenizer.advance()
    assert t.value == 'Fraction'
    assert t.type == 'identifier'

    t = tokenizer.advance()
    assert t.value == 'foo'
    assert t.type == 'identifier'

    t = tokenizer.advance()
    assert t.value == '('
    assert t.type == 'symbol'

    t = tokenizer.advance()
    assert t.value == 'int'
    assert t.type == 'keyword'

    t = tokenizer.advance()
    assert t.value == 'y'
    assert t.type == 'identifier'

    t = tokenizer.advance()
    assert t.value == ')'
    assert t.type == 'symbol'

    t = tokenizer.advance()
    assert t.value == '{'
    assert t.type == 'symbol'

    t = tokenizer.advance()
    assert t.value == 'var'
    assert t.type == 'keyword'

    t = tokenizer.advance()
    assert t.value == 'String'
    assert t.type == 'identifier'

    t = tokenizer.advance()
    assert t.value == 'bar'
    assert t.type == 'identifier'

    t = tokenizer.advance()
    assert t.value == ';'
    assert t.type == 'symbol'

    t = tokenizer.advance()
    assert t.value == 'let'
    assert t.type == 'keyword'

    t = tokenizer.advance()
    assert t.value == 'bar'
    assert t.type == 'identifier'

    t = tokenizer.advance()
    assert t.value == '='
    assert t.type == 'symbol'

    t = tokenizer.advance()
    assert t.value == 'b33 g44'
    assert t.type == 'stringConst'

    t = tokenizer.advance()
    assert t.value == ';'
    assert t.type == 'symbol'

    t = tokenizer.advance()
    assert t.value == 'var'
    assert t.type == 'keyword'

    t = tokenizer.advance()
    assert t.value == 'int'
    assert t.type == 'keyword'

    t = tokenizer.advance()
    assert t.value == 'temp'
    assert t.type == 'identifier'

    t = tokenizer.advance()
    assert t.value == ';'
    assert t.type == 'symbol'

    t = tokenizer.advance()
    assert t.value == 'let'
    assert t.type == 'keyword'

    t = tokenizer.advance()
    assert t.value == 'temp'
    assert t.type == 'identifier'

    t = tokenizer.advance()
    assert t.value == '='
    assert t.type == 'symbol'

    t = tokenizer.advance()
    assert t.value == '('
    assert t.type == 'symbol'

    t = tokenizer.advance()
    assert t.value == 'xxx'
    assert t.type == 'identifier'

    t = tokenizer.advance()
    assert t.value == '+'
    assert t.type == 'symbol'

    t = tokenizer.advance()
    assert t.value == '12'
    assert t.type == 'integerConst'

    t = tokenizer.advance()
    assert t.value == ')'
    assert t.type == 'symbol'

    t = tokenizer.advance()
    assert t.value == '*'
    assert t.type == 'symbol'

    t = tokenizer.advance()
    assert t.value == '-'
    assert t.type == 'symbol'

    t = tokenizer.advance()
    assert t.value == '63'
    assert t.type == 'integerConst'

    t = tokenizer.advance()
    assert t.value == ';'
    assert t.type == 'symbol'

    t = tokenizer.advance()
    assert t.value == '}'
    assert t.type == 'symbol'

    t = tokenizer.advance()
    assert t.value == '}'
    assert t.type == 'symbol'


def get_comp_engine(code):
    in_stream = io.StringIO(code)
    out_stream = io.StringIO()
    return CompilationEngine(in_stream, out_stream)


def test_compilation_engine_class_basic():
    comp_engine = get_comp_engine('class Foo {field int bar1, bar2; field Moo goo;}')
    data = comp_engine.start()
    assert  ['class',
                ('class', 'keyword'),
                ('Foo', 'identifier'),
                ('{', 'symbol'),
                ['classVarDec',
                    ('field', 'keyword'),
                    ('int', 'keyword'),
                    ('bar1', 'identifier'),
                    (',', 'symbol'),
                    ('bar2', 'identifier'),
                    (';', 'symbol')],
                ['classVarDec',
                    ('field', 'keyword'),
                    ('Moo', 'identifier'),
                    ('goo', 'identifier'),
                    (';', 'symbol')],
               ('}', 'symbol')
            ] == data


def test_compilation_engine_class():
    comp_engine = get_comp_engine(
    '''class Foo {

        field int bar1, bar2;
        field Moo goo;

        // define method here
        method Foo method_name (int int_var, Goo goo_var) {
            var char letter;
            var int i, j, k;
        }

        // define function without parameters
        function void function_void() {}
    }
    ''')
    data = comp_engine.start()
    # import pprint; pprint.pprint(data)
    assert  ['class',
                ('class', 'keyword'),
                ('Foo', 'identifier'),
                ('{', 'symbol'),
                ['classVarDec',
                    ('field', 'keyword'),
                    ('int', 'keyword'),
                    ('bar1', 'identifier'),
                    (',', 'symbol'),
                    ('bar2', 'identifier'),
                    (';', 'symbol')],
                ['classVarDec',
                    ('field', 'keyword'),
                    ('Moo', 'identifier'),
                    ('goo', 'identifier'),
                    (';', 'symbol')],
                ['subroutineDec',
                    ('method', 'keyword'),
                    ('Foo', 'identifier'),
                    ('method_name', 'identifier'),
                    ('(', 'symbol'),
                    ['parameterList',
                        ('int', 'keyword'),
                        ('int_var', 'identifier'),
                        (',', 'symbol'),
                        ('Goo', 'identifier'),
                        ('goo_var', 'identifier'),
                    ],
                    (')', 'symbol'),
                    ['subroutineBody',
                        ('{', 'symbol'),
                        ['varDec',
                            ('var', 'keyword'),
                            ('char', 'keyword'),
                            ('letter', 'identifier'),
                            (';', 'symbol'),
                        ],
                        ['varDec',
                            ('var', 'keyword'),
                            ('int', 'keyword'),
                            ('i', 'identifier'),
                            (',', 'symbol'),
                            ('j', 'identifier'),
                            (',', 'symbol'),
                            ('k', 'identifier'),
                            (';', 'symbol'),
                        ],
                        ['statements'],
                        ('}', 'symbol'),
                    ]
                ],
                ['subroutineDec',
                    ('function', 'keyword'),
                    ('void', 'keyword'),
                    ('function_void', 'identifier'),
                    ('(', 'symbol'),
                    ['parameterList'],
                    (')', 'symbol'),
                    ['subroutineBody',
                        ('{', 'symbol'),
                        ['statements'],
                        ('}', 'symbol'),
                    ],
                ],
               ('}', 'symbol'),
            ] == data


def test_compile_expression_basic():
    comp_engine = get_comp_engine('true;')
    data = comp_engine.compile_expression(Token('true', 'keyword'))
    ['expression',
        ['term',
         Token(value='true', type='keyword')
        ]
    ] == data


def test_compile_expression_1():
    comp_engine = get_comp_engine('(3 + x) - (4 + 2);')
    data = comp_engine.compile_expression(Token('3', 'integerConst'))
    ['expression',
        ['term',
            Token(value='(', type='symbol'),
            ['expression',
                ['term', Token(value='3', type='integerConst')],
                Token(value='+', type='symbol'),
                ['term', Token(value='x', type='identifier')]],
            Token(value=')', type='symbol')],
        Token(value='-', type='symbol'),
        ['term',
            Token(value='(', type='symbol'),
            ['expression',
                ['term', Token(value='4', type='integerConst')],
                Token(value='+', type='symbol'),
                ['term', Token(value='2', type='integerConst')]],
            Token(value=')', type='symbol')]] == data[0]


def test_compile_expression_2():
    comp_engine = get_comp_engine('4 + Foo.bar(arg1, 3);')
    data = comp_engine.compile_expression(Token('4', 'integerConst'))
    ['expression',
        ['term', Token(value='4', type='integerConst')],
        Token(value='+', type='symbol'),
        ['term',
            [Token(value='Foo', type='identifier'),
             Token(value='.', type='symbol'),
             Token(value='bar', type='identifier'),
             Token(value='(', type='symbol'),
                ['expressionList',
                    ['expression',
                        ['term', Token(value='arg1', type='identifier')]],
                    Token(value=',', type='symbol'),
                    ['expression',
                        ['term', Token(value='3', type='integerConst')]]],
                Token(value=')', type='symbol')]]] == data[0]


def test_compile_expression_3():
    comp_engine = get_comp_engine('bar();')
    data = comp_engine.compile_expression(Token('bar', 'identifier'))
    ['expression',
     ['term',
      [Token(value='bar', type='identifier'),
       Token(value='(', type='symbol'),
       ['expressionList'],
       Token(value=')', type='symbol')]]] == data[0]


def test_compile_let_1():
    comp_engine = get_comp_engine('foo = BAR; ;')
    data = comp_engine.compile_let(Token('let', 'keyword'))
    ['letStatement',
        Token(value='let', type='keyword'),
        Token(value='foo', type='identifier'),
        Token(value='=', type='symbol'),
        ['expression',
            ['term',
                Token(value='BAR', type='identifier')
            ]
        ],
        Token(value=';', type='symbol')
    ] == data[0]


def test_compile_let_2():
    comp_engine = get_comp_engine('foo[4] = BAR; ;')
    data = comp_engine.compile_let(Token('let', 'keyword'))
    ['letStatement',
        Token(value='let', type='keyword'),
        Token(value='foo', type='identifier'),
        Token(value='[', type='symbol'),
        ['expression', 
            ['term', Token(value='4', type='integerConst')]
        ],
        Token(value=']', type='symbol'),
        Token(value='=', type='symbol'),
        ['expression',
            ['term', Token(value='BAR', type='identifier')]
        ],
        Token(value=';', type='symbol')
    ] == data[0]


def test_compile_if_1():
    comp_engine = get_comp_engine('(true) {let x = 2;};')
    data = comp_engine.compile_if(Token('if', 'keyword'))
    ['ifStatemetn',
        Token(value='if', type='keyword'),
        Token(value='(', type='symbol'),
        ['expression',
            ['term', Token(value='true', type='keyword')]
        ],
        Token(value=')', type='symbol'),
        Token(value='{', type='symbol'),
        ['statements',
            ['letStatement',
                Token(value='let', type='keyword'),
                Token(value='x', type='identifier'),
                Token(value='=', type='symbol'),
                ['expression',
                    ['term', Token(value='2', type='integerConst')]
                ],
                Token(value=';', type='symbol')
            ]
        ],
        Token(value='}', type='symbol')
    ] == data[0]


def test_compile_if_2():
    comp_engine = get_comp_engine('(true) {} else {let x = 9;};')
    data = comp_engine.compile_if(Token('if', 'keyword'))
    ['ifStatemetn',
        Token(value='if', type='keyword'),
        Token(value='(', type='symbol'),
        ['expression',
            ['term', Token(value='true', type='keyword')]
        ],
        Token(value=')', type='symbol'),
        Token(value='{', type='symbol'),
        ['statements'],
        Token(value='}', type='symbol'),
        Token(value='else', type='keyword'),
        Token(value='{', type='symbol'),
        ['statements',
            ['letStatement',
                Token(value='let', type='keyword'),
                Token(value='x', type='identifier'),
                Token(value='=', type='symbol'),
                ['expression',
                    ['term', Token(value='9', type='integerConst')]
                ],
                Token(value=';', type='symbol')
            ]
        ],
        Token(value='}', type='symbol')
    ] == data[0]


def test_compile_while():
    comp_engine = get_comp_engine('(true) { do foo();};')
    data = comp_engine.compile_while(Token('while', 'keyword'))
    ['whileStatement',
        Token(value='while', type='keyword'),
        Token(value='(', type='symbol'),
        ['expression',
            ['term', Token(value='true', type='keyword')]
        ],
        Token(value=')', type='symbol'),
        Token(value='{', type='symbol'),
        ['statements',
            ['doStatement',
                Token(value='do', type='keyword'),
                Token(value='foo', type='identifier'),
                Token(value='(', type='symbol'),
                ['expressionList'],
                Token(value=')', type='symbol')
            ]
        ],
        Token(value='}', type='symbol')
    ] == data[0]


def test_compile_do():
    comp_engine = get_comp_engine('foo();;')
    data = comp_engine.compile_do(Token('do', 'keyword'))
    ['doStatement',
        Token(value='do', type='keyword'),
        Token(value='foo', type='identifier'),
        Token(value='(', type='symbol'),
        ['expressionList'],
        Token(value=')', type='symbol')
    ] == data[0]
