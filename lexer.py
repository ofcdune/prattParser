class Token:

    def __init__(self, token_type: str, literal=None):
        self.__type = token_type
        self.__literal = literal

    def precedence(self):
        return {
            "int": 1,
            '-': 2,
            '.': 3,
            '!': 3,
            '^': 4
        }.get(self.__type, 1)

    def type(self):
        return self.__type

    def literal(self):
        return self.__literal

    def __str__(self):
        return f"Token(\"{self.__type}\"{': ' + self.__literal if self.__literal is not None else ''})"


class Lexer:

    def __init__(self, input_: str):
        self.__input = input_
        self.__pos = 0

    def __advance(self):
        self.__pos += 1

    def __get_current_char(self):
        if self.__pos >= len(self.__input):
            return None
        return self.__input[self.__pos]

    def get_token_stream(self):
        absolute_count = 0
        token_stream = []

        while self.__pos < len(self.__input):
            match self.__get_current_char():
                case ' ':
                    self.__advance()
                case '(':
                    self.__advance()
                    token_stream.append(Token('('))
                case ')':
                    self.__advance()
                    token_stream.append(Token(')'))
                case '!':
                    self.__advance()
                    token_stream.append(Token('!'))
                case '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9':
                    token_stream.append(self.__get_integer())
                case '+':
                    self.__advance()
                    token_stream.append(Token('-', '+'))
                case '-':
                    self.__advance()
                    token_stream.append(Token('-', '-'))
                case '*':
                    self.__advance()
                    token_stream.append(Token('.', '*'))
                case '/':
                    self.__advance()
                    token_stream.append(Token('.', '/'))
                case '^':
                    self.__advance()
                    token_stream.append(Token("power", '^'))
                case '|':
                    self.__advance()
                    if absolute_count == 0:
                        absolute_count = 1
                        token_stream.append(Token("abs"))
                    else:
                        absolute_count = 0
                        token_stream.append(Token("abs_end"))
                case _:
                    raise NotImplementedError(
                        f"Unexpected symbol at index {self.__pos}: {self.__get_current_char()}"
                    )

        return token_stream

    def __get_integer(self):
        buffer = []
        curchar = self.__get_current_char()

        # we do this so confidently because the only way to this function is through an integer
        buffer.append(curchar)
        self.__advance()

        if curchar == '0':
            return Token("int", '0')

        while self.__get_current_char() and 48 <= ord(self.__get_current_char()) <= 57:
            buffer.append(self.__get_current_char())
            self.__advance()

        return Token("int", "".join(buffer))


if __name__ == '__main__':
    lexer = Lexer("|(3424*32)!|")
    for token in lexer.get_token_stream():
        print(token)
