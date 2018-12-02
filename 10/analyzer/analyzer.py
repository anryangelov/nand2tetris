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
        self.output = output_stream
        tokenizer = JackTokenizer(input_stream)
        self.tokenizer = iter(tokenizer)

    def start(self):
        try:
            t = next(self.tokenizer)
            if t.value != 'class':
                raise ParseError(t)
            return self.compile_class(t)

        except StopIteration:
            raise ParseError('Expect more tokens')

        try:
            next(self.tokenizer)
        except StopIteration:
            pass
        else:
            raise ParseError('More tokens than needed')

    def compile_class(self, t):
        data = ['class']
        data.append(t)

        t = next(self.tokenizer)
        if t.type != INDENDIFIER:
            raise ParseError(t)
        data.append(t)

        t = next(self.tokenizer)
        if t.value != '{':
            raise ParseError
        data.append(t)

        t = next(self.tokenizer)
        while t.value in ('static', 'field'):
            d = self.compile_class_var_dec(t)
            data.append(d)
            t = next(self.tokenizer)

        if t.value != '}':
            raise ParseError(t)
        data.append(t)

        return data

    def compile_class_var_dec(self, t):
        data = ['classVarDec']
        data.append(t)

        t = next(self.tokenizer)
        self.raise_if_type_is_wrong(t)
        data.append(t)

        while True:
            t = next(self.tokenizer)
            if t.type != INDENDIFIER:
                raise ParseError(t)
            data.append(t)

            t = next(self.tokenizer)
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



class JackAnalyzer():

    def __init__(self, source):
        self.source = source

    def get_streams(self):
        pass

    def run(self):
        for input_, output in self.get_streams():
            tokenizer = JackAnalyzer(input_)
            CompilationEngine()
