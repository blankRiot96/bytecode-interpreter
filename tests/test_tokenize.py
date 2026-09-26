from byte.tokenizer import Token, TokenType, tokenize


def test_1():
    assert list(tokenize("1 + 2")) == [
        Token(TokenType.INTEGER_LITERAL, bytearray(b"1")),
        Token(TokenType.OPERATOR, bytearray(b"+")),
        Token(TokenType.INTEGER_LITERAL, bytearray(b"2")),
    ]


def test_2():
    assert list(tokenize("1+2")) == [
        Token(TokenType.INTEGER_LITERAL, bytearray(b"1")),
        Token(TokenType.OPERATOR, bytearray(b"+")),
        Token(TokenType.INTEGER_LITERAL, bytearray(b"2")),
    ]


def test_3():
    assert list(tokenize("1+2 * 3 /4 +6")) == [
        Token(TokenType.INTEGER_LITERAL, bytearray(b"1")),
        Token(TokenType.OPERATOR, bytearray(b"+")),
        Token(TokenType.INTEGER_LITERAL, bytearray(b"2")),
        Token(TokenType.OPERATOR, bytearray(b"*")),
        Token(TokenType.INTEGER_LITERAL, bytearray(b"3")),
        Token(TokenType.OPERATOR, bytearray(b"/")),
        Token(TokenType.INTEGER_LITERAL, bytearray(b"4")),
        Token(TokenType.OPERATOR, bytearray(b"+")),
        Token(TokenType.INTEGER_LITERAL, bytearray(b"6")),
    ]
