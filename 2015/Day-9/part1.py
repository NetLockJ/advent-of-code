# Inspired from https://www.reddit.com/r/adventofcode/comments/3w192e/day_9_solutions/
# Good solution, and wanted to learn how some of it works

from itertools import permutations
import sys

allplaces = set()
connections = dict()
src = open("./input.txt").read().split("\n")[:-1]

for line in src:
    (start, _ , end, _, dist) = line.split()
    allplaces.add(start)
    allplaces.add(end)
    if not connections.get(start):
        connections.setdefault(start, dict())[start] = dict()
    if not connections.get(end):
        connections.setdefault(end, dict())[end] = dict()
    connections[start][end] = int(dist)
    connections[end][start] = int(dist)

min_dist = sys.maxsize

for perm in permutations(allplaces):

    dist = 0
    for i in range(0, len(perm) - 1):
        dist += connections[perm[i]][perm[i + 1]]
    min_dist = min(min_dist, dist)

print(min_dist)