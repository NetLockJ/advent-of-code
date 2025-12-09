from itertools import combinations
import math
import re

def min_lin(j):
    return math.dist(j[0], j[1])

def find_connection(p):
    for l, c in connections.items():
        if p in c:
            return l
    return None

MAX = 1000

file = open("./input.txt", "r").read()
points = [tuple((map(int, re.findall(r"\d+", line)))) for line in file.split("\n")] 

junctions = combinations(points, 2)
junctions = sorted(junctions, key=min_lin)

connections = {i: [p] for i, p in enumerate(points)}

count = 0

while count < MAX - 1:
    pa, pb = junctions.pop(0)

    la = find_connection(pa)
    lb = find_connection(pb)

    if la == lb:
        count += 1
        continue

    connections[la].extend(connections[lb])
    del connections[lb]

    count += 1

    print(count)

connections = sorted((len(c) for c in connections.values()))
print(math.prod(connections[-3:]))