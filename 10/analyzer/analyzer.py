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

    def __init__(self, token=None, message=None):
        if token:
            message = "Unexpected token: ", token


class JackTokenizer:

    def __init__(self, stream):
        self.stream = stream

    def __iter__(self):  # advance
        word = ''
        while True:
            self._advance_if_comment()

            char = self.stream.read(1)

            if not char:  # end of the stream
                break
            elif char == '"':
                value = self._advance_until(char)
                yield Token(value, STRING)
            elif char in symbols:
                if word:
                    type_ = JackTokenizer.get_token_type(word)
                    yield Token(word, type_)
                    word = ''
                yield Token(char, SYMBOL)
            elif char.isspace():
                if word:
                    type_ = JackTokenizer.get_token_type(word)
                    yield Token(word, type_)
                    word = ''
            else:
                word += char

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
        self.token_gen = iter(JackAnalyzer(self.input_stream))
        self.output = output_stream
        self.data = {}

    def advance(self, *args, type_=None):
        t = next(self.token_gen)
        if ((args and t.value not in args) or
            (type_ and t.type != type_)):
            raise ParseError("Unexpected token: ", t)
        return t

    def start(self):
        self.token_gen = iter(JackAnalyzer(self.input_stream))
        try:
            self.advance('class')
            self.data['class'] = self.compile_class()
        except StopIteration:
            pass

    def compile_class(self, token):
        tokens = {}
        for value, type_ in (
                ('class', KEYWORD),
                (None, INDENDIFIER),
                ('{', KEYWORD)
        ):
            t = next(self.token_gen)
            if not (type_ == t.type and value and value == t.value):
                raise ParseError("Unexpected token: ", t)
            tokens[t.type] = t.value

        t = next(self.token_gen)
        if t.value in ('static', 'field'):
            tokens['classVarDec'] = self.compile_class_var_dec(t)

        t = next(self.token_gen)
        if t.value != '}':
            raise ParseError("Unexpected token: ", t)

        return tokens

    def compile_class_var_dec(self, token):
        tokens = {}
        tokens[token.type] = token.value

        t = next(self.token_gen)
        if t.value != 'type':
            ParseError("Unexpected token: ", t)
        tokens[t.type] = t.value

        t = next(self.token_gen)
        if t.type != INDENDIFIER:
            ParseError("Unexpected token: ", t)


class JackAnalyzer():

    def __init__(self, source):
        self.source = source

    def get_streams(self):
        pass

    def run(self):
        for input_, output in self.get_streams():
            tokenizer = JackAnalyzer(input_)
            CompilationEngine()
