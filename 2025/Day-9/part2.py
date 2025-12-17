from itertools import combinations
import shapely
import re

def area(p1, p2):
    dx = abs(p1[0] - p2[0]) + 1
    dy = abs(p1[1] - p2[1]) + 1

    return dx * dy

def dxdy(p1, p2):
    dx = abs(p1[0] - p2[0])
    dy = abs(p1[1] - p2[1])

    return (dx, dy)


file = open("./input.txt", "r").read()

points = [tuple((map(int, re.findall(r"\d+", line)))) for line in file.split("\n")]

poly = shapely.Polygon(points)

rects = []

for comb in combinations(points, 2):
    min_x = min(comb[0][0], comb[1][0])
    max_x = max(comb[0][0], comb[1][0])
    min_y = min(comb[0][1], comb[1][1])
    max_y = max(comb[0][1], comb[1][1])

    if shapely.box(min_x, min_y, max_x, max_y).within(poly):
        rects.append(area(comb[0], comb[1]))
        print(comb[0], comb[1])


print(max(rects))