import re

total = 0
do = open("input.txt", "r").read().split("do()")
for rest in do:
    rest = rest.split("don't()")[0]
    mults = re.findall("mul\\(\d+,\d+\\)", rest)
    for mult in mults:
        nums = re.findall("\d+", mult)
        total += int(nums[0]) * int(nums[1])
print(total)

#TODO: find out why regex isn't working
# input = open("input.txt", "r").read()
# input = input.split("\n")
# total = 0

# for line in map(lambda i: "do()" + i +"don't()", input):
#     matches = re.findall(r"do\(\).*?mul\(\d+,\d+\).*?don't\(\)", line)
#     for line in matches:
#         mults = re.findall("mul\\(\d+,\d+\\)", line)
#         print(line, mults)
#         print()
#         for mult in mults:
#             nums = re.findall("\d+", mult)
#             total += int(nums[0]) * int(nums[1])
# print(total)