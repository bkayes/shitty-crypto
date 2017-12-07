#!/usr/bin/env python3
"""Simple command line tool to decrypt text encrypted badly."""

from algorithms import *
import json

key = [-1, -1, -1, -1]
ct_filename = 'ciphertext.out'
with open(ct_filename, 'r') as f:
    ct = json.load(f)

square_size = len(ct)

# BREAK SHIFT CIPHER #

scores = []

for test_shift in range(0, 94):
    key[3] = test_shift
    test_unshift = shift_back(ct, key[3])
    score = score_text(list_to_str(test_unshift))
    scores.append(score)

m = max(scores)
best = [i for i, j in enumerate(scores) if j == m]

for shift in best:
    print('Candidate shift: ', shift)
    uncaesared = shift_back(ct, shift)
    print('Shifted back:')
    prettyprint(uncaesared)
    print()

key[3] = int(input('Please select the best shift: '))
ct = shift_back(ct, key[3])

# BREAK CAESAR #

for test_shift in range(0, 26):
    key[0] = test_shift
    test_uncaesar = caesar_back(ct, key[0])
    print('Shift: ', test_shift)
    print('Caesared Back:')
    prettyprint(test_uncaesar)
    print()

key[0] = int(input('Please select the best shift: '))
ct = caesar_back(ct, key[0])

# BREAK ROTATION #

for rot in range(0, 4):
    key[2] = rot
    test_rot = reverse(rotate_back(ct, key[2]))
    print('Rot: ', rot)
    print('Rotated Back & Reversed:')
    prettyprint(test_rot)
    print()

key[2] = int(input('Please select the best rotation: '))
ct = reverse(rotate_back(ct, key[2]))

# BREAK CYCLE #

for cyc in range(0, square_size + 1):
    key[1] = cyc
    test_cyc = cycle_back(ct, key[1])
    print('Cyc: ', cyc)
    print('Cycled Back: ')
    prettyprint(test_cyc)
    print()

key[1] = int(input('Please select the best cycle: '))
ct = cycle_back(ct, key[1])

pt = square_back(ct)
print('Key: ', key)
print('Totally decrypted plaintext: ')
print(pt)
