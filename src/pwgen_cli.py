import argparse
import sys
from typing import Any
from pwgen.charsets import UPPER, LOWER, DIGITS, SYMBOL
from pwgen.pwgen import CharsetMinSamples, generate_password 

"""
    pwgen custom <length> (charset, min)+
    pwgen test <pwd>


"""


def is_integer(func):
    def integer(n: Any):
        n = int(n)
        return func(n)
    return integer


def is_non_negative(func):
    def non_negative(n: float):
        if n < 0:
            raise argparse.ArgumentTypeError(
                f'{n} is negative!'
            )
        return func(n)
    return non_negative


def is_positive(func):
    def positive(n: float):
        if n <= 0:
            raise argparse.ArgumentTypeError(
                f'{n} is not positive!'
            )
        return func(n)
    return positive


@is_integer
@is_non_negative
def non_neg_int(n: Any) -> int:
    return n


@is_integer
@is_positive
def pos_int(n: Any) -> int:
    return n


def main():
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument(
        "length",
        type=pos_int,
        metavar='<length>',
        help='password length'
    )
    parser.add_argument(
        '-l', '--lower',
        metavar='<int>',
        dest='n_lower',
        type=non_neg_int,
        default=1,
        help="min amount of lower case characters",
    )
    parser.add_argument(
        '-u', '--upper',
        metavar='<int>',
        dest='n_upper',
        type=non_neg_int,
        default=1,
        help="min amount of upper case characters"
    )
    parser.add_argument(
        '-d', '--digit',
        metavar='<int>',
        dest='n_digit',
        type=non_neg_int,
        default=1,
        help='min amount of digits'
    )
    parser.add_argument(
        '-s', '--symbol',
        metavar='<int>',
        dest='n_symbol',
        type=non_neg_int,
        default=1,
        help='min amount of symbols'
    )
    parser.add_argument(
        '-i', '--include',
        metavar='<str>',
        dest='include',
        type=str,
        default='',
        help='include specified characters at least once'
    )
    parser.add_argument(
        '-e', '--exclude',
        metavar='<str>',
        dest='exclude',
        type=str,
        default='',
        help=("exclude specified characters."
              " Overwrites other specifications")
    )
    args = parser.parse_args()

    # build charsets
    charsets = [
        CharsetMinSamples(LOWER, args.n_lower),
        CharsetMinSamples(UPPER, args.n_upper),
        CharsetMinSamples(DIGITS, args.n_digit),
        CharsetMinSamples(SYMBOL, args.n_symbol)
    ]
    # include explicitly
    for c in args.include:
        charsets.append(CharsetMinSamples(c, 1))
    
    # exclude explicitly
    charsets = [cs.exclude(args.exclude) for cs in charsets]

    # validate charsets:
    charsets = [cs for cs in charsets if len(cs.charset) and cs.n_samples > 0]

    if not charsets:
        print(f"Cannot generate password of length {args.length}"
              " from empty charsets!"
              )
        sys.exit(1)
    password = generate_password(args.length, charsets)

    return password

