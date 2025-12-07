from functools import reduce
import operator
import re

sym = {"*": operator.mul,
       "/": operator.floordiv,
       "+": operator.add,
       "-": operator.sub}

file = open("./input.txt", "r").read()

problems = len(re.findall(r"\d+", file.split("\n")[0]))
symbols = []
nums = []
results = []

for n, line in enumerate(file.split("\n")):
    if re.findall(r"\*|\+|\-|\/", line):
        symbols = re.findall(r"\*|\+|\-|\/", line)
    else:
        for n in map(int, re.findall(r"\d+", line)):
            nums.append(n)
        

# print(nums, symbols, problems)
for i in range(0, problems):
    results.append(reduce(sym[symbols[i]], nums[i::problems]))

print(sum(results))