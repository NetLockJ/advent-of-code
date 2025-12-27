import re

file = open("input.txt", "r").read().split("\n\n")

shapes = [0] * 6

for i in range(0, 6):
    for line in file[i]:
        shapes[i] += line.count("#")
    
total = 0

for line in file[6].split("\n"):
    nums = list(map(int, re.findall(r"\d+", line)))
    dy, dx = nums[0], nums[1]

    shape_area = list(zip(shapes, nums[2:]))
    packed_shapes = sum((n * a for n, a in shape_area))

    if(packed_shapes < dy * dx):
        total += 1

print(total)