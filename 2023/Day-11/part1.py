from itertools import combinations
import re

def get_dist(c):
    return abs(c[0][0] -  c[1][0]) + abs(c[0][1] - c[1][1])

src = open("./input.txt").read().split("\n")
# Rows
i = 0
while i < len(src):
    if re.match("^\.+$", src[i]) != None:
        src.insert(i, "".ljust(len(src[i]), "."))
        i += 1
    i += 1

# Cols
i = 0
while i < len(src[0]):
    chars = ""
    for j in range(0, len(src)):
        chars += src[j][i]
    if re.match("^\.+$", chars) != None:
        for j in range(0, len(src)):
            src[j] = src[j][0:i] + "." + src[j][i:]
        i += 1
    i += 1

for line in src:
    print(line)

galaxies = []

for i in range(0, len(src)):
    for j in range(0, len(src[0])):
        if src[i][j] == "#":
            galaxies.append((i,j))
distance = 0

for combination in combinations(galaxies, 2):
    distance += get_dist(combination)

print(distance)