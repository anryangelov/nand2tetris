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

    def advance(self):
        return self.tokenizer.advance()

    def advance_if_value(self, value):
        t = self.advance()
        if t.value != value:
            raise ParseError(t)
        return t

    def advance_if_type(self, type_):
        t = self.advance()
        if t.type != type_:
            raise ParseError(t)
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

    def compile_class(self, t):
        data = ['class', t]

        t = self.advance_if_type(INDENDIFIER)
        data.append(t)

        t = self.advance_if_value('{')
        data.append(t)

        t = self.advance()
        while t.value in ('static', 'field'):
            d = self.compile_var_dec(t, structure='classVarDec')
            data.append(d)
            t = self.tokenizer.advance()

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

        t = self.advance_if_type(INDENDIFIER)
        data.append(t)

        t = self.advance_if_value('(')
        data.append(t)

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

        t = self.advance_if_value('{')
        data.append(t)

        while True:
            t = self.advance()
            if t.value != 'var':
                break

            d = self.compile_var_dec(t, structure='varDec')
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


class JackAnalyzer():

    def __init__(self, source):
        self.source = source

    def get_streams(self):
        pass

    def run(self):
        for input_, output in self.get_streams():
            tokenizer = JackAnalyzer(input_)
            CompilationEngine()
