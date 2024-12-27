# Original Solution
from collections import deque

file = open("input.txt", "r").read()

file = file.split("\n")
left = deque()
right = deque()

for line in file:
    line = line.split("   ")
    left.append(int(line[0]))
    right.append(int(line[1]))

left = sorted(left)
right = sorted(right)

total = 0
while left:
    total += abs(left.pop() - right.pop())

print(total)

# One line rewrite
print(sum(map(lambda r,l: abs(r - l), sorted((input := [*map(int, open("input.txt", "r").read().split())])[0::2]), sorted(input[1::2]))))