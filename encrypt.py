#!/usr/bin/env python3
"""Simple command line tool to encrypt text badly."""

from algorithms import *
import json

key = [-1, -1, -1, -1]
print("Type the text you wish to encrypt:")
pt = input().strip()
square_size = next_square(len(pt))

gen_key = input("Generate a random key (Y/N): ").strip().upper()

if not gen_key or gen_key[0] != 'N':
    key = generate_key(square_size)
else:
    while not check_key(key, square_size):
        print("Please input valid key values: ")
        key[0] = int(input("Caesar Key (0 to 25): "))
        key[1] = int(input("Shift Key (0 to " + str(square_size) + "): "))
        key[2] = int(input("Rotate Key (0 to 3): "))
        key[3] = int(input("Shift Key (0 to 93): "))

print("Secret Key (keep safe): " + str(key))

ct = encrypt(pt, key)

ct_filename = 'ciphertext.out'
with open(ct_filename, 'w') as f:
    json.dump(ct, f)

# ensure it is dumped and decryption is valid
with open(ct_filename, 'r') as f:
    ct = json.load(f)
    assert(pt == decrypt(ct, key))
