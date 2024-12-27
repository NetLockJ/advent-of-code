from itertools import zip_longest
from collections import deque

def find_free(allocated):
    for id, pair in enumerate(allocated):
        _, free = pair
        if free > 0:
            return id
    return None

def add_to_fs(id, length):
    fs.extend(id for _ in range(length))


inp = open("input.txt", "r").read()

# print(sum(list(map(int, input))))

allocated = []
fs = deque()

for file, space in zip_longest(inp[::2], inp[1::2]):
    allocated.append((int(file), 0 if space is None else int(space)))

print(allocated)

for id, pair in enumerate(allocated):
    stored, free = pair
    add_to_fs(id, stored)
    add_to_fs(-1, free)

while True:
    try:
        if(fs.count(-1) < 1):
            break
        move = fs.pop()
        length = len(fs)
        pos = fs.index(-1)
        fs[pos] = move
        if(pos >= length):
            break
    except: 
        break

    # print(fs)

total = 0

for i, id in enumerate(fs):
    total += i * id

print(fs)
print(total)