from pwgen.pwgen import CharsetMinSamples, generate_password
from pwgen.charsets import UPPER, LOWER, DIGITS, SYMBOL, ALL
import random


def test_CharsetMinSamples_exclude():
    tests = (
        ("", "a", ""),
        ("a", "b", "a"),
        ("a", "a", ""),
        ("abc", "abc", ""),
        ("abc", "d", "abc"),
        ("abc", "c", "ab"),
        ("abc", "cb", "a"),
    )
    for charset, exclude_chars, exp in tests:
        charset = CharsetMinSamples(charset, 0)
        charset.exclude(exclude_chars)
        assert charset.charset == exp


def test_generate_password_length_simple():
    charset = CharsetMinSamples(ALL, 0)
    for length in range(1000):
        password = generate_password(length, [charset])
        assert len(password) == length


def test_generate_password_length_complex():
    charsets = [
        CharsetMinSamples(DIGITS, 0),
        CharsetMinSamples("C", 1),
        CharsetMinSamples("D", 1),
    ]

    password = generate_password(2, charsets)
    assert len(password) == 2


def test_generate_password_mandatory_chars_1():
    charsets = [
        CharsetMinSamples("A", 1),
        CharsetMinSamples("B", 1),
        CharsetMinSamples(ALL, 0).exclude("AB")
    ]
    pw = generate_password(10, charsets)

    assert len(pw) == 10
    assert "A" in pw
    assert "B" in pw


def test_generate_password_mandatory_chars_2():
    charsets = [
        CharsetMinSamples("A", 4),
        CharsetMinSamples(ALL, 0)
    ]
    pw = generate_password(10, charsets)

    n_a = sum([1 for c in pw if c == 'A'])
    assert n_a >= 4


def test_generate_password_mandatory_chars_3():
    charsets = [
        CharsetMinSamples(DIGITS, 1),
        CharsetMinSamples(SYMBOL, 1),
        CharsetMinSamples(LOWER, 1),
        CharsetMinSamples(UPPER, 1),
        CharsetMinSamples("T", 2),
    ]
    for length in random.choices(range(6, 100), k=1000):
        pw = generate_password(length, charsets)
        assert len(pw) == length
        
        contains_digit = False
        contains_symbol = False
        contains_lower = False
        contains_upper = False
        number_of_t = 0
        for c in pw:
            if c in DIGITS:
                contains_digit = True
            elif c in SYMBOL:
                contains_symbol = True
            elif c in LOWER:
                contains_lower = True
            elif c in UPPER:
                contains_upper = True
            if c == "T":
                number_of_t += 1

        assert contains_digit
        assert contains_symbol
        assert contains_lower
        assert contains_upper
        assert number_of_t >= 2
