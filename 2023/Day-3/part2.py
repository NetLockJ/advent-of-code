import re

src = open("./input.txt").read().split("\n")
symbols = dict()

for i in range(140):
    for j in range(140):
        if src[i][j] == '*':
            symbols.setdefault((i, j), [])

for r, row in enumerate(src):
    for mch in re.finditer("\d+", row):
        possible = {(r,c) for r in (r - 1, r, r + 1) for c in range(mch.start() - 1, mch.end() + 1)}
        
        for pos in possible & symbols.keys():
            symbols[pos].append(int(mch.group()))

gear_ratio = 0

for nums in symbols.values():
    print(nums)
    if len(nums) == 2:
        gear_ratio += nums[0] * nums[1]

print(gear_ratio)