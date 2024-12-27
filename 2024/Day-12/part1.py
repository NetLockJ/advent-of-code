import shapely
import numpy as np
from collections import deque

# flood find with map, pass coords to shapely .length x .area

def flood_find(i,j):
    ch = input[i][j]
    queue = deque([(i, j)])

    coords = []

    while queue:
        y, x = queue.popleft()
        if (y, x) in checked:
            continue
        checked.add((y,x))
        if input[y][x] == ch:
            coords.append((y,x))
        for cy, cx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            dy = y + cy
            dx = x + cx
            if dy in range(0, len(input)) and dx in range(len(input[0])) and input[dy][dx] == ch:
                queue.append((dy, dx))
    
    return coords

checked = set()
input = np.array([list(list(l)) for l in open("./input.txt").read().split("\n")])

cost = 0

for i in range(len(input)):
    for j in range(len(input[0])):
        if (i,j) not in checked:
            points = shapely.MultiPoint(flood_find(i,j)).buffer(0.5, join_style="mitre", cap_style="square")
            cost += points.length * points.area

print(cost)