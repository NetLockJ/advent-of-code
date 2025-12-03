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

input = open("./input.txt").read()

for line in input.split("\n"):
    gifts = re.findall(r"[a-z]+:\s\d+", line)
    sues.append([(gift.split(": ")[0], int(gift.split(": ")[1])) for gift in gifts])
print(sues)


for num, sue in enumerate(sues):
    print(sue)
    if(all(real_sue[atr[0]] == atr[1] for atr in sue)):
        print(num + 1)
        break