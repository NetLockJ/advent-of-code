import re
from itertools import product
from functools import reduce

def op(a,b, op):
    if(op.pop() == "*"):
        return int(a) * int(b)
    else:
        return int(a) + int(b)

input = open("input.txt", "r").read()
input = input.split("\n")
passed = 0

for line in input:
    test, nums = line.split(":")
    test = int(test)
    nums = list(map(int, re.findall("\d+", nums)))

    for comb in list(product(["*", "+"], repeat=len(nums) - 1)):
        comb = list(comb)
        if test == reduce(lambda a, b: op(a,b,comb), nums):
            passed += test
            break
        
print(passed)