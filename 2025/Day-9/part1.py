from itertools import combinations
import re

def area(p1, p2):
    dx = abs(p1[0] - p2[0]) + 1
    dy = abs(p1[1] - p2[1]) + 1

    return dx * dy

file = open("./input.txt", "r").read()

points = [tuple((map(int, re.findall(r"\d+", line)))) for line in file.split("\n")] 

rects = []

for comb in combinations(points, 2):
    rects.append(area(comb[0], comb[1]))

print(max(rects))