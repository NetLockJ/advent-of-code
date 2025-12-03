# Rockwell reteroencabulator mentioned, nice!
import re

sues = []

real_sue = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}

exact = {
    "children": 3,
    "samoyeds": 2,
    "akitas": 0,
    "vizslas": 0,
    "cars": 2,
    "perfumes": 1
}

input = open("./input.txt").read()

for line in input.split("\n"):
    gifts = re.findall(r"([a-z]+): (\d+)", line)
    sues.append({key: int(value) for key, value in gifts})
print(sues)


for num, sue in enumerate(sues):
    is_real = True
    for prop, val in sue.items():
        if prop in ["cats", "trees"]:
            if val <= real_sue[prop]:
                is_real = False
                break
        elif prop in ["pomeranians", "goldfish"]:
            if val >= real_sue[prop]:
                is_real = False
                break
        else:
            if val != real_sue[prop]:
                is_real = False
                break
    if is_real:
        print(num + 1)
        break