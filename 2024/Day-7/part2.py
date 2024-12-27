# Not the best solution, takes about 1.5 minutes to run

import re
from itertools import product
from collections import deque
import tqdm


input = open("input.txt", "r").read()
input = input.split("\n")
passed = 0

for line in tqdm.tqdm(input):
    test, nums = line.split(":")
    test = int(test)
    nums = list(map(int, re.findall("\d+", nums)))
    
    for comb in list(product(["*", "+", "||"], repeat=len(nums) - 1)):
        cb = list(comb)
        d_nums = deque(nums)
        
        while len(d_nums) != 1:
            op = cb.pop(0)
            left = d_nums.popleft()
            right = d_nums.popleft()
            if op == "+":
                d_nums.appendleft(int(left) + int(right))
            elif op == "*":
                d_nums.appendleft(int(left) * int(right))
            elif op == "||": 
                d_nums.appendleft(int(str(left) + str(right)))
            # print(d_nums, comb, op)
        if test == d_nums[0]:
            passed += test
            # print(test, nums, comb)
            break

print(passed)