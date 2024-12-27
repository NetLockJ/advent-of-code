import numpy as np
from collections import defaultdict
from itertools import combinations

input  = open("input.txt", "r").read()
input = [list(list(l)) for l in open("./input.txt").read().split("\n")]
grid = np.array(input)

antennas = defaultdict(set)
locations = set()

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] != ".":
            antennas[grid[i][j]].add(complex(i, j))
            # locations.add(complex(i,j))

for k, v in antennas.items():
    for comb in combinations(v, 2):
        vec = complex(comb[0].real - comb[1].real, comb[0].imag - comb[1].imag)
        # First, negative vec, second positive vec
        neg = comb[0] + vec
        pos = comb[1] - vec
        if neg.real in range(len(grid)) and neg.imag in range(len(grid[0])):
            locations.add(neg)
        if pos.real in range(len(grid)) and pos.imag in range(len(grid[0])):
            locations.add(pos)
        print(comb, neg, pos)
        
        

print(len(locations))
print(grid)