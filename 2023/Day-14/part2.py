import numpy as np
import tqdm

def roll_north(coord : tuple):
    global rocks
    cur_y = coord[0]
    while cur_y > 0 and src[cur_y - 1][coord[1]] == ".":
        cur_y -= 1
    src[coord[0]][coord[1]] = "."
    src[cur_y][coord[1]] = "O"

def weight():
    total = 0
    for rock in rocks:
        total += len(src) - rock[0]
    return total

src = open("input.txt").read().split("\n")

src = list(list(s) for s in src)

grids = set()
grids_arr = []
weights = []
last_repeat = False

rocks = [(i, j) for i in range(len(src)) for j in range(len(src[0])) if src[i][j] == "O"]
cycle_num = 0
while True:
    cycle_num += 1
    for _ in range(4):
        for idx in range(len(rocks)):
            roll_north(rocks[idx])
        src = np.rot90(src, 3)
        rocks = [(i, j) for i in range(len(src)) for j in range(len(src[0])) if src[i][j] == "O"]
    if(tuple(rocks) in grids):
        break
    grids.add(tuple(rocks))
    grids_arr.append((rocks))
    weights.append(weight())

print(cycle_num)

rocks = grids_arr[(1000000000 - cycle_num) % (cycle_num - grids_arr.index((rocks)) - 1) + grids_arr.index((rocks))]
print(weights)
print(weight())