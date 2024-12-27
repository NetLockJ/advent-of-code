from itertools import zip_longest
from collections import deque

def find_free(allocated, block):
    for id, pair in enumerate(allocated):
        _, free = pair
        if free.count(-1) >= block:
            return id
    return None

def add_to_fs(id, length):
    fs.extend(id for _ in range(length))


inp = open("input.txt", "r").read()

# print(sum(list(map(int, input))))

allocated = []
fs = deque()

for file, space in zip_longest(inp[::2], inp[1::2]):
    allocated.append((int(file), [0] if space is None else [-1] * int(space)))

allocated_copy = allocated.copy()

for id, pair in reversed(list(enumerate(allocated))):
    to_move, free = pair
    space = find_free(allocated_copy, to_move)

    if space != None and space < id:
        for i in range(allocated[space][1].index(-1), allocated[space][1].index(-1) + to_move):
            allocated_copy[space][1][i] = id
        allocated_copy[id] = ((-1, allocated_copy[id][0]), allocated_copy[id][1])

for id, pair in enumerate(allocated_copy):
        stored, free = pair
        if stored is not None:
            if type(stored) is tuple:
                add_to_fs(stored[0], stored[1])
            else:
                add_to_fs(id, stored)
        fs.extend(free)

fs.pop()

total = 0
for i, id in enumerate(fs):
    if(id != -1):
        total += i * id

# print(allocated_copy)
print(fs)
print(total)