import re
from math import prod

file = open("./input.txt", "r").read()

problems = len(re.findall(r"\d+", file.split("\n")[0]))

nums = file.split("\n")
symbols = nums.pop()

total = []

col_nums = []

for col in reversed(range(len(symbols))):
    col_num = ""
    for row in nums:
        col_num += "" if row[col] == " " else row[col]
    
    print(col_num)

    if col_num == "":
        col_nums = []
        continue

    col_nums.append(int(col_num))

    if symbols[col] == " ":
        pass

    if symbols[col] == "+":
        total.append(sum(col_nums))

    if symbols[col] == "*":
        total.append(prod(col_nums))

print(sum(total))