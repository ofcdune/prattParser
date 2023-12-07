from lexer import Lexer, Token
from node import *


class Parser:

    def __init__(self, token_stream: list[Token]):
        self.__tokens = token_stream
        self.__index = 0

    def __get_current_token(self):
        if self.__index >= len(self.__tokens):
            return None
        return self.__tokens[self.__index]

    def __get_lookahead(self):
        if (self.__index + 1) >= len(self.__tokens):
            return None
        return self.__tokens[self.__index + 1]

    def __advance(self):
        self.__index += 1

    def parse(self, precedence: int):
        token = self.__get_current_token()
        match token.type():
            case "int":

                # we use the lookahead specifically at the moment we want to, and 100% before we advance
                la = self.__get_lookahead()
                if la is not None and la.type() == "int":
                    # in this case, if we encounter two integers in a row, we assume that we want to add them
                    # this is because the plus or minus gets consumed as the sign of the integer
                    self.__tokens.insert(self.__index + 1, Token("-", "+"))
                del la

                left = self.__parse_int(token.literal())
            case "abs":
                left = self.__parse_absolute()
                # this advance is done because we also consume something inside the parser
                self.__advance()
            case "(":
                left = self.__parse_group()
                self.__advance()
            case "!":
                left = self.__parse_fact(token)
            case _:
                raise ReferenceError(
                    f"Invalid token at {self.__index}: {token.literal()}"
                )

        next_token = self.__get_current_token()
        if next_token is None:
            return left

        while precedence < next_token.precedence():
            match next_token.type():
                case "-":
                    left = self.__parse_str(left, next_token)
                case ".":
                    left = self.__parse_pkt(left, next_token)
                case _:
                    raise ReferenceError(
                        f"Invalid token at {self.__index}: {next_token.literal()}"
                    )

            next_token = self.__get_current_token()
            if next_token is None:
                break

        return left

    def __parse_int(self, literal: str):
        self.__advance()
        return Integer(literal)

    def __parse_absolute(self):
        self.__advance()

        expression = self.parse(1)
        next_token = self.__get_current_token()
        if next_token is None:
            raise RecursionError(
                "Missing | at end of input"
            )
        elif next_token.type() != "abs_end":
            raise ReferenceError(
                f"Expected |, got {next_token.literal()}"
            )

        return Absolute(expression)

    def __parse_group(self):
        self.__advance()

        expression = self.parse(1)
        next_token = self.__get_current_token()
        if next_token is None:
            raise RecursionError(
                "Missing ) at end of input"
            )
        elif next_token.type() != ")":
            raise ReferenceError(
                f"Expected ), got {next_token.literal()}"
            )

        return expression

    def __parse_str(self, left: Node, current_token: Token):
        self.__advance()
        right = self.parse(current_token.precedence())

        match current_token.literal():
            case "+":
                return Addition(left, right)
            case "-":
                return Subtraction(left, right)
            case _:
                raise ReferenceError(
                    f"Invalid token at {self.__index}: {current_token.literal()}"
                )

    def __parse_pkt(self, left: Node, current_token: Token):
        self.__advance()
        right = self.parse(current_token.precedence())
        match current_token.literal():
            case "*":
                return Multiplication(left, right)
            case "/":
                return Division(left, right)
            case _:
                raise ReferenceError(
                    f"Invalid token at {self.__index}: {current_token.literal()}"
                )

    def __parse_fact(self, current_token: Token):
        self.__advance()
        right = self.parse(current_token.precedence())
        return Factorial(right)


if __name__ == '__main__':

    math = input("Please enter a mathematical formula: ")
    lexer = Lexer(math)
#
    parser = Parser(lexer.get_token_stream())
    result = parser.parse(1)

    print(result.evaluate())
