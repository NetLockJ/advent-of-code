from heapq import heappop, heappush
import numpy as np

def dijk(start, q):
    seen = set()
    seen.add((start))

    i = 0

    while q:
        score, _, location = heappop(q)

        if location == end:
            # print(grid)
            return score
        
        # print(location, end)
        
        for dir in [1, -1,  0 + 1j, 0 -1j]:
            new_loc = location + dir


            if int(new_loc.real) in range(len(grid)) and int(new_loc.imag) in range(len(grid[0])):
                if grid[int(new_loc.real)][int(new_loc.imag)] == 1:
                    continue

                if (new_loc) not in seen:
                    heappush(q, (score + 1, i := i + 1, new_loc))
                    seen.add((new_loc))
                    grid[int(new_loc.real)][int(new_loc.imag)] = "9"

grid_size = 70 + 1
fallen = 1024
grid = np.zeros((grid_size,grid_size))

start = complex(0,0)
end = complex(grid_size - 1, grid_size - 1)

input = open("input.txt", "r").read().split("\n")

for byte, line in enumerate(input):
    if byte < fallen:
        x, y = map(int, line.split(","))
        grid[y][x] = "1"

hq = []

heappush(hq, (0, 0, start))
print(dijk(start, hq))
