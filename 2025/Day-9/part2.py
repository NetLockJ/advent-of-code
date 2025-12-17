from itertools import combinations
import shapely
import re

def area(p1, p2):
    dx = abs(p1[0] - p2[0]) + 1
    dy = abs(p1[1] - p2[1]) + 1

    return dx * dy

def is_corner(pt):
    i = points.index(pt)
    
    p = points[i - 1]
    n = points[(i + 1) % len(points)]

    if (p[0] == pt[0] and n[1] == pt[1]) or (p[1] == pt[1] and n[0] == pt[0]):
        return True
    return False


file = open("./input.txt", "r").read()

points = [tuple((map(int, re.findall(r"\d+", line)))) for line in file.split("\n")]

rects = []

for comb in combinations(points, 2):
    if is_corner(comb[0]) and is_corner(comb[1]):
        rects.append(area(comb[0], comb[1]))

print(max(rects))

print(is_corner((7, 1)))
