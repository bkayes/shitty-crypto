"""A set of shitty encryption algorithms."""

import string
import math
import secrets
import time
import re


def next_square(n):
    """Finds the next integer which, when squared, is greater than n."""
    return math.ceil(math.sqrt(n))


def pad(text, n):
    """Pad a given text with spaces so it's length is a multiple of n."""
    pad_n = n - len(text) % n
    if pad_n == n:
        return text
    return text + ' ' * pad_n


def chunk(text, n):
    """Chunk text into list of char lists with size n."""
    text = pad(text, n)
    return [list(text[pos:pos + n]) for pos in range(0, len(text), n)]


def square(text, n):
    """Return a square list with n rows and cols of chunks of text."""
    res = chunk(text, n)
    padding = ' ' * n
    if len(res) > n:
        print("Text length must be less than n squared.")
        exit(1)
    while len(res) < n:
        res.append(padding)
    return list(res)


def square_back(square):
    """Given a square list of text, return the original text string."""
    res = ''
    for l in square:
        for c in l:
            res += str(c)
    return res.strip()


def rotate(square, n=1):
    """Given a square list, rotate it clockwise by n turns."""
    n = abs(n)
    if n != 0:
        square = rotate(list(zip(*square[::-1])), n - 1)
    return [list(l) for l in square]


def rotate_back(square, n=1):
    """Given a square list, rotate it counterclockwise by n turns."""
    n = abs(n)
    if n != 0:
        square = rotate_back(list(zip(*square))[::-1], n - 1)
    return [list(l) for l in square]


def reverse(square):
    """Reverse the rows of the square."""
    return list(reversed(square))


def caesar(square, shift):
    """Caesar shift all letters in the square."""
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    alphabet = lower + upper
    shifted_alphabet = (lower[shift:] + lower[:shift] +
                        upper[shift:] + upper[:shift])
    trans = str.maketrans(alphabet, shifted_alphabet)
    return [[c.translate(trans) for c in l] for l in square]


def caesar_back(square, shift):
    """Reverses the caesar shift."""
    return caesar(square, -shift)


def cycle(square, n):
    """Cycles the character order of each row."""
    i = n
    res = []
    for l in square:
        res.append(l[i:] + l[:i])
    return res


def cycle_back(square, n):
    """Reverses the cycled character order of each row."""
    return cycle(square, -n)


def shift(square, n):
    """Shifts all ASCII values by n."""
    return [[chr((ord(c) + n) % 127) for c in l] for l in square]


def shift_back(square, n):
    """Shifts all ASCII values back by n."""
    return shift(square, -n)


def generate_key(square_size):
    """
    The key specifies the argument n for each algorithm.

    The order is: caesar, cycle, rotate, shift_val.
    """
    key_form = [26, square_size, 4, 94]
    return [secrets.randbelow(n) for n in key_form]


def check_key(key, square_size):
    """Checks if the given key is in a valid format."""
    return (
        key[0] in range(0, 26) and
        key[1] in range(0, square_size) and
        key[2] in range(0, 4) and
        key[3] in range(0, 94)
    )


def encrypt(s, key):
    size = next_square(len(s))

    print("Squared:")
    sq = square(s, size)
    prettyprint(sq)

    print("Caesar'd:")
    sq = caesar(sq, key[0])
    prettyprint(sq)

    print("Cycled:")
    sq = cycle(sq, key[1])
    prettyprint(sq)

    print("Reversed:")
    sq = reverse(sq)
    prettyprint(sq)

    print("Rotated:")
    sq = rotate(sq, key[2])
    prettyprint(sq)

    print("Shifted:")
    sq = shift(sq, key[3])
    prettyprint(sq)
    return sq


def decrypt(sq, key):
    sq = shift_back(sq, key[3])
    sq = rotate_back(sq, key[2])
    sq = reverse(sq)
    sq = cycle_back(sq, key[1])
    sq = caesar_back(sq, key[0])
    s = square_back(sq)
    return s


def score_text(s):
    score = 0
    for c in s:
        if c in string.ascii_letters or c == ' ':
            score += 1
    return score


def list_to_str(sq):
    return ''.join(str(item) for row in sq for item in row)


def prettyprint(square):
    """Print the given square in a square"""
    for l in square:
        for c in l:
            print(str(c) + ' ', end='')
        print()
