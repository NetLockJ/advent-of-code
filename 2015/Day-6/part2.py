import numpy as np
import re

src = open("./input.txt", 'r').read().split("\n")[:-1]

def light_command(line):
    pos = re.search("(\d*,\d*)", line).group() + "," + re.search("(\d*,\d*)", line.split("through")[1]).group()
    if line.count("turn on") == 1:
        return "o " + pos
    elif line.count("turn off") == 1:
        return "f " + pos
    else:
        return "t " + pos
    
def change_lights(mode, x1, y1, x2, y2):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if mode == "t":
                lights[i][j] += 2
            if mode == "o":
                lights[i][j] += 1
            if mode == "f":
                lights[i][j] = max(0, lights[i][j] - 1)

src = map(light_command, src)
src = list(src)

lights = np.zeros([1000, 1000], dtype=int)

for command in src:
    nums = command[2:].split(",")
    change_lights(command[:1], int(nums[0]), int(nums[1]), int(nums[2]), int(nums[3]))

print(lights.sum())

