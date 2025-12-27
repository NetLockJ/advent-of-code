from functools import cache
from math import prod

@cache
def count_paths(s, e):
    if s == e:
        return 1
    if s not in connections:
        return 0
    
    total = 0
    for n in connections[s]:
        total += count_paths(n, e)
    return total

file = open("input.txt", "r").read().split("\n")

connections = dict()

for line in file:
    line = line.split(" ")
    connections.setdefault(line[0][:-1], line[1:])

route = ("svr", "dac", "fft", "out")

if count_paths("fft", "dac") > 0:
    route = ("svr", "fft", "dac", "out")

print(prod(count_paths(s, e) for s, e in list(zip(route, route[1:]))))