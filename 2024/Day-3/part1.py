import re

input = open("input.txt", "r").read()

input = input.split("\n")
total = 0

for line in input:
    mults = (re.findall("mul\\(\d+,\d+\\)", line))
    for mult in mults:
        nums = re.findall("\d+", mult)
        total += int(nums[0]) * int(nums[1])
print(total)