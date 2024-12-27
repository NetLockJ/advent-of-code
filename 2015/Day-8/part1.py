import re

src = open("./input.txt").read()
str_len = len(src.replace("\n", ""))
src = src.split("\n")[:-1]
mem_len = 0

for line in src:
    mem_len += len(re.sub(r"\\x..|\\.", "*", line)) - 2

print(str_len, mem_len, str_len - mem_len)