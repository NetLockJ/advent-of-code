from heapq import heappop, heappush
import numpy as np
from collections import defaultdict

def find_path(q):

    while q:
        cost, y, x, dist_in_dir, dir = heappop(q)

        if y == len(src) - 1 and x == len(src[0]) - 1:
            return cost

        if (y,x) in seen:
            continue

        if y < 0 or y > len(src) - 1 or x < 0 or x > len(src[0]) - 1:
            continue

        traveled_grid[y][x] = "0"

        for possible in [c for c in "NSEW" if c not in opposites[dir]]:
            if (new := add((y, x), directions[possible])) not in seen:
                if new[0] < 0 or new[0] > len(src) - 1 or new[1] < 0 or new[1] > len(src[0]) - 1 or dist_in_dir > 3:
                    continue
                heappush(q, (cost + src[new[0]][new[1]], new[0], new[1], (dist_in_dir + 1 if dir == possible else 1), possible))
        seen.add((y, x))

def add(t1, t2):
    return tuple(map(lambda a, b: a + b, t1, t2))

src = [list(map(int, list(l))) for l in open("./input.txt").read().split("\n")]
src = np.array(src)

seen = set()
seen.add((0,0))
q = []

directions = {"N" : (-1,0), "S" : (1,0), "E" : (0,1), "W" : (0,-1)}
opposites = {"N" : "S", "S" : "N", "E": "W", "W" : "E"}

# cost, pos, dis_in_dir, dir, last
heappush(q, (src[1][0], 1, 0, 1, "S"))
heappush(q, (src[0][1], 0, 1, 1, "E"))



print(src)
traveled_grid = src.copy()

cost = find_path(q)
print(cost)