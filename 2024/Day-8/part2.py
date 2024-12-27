import numpy as np
from collections import defaultdict
from itertools import combinations

def diagonal(i,j,v):
    k = 0
    while i + k * v.real in range(len(grid)) and j + k * v.imag in range(len(grid[0])):
        locations.add(complex(i + k * v.real, j + k * v.imag))
        grid[int(i + k * v.real)][int(j + k * v.imag)] = "#"
        k += 1
    k = 0
    while i + k * v.real in range(len(grid)) and j + k * v.imag in range(len(grid[0])):
        locations.add(complex(i + k * v.real, j + k * v.imag))
        grid[int(i + k * v.real)][int(j + k * v.imag)] = "#"
        k -= 1


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
        diagonal(comb[0].real, comb[0].imag, vec)

print(len(locations))