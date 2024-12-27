from itertools import combinations
import re

def get_dist(c):
    return abs(c[0][0] -  c[1][0]) + abs(c[0][1] - c[1][1])

src = open("./input.txt").read().split("\n")
not_expanded = src.copy()
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
for line in not_expanded:
    print(line)

galaxies = []
old_galaxies = []

for i in range(0, len(src)):
    for j in range(0, len(src[0])):
        if src[i][j] == "#":
            galaxies.append((i, j))

for i in range(0, len(not_expanded)):
    for j in range(0, len(not_expanded[0])):
        if not_expanded[i][j] == "#":
            old_galaxies.append((i, j))
print(old_galaxies)
print(galaxies)

distance = 0

new_combinations = list(combinations(galaxies, 2))
old_combinations = list(combinations(old_galaxies, 2))


for i in range(0, len(new_combinations)):
    print(new_combinations[i])
    print(old_combinations[i])
    this_dist = get_dist(new_combinations[i]) + ((1000000 - 2) * abs(get_dist(new_combinations[i]) - get_dist(old_combinations[i])))
    distance += this_dist
    print(this_dist)

print(distance)