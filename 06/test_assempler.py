import io

import pytest

import assempler


@pytest.mark.parametrize(
    "command, expected_result",
    [('M=1', '1110111111001000'),
     ('D=D-A', '1110010011010000'),
     ('D;JGT', '1110001100000001'),
     ('0;JMP', '1110101010000111')])
def test_translate_c_command(command, expected_result):
    got_result = assempler.translate_c_command(command)
    assert expected_result == got_result


@pytest.mark.parametrize(
    "command, expected_result",
    [('134', '000000010000110'),
     ('KBD', '110000000000000'),
     ('user_var', '000000100101100'),
     ('R4', '000000000000100')])
def test_traslate_symbol_command(command, expected_result):
    got_result = assempler.translate_symbol_command(
        command, symbol_table={'user_var': 300})
    assert expected_result == got_result


def test_translate():
    assemply = '''
    // Adds 1 + ... + 100
    @i
    M=1 // i=1
    @sum
    M=0 // sum=0
(LOOP)
    @i
    D=M // D=i
    @100
    D=D-A // D=i-100
    @END
    D;JGT // if (i-100)>0 goto END
    @i
    D=M // D=i
    @sum
    M=D+M // sum=sum+i
    @i
    M=M+1 // i=i+1
    @LOOP
    0;JMP // goto LOOP
(END)
    @END
    0;JMP // infinite loop
    '''

    machine_language = \
'''0000000000010000
1110111111001000
0000000000010001
1110101010001000
0000000000010000
1111110000010000
0000000001100100
1110010011010000
0000000000010010
1110001100000001
0000000000010000
1111110000010000
0000000000010001
1111000010001000
0000000000010000
1111110111001000
0000000000000100
1110101010000111
0000000000010010
1110101010000111
'''

    stream = io.StringIO()
    stream.write(assemply)
    stream.seek(0)

    got_result = assempler.translate(stream)

    assert machine_language == got_result
