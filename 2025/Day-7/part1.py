import numpy as np
from collections import deque

def process_beam(loc):
    global total
    new_loc = []
    i, j = loc

    try:
        if(grid[i][j] == "." or grid[i][j] == "S"):
            new_loc.append((i + 1, j))
            grid[i][j] = "|"
        elif grid[i][j] == "^":
            total += 1
            if(grid[i][j - 1] != "|"):
                new_loc.append((i, j - 1))
                grid[i][j] = "|"
            if(grid[i][j + 1] != "|"):
                new_loc.append((i,j + 1))
                grid[i][j] = "|"
    except IndexError:
        pass

    return new_loc
    

file = open("./input.txt", "r").read()
grid = np.array([list(list(l)) for l in file.split("\n")])

d = deque([(1, len(grid[0]) // 2)])
total = 0

while d:
    ds = process_beam(d.popleft())
    for new in ds:
        d.append(new)
    print(grid)

print(total)