import numpy as np
import functools


@functools.cache
def count_split(loc):
    i, j = loc
    while i < len(grid):
        if(grid[i][j] == "^"):
            return 1 + count_split((i, j - 1)) + count_split((i, j + 1))
        i += 1
    return 0

file = open("./input.txt", "r").read()
grid = np.array([list(list(l)) for l in file.split("\n")])

print(count_split((1, len(grid[0]) // 2)) + 1)