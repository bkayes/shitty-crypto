"""A set of shitty encryption algorithms."""

import string
import math
import secrets


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


def rotate(square, n=1):
    """Given a square list, rotate it clockwise by one turn."""
    n = abs(n)
    if n != 0:
        square = rotate(list(zip(*square[::-1])), n - 1)
    return [list(l) for l in square]


def reverse(square):
    """Reverse the rows of the square."""
    return list(reversed(square))


def caesar(square, shift):
    """Caesar shift all letters in the square."""
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return [[c.translate(table) for c in l] for l in square]


def cycle(square, n):
    i = n
    res = []
    for l in square:
        res.append(l[i:] + l[:i])
    return res


# Because of the printable check, decryption may be weird/difficult.
# If this is the case, remove that part.
def shift_val(square, n):
    """
    Shifts all ASCII values by n.

    Ensures that only printable characters are valid shifts.
    """
    n = n % 94 + 32
    return [[chr(((ord(c) + n) % 94 + 33)) for c in l] for l in square]


def generate_key(square_size):
    """
    The key specifies the argument n for each algorithm.

    The order is: caesar, cycle, rotate, shift_val.
    """
    key_form = [26, square_size, 3, 93]
    return [secrets.randbelow(n + 1) for n in key_form]


def prettyprint(square):
    """Print the given square in a square"""
    for l in square:
        for c in l:
            print(str(c) + ' ', end='')
        print()
