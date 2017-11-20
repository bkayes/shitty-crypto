from algorithms import *

s = ("Modi nostrum numquam voluptate quos."
     "Expedita soluta et quaerat in aspernatur consequuntur."
     "Quibusdam doloribus ut ut officia."
     "Voluptatum corporis ratione eaque odio cumque libero."
     "Voluptates magni at delectus excepturi et ipsumsaepe.")

square_size = next_square(len(s))
print("Squared:")
sq = square(s, square_size)
prettyprint(sq)
print("Caesar'd:")
sq = caesar(sq, 7)
prettyprint(sq)
print("Cycled:")
sq = cycle(sq, 8)
prettyprint(sq)
print("Reversed:")
sq = reverse(sq)
prettyprint(sq)
print("Rotated:")
sq = rotate(sq, 1)
prettyprint(sq)
print("Shifted:")
sq = shift_val(sq, 89)
prettyprint(sq)

# key format: 0 to 26, 0 to n, 0 to 3, 0 to 93