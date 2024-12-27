import re

src = open("./input.txt").read()
print(sum(map(int, re.findall("-?\d+", src))))