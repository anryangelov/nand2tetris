import re
import os
from collections import namedtuple
import xml.etree.ElementTree as ET


KEYWORD = 'keyword'
SYMBOL = 'symbol'
INTEGER = 'integerConst'
STRING = 'stringConst'
INDENDIFIER = 'identifier'

keywords = {'class', 'constructor', 'function',
    'method', 'field', 'static', 'var',
    'int', 'char', 'boolean', 'void', 'true',
    'false', 'null', 'this', 'let', 'do',
    'if', 'else', 'while', 'return'}

symbols = {'{', '}', '(', ')', '[', ']', '.',
    ',', ';', '+', '-', '*', '/', '&',
    '|', '<', '>', '=', ' ~ '}

keyword_const = {'true', 'false', 'null', 'this'}

op = {'+', '-', '*', '/', '&', '|', '<', '>', '='}

unary_op = {'-', ' ~ '}


Token = namedtuple('Token', ['value', 'type'])


class ParseError(Exception):
    pass


class NoMoreTokens(Exception):
    pass


class JackTokenizer:

    def __init__(self, stream):
        self.stream = stream

    def advance(self):
        word = ''
        token = None
        while not token:
            self._advance_if_comment()

            char = self.stream.read(1)

            if not char:  # end of the stream
                raise NoMoreTokens()

            if char == '"':
                value = self._advance_until(char)
                token = Token(value, STRING)
            elif char in symbols and word:
                type_ = JackTokenizer.get_token_type(word)
                token = Token(word, type_)
                self.stream.seek(self.stream.tell() - 1)  # move to previous char (symbol)
            elif char in symbols:
                token = Token(char, SYMBOL)
            elif char.isspace() and word:
                type_ = JackTokenizer.get_token_type(word)
                token = Token(word, type_)
            elif char.isspace():
                pass
            else:
                word += char
        return token

    def _advance_if_comment(self):
        s = self.stream.read(2)
        if s == '//':
            self._advance_until(os.linesep)
        elif s == '/*':
            self._advance_until('*/')
        else:
            self.stream.seek(self.stream.tell() - len(s))  # move to previous char

    def _advance_until(self, border_char):
        consume_chars = []
        current_char = self.stream.read(1)
        while current_char and current_char != border_char:
            consume_chars.append(current_char)
            current_char = self.stream.read(1)
        return ''.join(consume_chars)

    @staticmethod
    def get_token_type(word):
        type_ = None
        if JackTokenizer.is_int(word):
            type_ = INTEGER
        elif word in keywords:
            type_ = KEYWORD
        elif JackTokenizer.is_idendifier(word):
            type_ = INDENDIFIER
        else:
            raise ParseError(word)
        return type_

    @staticmethod
    def is_int(token):
        try:
            i = int(token)
            return True
        except ValueError:
            return False
        if not 0 <= i <= 32767:
            raise ValueError("illigal integer {}".format(token))

    @staticmethod
    def is_idendifier(token):
        return re.search('^[a-zA-Z_][a-zA-Z_0-9]*$', token) is not None


class CompilationEngine:

    def __init__(self, input_stream, output_stream):
        self.output = output_stream
        self.tokenizer = JackTokenizer(input_stream)
        self.peaked_token = None

    def peak(self):
        if self.peaked_token is None:
            t = self.tokenizer.advance()
            self.peaked_token = t
        return self.peaked_token

    def advance(self):
        t = self.peak()
        self.peaked_token = None
        return t

    def advance_if_value(self, value, data=None):
        t = self.advance()
        if t.value != value:
            raise ParseError(t)
        if data:
            data.append(t)
        return t

    def advance_if_type(self, type_, data=None):
        t = self.advance()
        if t.type != type_:
            raise ParseError(t)
        if data:
            data.append(t)
        return t

    def start(self):
        try:
            t = self.advance_if_value('class')
            return self.compile_class(t)
        except NoMoreTokens:
            raise ParseError('Expect more tokens')

        try:
            self.advance()
        except NoMoreTokens:
            pass
        else:
            raise ParseError('More tokens than needed')

    @staticmethod
    def make_xml(data):
        text, inner_d = data
        root = ET.Element(text)
        CompilationEngine._make_sub_elements_xml(inner_d, root)
        return ET.dump(root)

    @staticmethod
    def _make_sub_elements_xml(data, root):
        for d in data:
            if isinstance(d, list):
                text, inner_d = d
                element = ET.SubElement(root, text)
                CompilationEngine.make_xml(inner_d, element)
            elif isinstance(d, Token):
                t = d
                e = ET.SubElement(root, t.value)
                e.text = t.type
            else:
                raise ValueError('unexpected type: ', d)

    def compile_class(self, t):
        data = ['class', t]

        self.advance_if_type(INDENDIFIER, data)
        self.advance_if_value('{', data)

        t = self.advance()
        while t.value in ('static', 'field'):
            d = self.compile_var_dec(t, structure='classVarDec')
            data.append(d)
            t = self.advance()

        while t.value in ('constructor', 'function', 'method'):
            d = self.compile_subroutine_dec(t)
            data.append(d)
            t = self.advance()

        if t.value != '}':
            raise ParseError(t)
        data.append(t)

        return data

    def compile_var_dec(self, t, structure):
        data = [structure, t]

        t = self.advance()
        self.raise_if_type_is_wrong(t)
        data.append(t)

        while True:
            t = self.advance_if_type(INDENDIFIER)
            data.append(t)

            t = self.advance()
            if t.value in (',', ';'):
                data.append(t)
            else:
                raise ParseError(t)

            if t.value == ';':
                break

        return data

    def raise_if_type_is_wrong(self, t):
        if t.type == KEYWORD and t.value in ('int', 'char', 'boolean'):
            return
        if t.type == INDENDIFIER:
            return
        raise ParseError(t)

    def compile_subroutine_dec(self, t):
        data = ['subroutineDec', t]

        t = self.advance()
        if t.value != 'void':
            self.raise_if_type_is_wrong(t)
        data.append(t)

        self.advance_if_type(INDENDIFIER, data)

        self.advance_if_value('(', data)
        d, t = self.parameter_list()
        data.append(d)

        if t.value != ')':
            raise ParseError(t)
        data.append(t)

        d = self.subroutine_body()
        data.append(d)

        return data

    def subroutine_body(self):
        data = ['subroutineBody']

        self.advance_if_value('{', data)

        while True:
            t = self.advance()
            if t.value != 'var':
                break

            d = self.compile_var_dec(t, structure='varDec')
            data.append(d)

        d, t = self.compile_statemets(t)
        data.append(d)

        if t.value != '}':
            raise ParseError(t)
        data.append(t)

        return data

    def parameter_list(self):
        data = ['parameterList']

        t = self.advance()
        if t.value == ')':
            return data, t

        while True:
            self.raise_if_type_is_wrong(t)
            data.append(t)

            t = self.advance_if_type(INDENDIFIER)
            data.append(t)

            t = self.advance()
            if t.value != ',':
                break
            data.append(t)

            t = self.advance()

        return data, t

    def compile_statemets(self, t):
        data = ['statements']

        while True:
            if t.value == 'let':
                d, t = self.compile_let(t)
            elif t.value == 'if':
                d, t = self.compile_if(t)
            elif t.value == 'while':
                d, t = self.compile_while(t)
            elif t.value == 'do':
                d, t = self.compile_do(t)
            elif t.value == 'return':
                d, t = self.compile_return(t)
            else:
                break
            data.append(d)

        return data, t

    def compile_let(self, t):
        data = ['letStatement', t]

        self.advance_if_type(INDENDIFIER, data)
        if self.peak().value == '[':
            self.advance_array(data)

        self.advance_if_value('=', data)

        t = self.advance()
        d, t = self.compile_expression(t)
        data.append(d)

        if t.value != ';':
            raise ParseError(t)
        data.append(t)
        t = self.advance()

        return data, t

    def compile_if(self, t):
        data = ['ifStatemetn', t]

        self.advance_if_value('(', data)
        t = self.advance()
        d, t = self.compile_expression(t)
        data.append(d)
        if t.value != ')':
            raise ParseError(t)
        data.append(t)
        self.advance_if_value('{', data)
        t = self.advance()
        d, t = self.compile_statemets(t)
        data.append(d)
        if t.value != '}':
            raise ParseError(t)
        data.append(t)

        t = self.advance()
        if t.value == 'else':
            data.append(t)
            self.advance_if_value('{', data)
            t = self.advance()
            d, t = self.compile_statemets(t)
            data.append(d)
            if t.value != '}':
                raise ParseError(t)
            data.append(t)
            t = self.advance()

        return data, t

    def compile_do(self, t):
        data = ['doStatement', t]

        t = self.advance()
        d = self.advance_subroutine_call(t)
        data.extend(d)
        self.advance_if_value(';')
        t = self.advance()

        return data, t

    def compile_while(self, t):
        data = ['whileStatement', t]

        self.advance_if_value('(', data)
        d, t = self.compile_expression(self.advance())
        data.append(d)
        if t.value != ')':
            raise ParseError(t)
        data.append(t)
        self.advance_if_value('{', data)
        d, t = self.compile_statemets(self.advance())
        data.append(d)
        if t.value != '}':
            raise ParseError(t)
        data.append(t)
        t = self.advance()

        return data, t

    def compile_return(self, t):
        data = ['returnStatement', t]

        t = self.advance()

        if t.value != ';':
            d, t = self.compile_expression(t)
            data.append(d)
        if t.value != ';':
            raise ParseError(t)
        data.append(t)

        t = self.advance()
        return data, t

    def compile_expression(self, t):
        data = ['expression']

        while True:
            d = self.compile_term(t)
            data.append(d)

            t = self.advance()
            if t.value not in op:
                break
            data.append(t)
            t = self.advance()

        return data, t

    def compile_term(self, t):
        data = ['term']

        t_peak = self.peak()

        if t.type in ('integerConst', 'stringConst', ) or t.value in keyword_const:
            data.append(t)
        elif t.value in unary_op:
            data.append(t)
            d = self.compile_term()
            data.append(d)
        elif t.type is INDENDIFIER and t_peak.value == '[':
            data.append(t)
            self.advance_array(data)
        elif t.type is INDENDIFIER and (t_peak.value == '.' or t_peak.value == '('):
            d = self.advance_subroutine_call(t)
            data.append(d)
        elif t.type is INDENDIFIER:
            data.append(t)
        elif t.value == '(':
            data.append(t)
            t = self.advance()
            d, t = self.compile_expression(t)
            data.append(d)
            if t.value != ')':
                raise ParseError(t)
            data.append(t)
        else:
            raise ValueError(t)

        return data

    def compile_expression_list(self):
        data = ['expressionList']

        if self.peak().value == ')':
            t = self.advance()
            return data, t

        t = self.advance()
        d, t = self.compile_expression(t)
        data.append(d)
        while t.value == ',':
            data.append(t)
            t = self.advance()
            d, t = self.compile_expression(t)
            data.append(d)

        return data, t

    def advance_subroutine_call(self, t):
        data = [t]

        t = self.peak()
        if t.value == '.':
            self.advance()
            data.append(t)
            self.advance_if_type(INDENDIFIER, data)
        self.advance_if_value('(', data)
        d, t = self.compile_expression_list()
        data.append(d)
        if t.value != ')':
            raise ParseError(t)
        data.append(t)
        return data

    def advance_array(self, data):
        self.advance_if_value('[', data)
        t = self.advance()
        d, t = self.compile_expression(t)
        data.append(d)
        if t.value != ']':
            raise ParseError(t)
        data.append(t)


class JackAnalyzer():

    def __init__(self, source):
        self.source = source

    def get_streams(self):
        pass

    def run(self):
        for input_, output in self.get_streams():
            tokenizer = JackAnalyzer(input_)
            CompilationEngine()
