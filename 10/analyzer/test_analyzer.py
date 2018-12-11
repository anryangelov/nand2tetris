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


def test_compilation_engine_class_basic():
    in_stream = io.StringIO('class Foo {field int bar1, bar2; field Moo goo;}')
    out_stream = io.StringIO()
    comp_engine = CompilationEngine(in_stream, out_stream)
    data = comp_engine.start()
    import pprint; pprint.pprint(data)
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
    in_stream = io.StringIO(
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
    out_stream = io.StringIO()
    comp_engine = CompilationEngine(in_stream, out_stream)
    data = comp_engine.start()
    import pprint; pprint.pprint(data)
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
                        ('}', 'symbol'),
                    ],
                ],
               ('}', 'symbol'),
            ] == data
