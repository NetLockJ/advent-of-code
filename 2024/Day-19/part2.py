from itertools import permutations
from functools import cache

@cache
def combs(s: str):
    return s == '' or sum(combs(s.removeprefix(p)) for p in towels if s.startswith(p))

inp = open("input.txt", "r").read().split("\n\n")

towels = inp[0].replace(" ", "").split(",")
patterns = inp[1].split("\n")

valid = 0

for pattern in patterns:
    valid += combs(pattern)

print(valid)