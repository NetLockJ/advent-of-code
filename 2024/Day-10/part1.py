import numpy as np
from collections import deque


def count_trails(i, j):
    queue = deque([(i, j)])
    seen = set()
    trails = 0

    while queue:
        y, x = queue.popleft()
        if (y, x) in seen:
            continue
        seen.add((y, x))
        if input[y][x] == 9:
            trails += 1
        for cy, cx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            dy = y + cy
            dx = x + cx
            if dy in range(0, len(input)) and dx in range(len(input[0])) and input[dy][dx] == input[y][x] + 1:
                queue.append((dy, dx))

    return trails


input = np.array([list(list(map(int, l))) for l in open("./input.txt").read().split("\n")])
print(input)

total = 0

for i in range(len(input)):
    for j in range(len(input[0])):
        if input[i][j] == 0:
            total += count_trails(i, j)
print(total)
