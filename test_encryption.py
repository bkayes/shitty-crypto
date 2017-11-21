from algorithms import *

s = ("Modi nostrum numquam voluptate quos."
     "Expedita soluta et quaerat in aspernatur consequuntur."
     "Quibusdam doloribus ut ut officia."
     "Voluptatum corporis ratione eaque odio cumque libero."
     "Voluptates magni at delectus excepturi et ipsumsaepe.")

square_size = next_square(len(s))
key = generate_key(square_size)
print("Key: " + str(key) + "\n")
print("Squared:")
sq = square(s, square_size)
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
sq = shift_val(sq, key[3])
prettyprint(sq)
