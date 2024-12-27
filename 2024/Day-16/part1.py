# Doesn't work yet... works for examples, but not my input

from heapq import heappush, heappop
import numpy as np

def find(ch):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == ch:
                return complex(i,j)

def dijk(start, q):
    seen = set()
    seen.add((start, complex(0,1)))

    i = 0

    while q:
        score, _, location, direction = heappop(q)

        if location == end:
            print(grid)
            return score
        
        # print(location, end)
        
        for dir in [1, 1j, -1j]: 
            new_loc = location + dir * direction if dir == 1 else location
            new_dir = direction if dir == 1 else dir * direction

            if grid[int(new_loc.real)][int(new_loc.imag)] == "#":
                continue

            if int(new_loc.real) in range(len(grid)) and int(new_loc.imag) in range(len(grid[0])):
                if (new_loc, new_dir) not in seen:
                    heappush(q, (score + (1 if dir == 1 else 1000), i := i + 1, new_loc, new_dir))
                    seen.add((new_loc, new_dir))
                    # grid[int(new_loc.real)][int(new_loc.imag)] = "X"

grid = [list(list(l)) for l in open("./input.txt").read().split("\n")]
grid = np.array(grid)

start = find("S")
end = find("E")

hq = []

# score, loc, dir 
heappush(hq, (0, 0, start, complex(0, 1)))
print(dijk(start, hq))