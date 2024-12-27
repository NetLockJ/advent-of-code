import re
from math import gcd
from functools import reduce

def solve(start):
    instruction_idx = 0
    steps = 0

    while start[2] != "Z":
        value = desert_map[start]
        start = value[0]
        if(instructions[instruction_idx] == 'R'):
            start = value[1]

        instruction_idx = (instruction_idx + 1) % len(instructions)
        steps += 1
    
    return steps

def lcm(arr):
    return reduce(lambda a,b: a*b // gcd(a,b), arr)

src = open("./input.txt").read().split("\n")
instructions = src[0]
desert_map = {idx.split(" = ")[0]: (idx.split(" = ")[1][1:4], idx.split(" = ")[1][6:9]) for idx in src[2:]}

all_spots = []

for spot in desert_map.keys():
    if re.match("..A", spot) != None:
        all_spots.append(spot)

print(all_spots)

cycles = [solve(i) for i in all_spots]
print(lcm(cycles))