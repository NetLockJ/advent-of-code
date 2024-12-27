import re

src = open("./input.txt").read()
str_len = len(src.replace("\n", ""))
src = src.split("\n")[:-1]
enc_len = 0

for line in src:
    # Outside "" + line chars + counts of special charecters
    enc_len += len(line) + line.count("\\") + line.count('"') + 2

print(enc_len, str_len, enc_len - str_len)