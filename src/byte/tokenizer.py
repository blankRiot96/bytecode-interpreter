from collections.abc import Callable, Generator, Sequence
from dataclasses import dataclass
from enum import Enum, auto


class TokenType(Enum):
    INTEGER_LITERAL = auto()
    KEYWORD = auto()
    OPERATOR = auto()


@dataclass
class Token:
    token_type: TokenType | None
    value: bytearray

    def __repr__(self) -> str:
        return "'" + "".join(map(chr, self.value)) + "'"


class Walker[T]:
    def __init__(self, sequence: Sequence[T]) -> None:
        self.sequence = sequence
        self.idx = 0

    def __iter__(self):
        return self

    def peek(self) -> T:
        if self.idx == len(self.sequence):
            raise StopIteration

        return self.sequence[self.idx]

    def __next__(self) -> T:
        if self.idx == len(self.sequence):
            raise StopIteration

        result = self.sequence[self.idx]
        self.idx += 1
        return result


def consume(walker: Walker, character: str, condition: Callable, token_type: TokenType) -> Token:
    consumed_value = bytearray(character.encode())
    try:
        while condition(character := walker.peek()):
            consumed_value.append(ord(character))
            next(walker)
    except StopIteration:
        pass

    return Token(token_type, consumed_value)


def constitutes_integer_literal(character: str):
    return character.isdigit()


def constitutes_keyword(character: str):
    return character.isalpha()


def is_operator(character: str):
    return character in ("+", "-", "*", "/")


def tokenize(source: str) -> Generator[Token]:
    walker = Walker(source)
    for character in walker:
        if constitutes_integer_literal(character):
            yield consume(walker, character, constitutes_integer_literal, TokenType.INTEGER_LITERAL)
        elif constitutes_keyword(character):
            yield consume(walker, character, constitutes_keyword, TokenType.KEYWORD)
        elif is_operator(character):
            yield Token(TokenType.OPERATOR, bytearray(character.encode()))
        elif character == " ":
            continue
