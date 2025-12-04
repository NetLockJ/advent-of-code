import re

file = open("./input.txt", "r").read()
file = file.split(",")

invalid = []

for pair in file:
    pair = pair.split("-")

    for i in range(int(pair[0]), int(pair[1]) + 1):
        if re.match(r"^([1-9]([0-9])*)\1$", str(i)):
            invalid.append(i)

print(sum(invalid))