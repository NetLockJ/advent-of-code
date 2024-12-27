import re
from itertools import combinations

src = open("./input.txt").read().split("\n")

hailstones = []
min_pos = 2e14
max_pos = 4e14

for line in src:
    hailstones.append([*map(int, re.findall("-?\d+", line))])

print(hailstones)

cross = 0

for comb in combinations(hailstones, 2):
    # px py pz @ vx vy vz
    h1 = comb[0]
    h2 = comb[1]

    h1_dydx = h1[4] / h1[3]
    h2_dydx = h2[4] / h2[3]

    if(h1_dydx == h2_dydx):
        continue


    # Yielded from solving y - y1 = m(x-x1) and setting y | x equal
    x = (h1[1] - h2[1] - (h1[0] * h1_dydx) + (h2[0] * h2_dydx)) / (h2_dydx - h1_dydx)
    y = ((h2_dydx * h1_dydx * h1[0]) - (h2_dydx * h1[1]) + (h1_dydx * h2[1]) - (h2_dydx * h1_dydx * h2[0])) / (h1_dydx - h2_dydx)

    if (min_pos <= x <= max_pos) and (min_pos <= y <= max_pos):
        if ((((h1[3] > 0 and x > h1[0]) or (h1[3] < 0 and x < h1[0])) and ((h2[3] > 0 and x > h2[0]) or (h2[3] < 0 and x < h2[0])))):
            cross += 1
            # print(comb)

print(cross)
