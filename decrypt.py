#!/usr/bin/env python3
"""Simple command line tool to decrypt text encrypted badly."""

from algorithms import *
import pickle

key = [-1, -1, -1, -1]
ct_filename = 'ciphertext.out'
with open(ct_filename, 'rb') as f:
    ct = pickle.load(f)

square_size = len(ct)

while not check_key(key, square_size):
    print("Please input your valid key values: ")
    key[0] = int(input("Caesar Key: "))
    key[1] = int(input("Shift Key: "))
    key[2] = int(input("Rotate Key: "))
    key[3] = int(input("Shift Key: "))

pt = decrypt(ct, key)
print("Decrypted Plaintext:")
print(pt)
