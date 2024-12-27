import re

src = open("./input.txt", 'r').read()
src = src.split("\n")[:-1]

double = "(.)\\1"
vowels = "((.*[aeiou]){3,})"
naughty = "ab|cd|pq|xy"

count = 0

def is_nice(line):
	return re.search(double, line) is not None and re.search(vowels, line) is not None

for line in src:
	if is_nice(line) and re.search(naughty, line) is None:
		count += 1

print(count)
