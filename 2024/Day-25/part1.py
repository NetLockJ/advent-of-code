import numpy as np
from itertools import dropwhile

grids = open("input.txt", "r").read().replace(".", "0").replace("#", "1").split("\n\n")

keys = []
locks = []

for grid in grids:
    grid = np.array([list(list(map(int, l))) for l in grid.splitlines()])
    if grid[0][0] == 1:
        locks.append(np.sum(grid, axis=0, initial=-1))
    else:
        keys.append(np.sum(grid, axis=0, initial=-1))

total = 0

for lock in locks:
    for key in keys:
        comb = lock + key
        if all(n <= 5 for n in comb):
            total += 1
        
print(total)