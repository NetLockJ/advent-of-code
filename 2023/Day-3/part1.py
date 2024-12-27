import re

src = open("./input.txt").read().split("\n")
symbols = dict()

for i in range(140):
    for j in range(140):
        if src[i][j] not in "0123456789.":
            symbols.setdefault((i, j), [])

for r, row in enumerate(src):
    for mch in re.finditer("\d+", row):
        possible = {(r,c) for r in (r - 1, r, r + 1) for c in range(mch.start() - 1, mch.end() + 1)}
        
        for pos in possible & symbols.keys():
            symbols[pos].append(int(mch.group()))

print(sum(sum(val) for val in symbols.values()))