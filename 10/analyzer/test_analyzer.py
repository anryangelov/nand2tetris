import io

from analyzer import JackTokenizer


def test_jack_tokenizer():
    tokenizer = iter(JackTokenizer(io.StringIO('class {}')))
    token = next(tokenizer)
    assert token.value == 'class'
    assert token.type == 'keyword'

    tokenizer = iter(JackTokenizer(io.StringIO('''class Bar {
                                                    method Fraction foo(int y) {
                                                        var String bar;
                                                        let bar = "b33 g44";
                                                        var int temp; // a variable
                                                        let temp =  ( xxx+ 12)*-63;
                                                    }
                                                }''')))
    t = next(tokenizer)
    assert t.value == 'class'
    assert t.type == 'keyword'

    t = next(tokenizer)
    assert t.type == 'identifier'
    assert t.value == 'Bar'

    t = next(tokenizer)
    assert t.value == '{'
    assert t.type == 'symbol'

    t = next(tokenizer)
    assert t.value == 'method'
    assert t.type == 'keyword'

    t = next(tokenizer)
    assert t.value == 'Fraction'
    assert t.type == 'identifier'

    t = next(tokenizer)
    assert t.value == 'foo'
    assert t.type == 'identifier'

    t = next(tokenizer)
    assert t.value == '('
    assert t.type == 'symbol'

    t = next(tokenizer)
    assert t.value == 'int'
    assert t.type == 'keyword'

    t = next(tokenizer)
    assert t.value == 'y'
    assert t.type == 'identifier'

    t = next(tokenizer)
    assert t.value == ')'
    assert t.type == 'symbol'

    t = next(tokenizer)
    assert t.value == '{'
    assert t.type == 'symbol'

    t = next(tokenizer)
    assert t.value == 'var'
    assert t.type == 'keyword'

    t = next(tokenizer)
    assert t.value == 'String'
    assert t.type == 'identifier'

    t = next(tokenizer)
    assert t.value == 'bar'
    assert t.type == 'identifier'

    t = next(tokenizer)
    assert t.value == ';'
    assert t.type == 'symbol'

    t = next(tokenizer)
    assert t.value == 'let'
    assert t.type == 'keyword'

    t = next(tokenizer)
    assert t.value == 'bar'
    assert t.type == 'identifier'

    t = next(tokenizer)
    assert t.value == '='
    assert t.type == 'symbol'

    t = next(tokenizer)
    assert t.value == 'b33 g44'
    assert t.type == 'stringConst'

    t = next(tokenizer)
    assert t.value == ';'
    assert t.type == 'symbol'

    t = next(tokenizer)
    assert t.value == 'var'
    assert t.type == 'keyword'

    t = next(tokenizer)
    assert t.value == 'int'
    assert t.type == 'keyword'

    t = next(tokenizer)
    assert t.value == 'temp'
    assert t.type == 'identifier'

    t = next(tokenizer)
    assert t.value == ';'
    assert t.type == 'symbol'

    t = next(tokenizer)
    assert t.value == 'let'
    assert t.type == 'keyword'

    t = next(tokenizer)
    assert t.value == 'temp'
    assert t.type == 'identifier'

    t = next(tokenizer)
    assert t.value == '='
    assert t.type == 'symbol'

    t = next(tokenizer)
    assert t.value == '('
    assert t.type == 'symbol'

    t = next(tokenizer)
    assert t.value == 'xxx'
    assert t.type == 'identifier'

    t = next(tokenizer)
    assert t.value == '+'
    assert t.type == 'symbol'

    t = next(tokenizer)
    assert t.value == '12'
    assert t.type == 'integerConst'

    t = next(tokenizer)
    assert t.value == ')'
    assert t.type == 'symbol'

    t = next(tokenizer)
    assert t.value == '*'
    assert t.type == 'symbol'

    t = next(tokenizer)
    assert t.value == '-'
    assert t.type == 'symbol'

    t = next(tokenizer)
    assert t.value == '63'
    assert t.type == 'integerConst'

    t = next(tokenizer)
    assert t.value == ';'
    assert t.type == 'symbol'

    t = next(tokenizer)
    assert t.value == '}'
    assert t.type == 'symbol'

    t = next(tokenizer)
    assert t.value == '}'
    assert t.type == 'symbol'