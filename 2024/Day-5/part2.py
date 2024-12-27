# Huge re-write because I was doing something that caused bad behaviour (non-determinism), probably with hashing, but I couldn't figure it out
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

total = 0

def is_correctly_ordered(update):
    pages = update.split(",")
    for key, pages_set in order.items():
        if key in pages:
            key_index = pages.index(key)
            for page in pages_set:
                if page in pages:
                    if pages.index(page) < key_index:
                        return False
    return True

def reorder(update):
    pages = update.split(",")
    priority = {page: 0 for page in pages}

    for key, pages_set in order.items():
        for page in pages_set:
            if page in priority and key in priority:
                priority[page] += 1

    #Most last
    pages.sort(key=lambda x: priority[x], reverse=True)
    return ",".join(pages)


for update in updates:
    if not is_correctly_ordered(update):
        fixed_update = reorder(update)
        nums = list(map(int, re.findall("\d+", fixed_update)))
        middle_num = nums[int(len(nums) / 2)]
        total += middle_num

print(total)