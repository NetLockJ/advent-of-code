from itertools import combinations

input = open("./input.txt").read()
print(input)

input = input.splitlines()
total = 0
least = 0

for i in range(1, len(input) + 1):
    for combination in combinations(input, i):
        if sum(map(int, combination)) == 150:
            least = i
            break
    if least != 0:
        break

for combination in combinations(input, least):
    if sum(map(int, combination)) == 150:
        total += 1
            
print(total)