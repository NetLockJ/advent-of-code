import re

src = open("./input.txt", 'r').read()
src = src.split("\n")[:-1]
# ... aba ... 
split = "(?P<letter>[a-z]).(?P=letter)"
# ab ... ab
group = "(?P<letter>[a-z][a-z]).*?(?P=letter)"

count = 0

def is_nice(line):
	return re.search(split, line) is not None and re.search(group, line) is not None

for line in src:
	if is_nice(line):
		count += 1

print(count)
