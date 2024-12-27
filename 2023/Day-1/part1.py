import re

src = open("./input.txt").read().split("\n")[:-1]

values = []

for line in src:
    digits = re.findall("\d", line)
    values.append(int(str(digits[0] + digits[len(digits) - 1])))

print(sum(values))
