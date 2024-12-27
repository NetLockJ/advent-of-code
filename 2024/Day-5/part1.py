from collections import defaultdict
import re

input = open("input.txt", "r").read()

input = input.split("\n\n")
pairs = input[0].split("\n")
updates = input[1].split("\n")
order = defaultdict(set)

for pair in pairs:
    first, last = pair.split("|")
    order[first].add(last)
print(order)

total = 0
for update in updates:
    correct = True
    for key in order.keys():
        if(key in update):
            for page in order[key]:
                if(page in update):
                    if update.find(page) > update.find(key):
                        continue
                    else:
                        correct = False
                        break
    print("Accepted", update)
    if correct:
        nums = re.findall("\d+", update)
        total += int(nums[int(len(nums) / 2)])

print(total)