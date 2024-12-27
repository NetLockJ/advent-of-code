# Doesn't work yet

import numpy as np
import tqdm

def dir_char(heading):
    return "|" if heading in (complex(1,0), complex(-1,0)) else "-"

def is_loop(i, j, position, heading, input):
    if input[i][j] in "#^":
        return False
    
    guard_path = input.copy()
    guard_path[i][j] = "#"
    visited = set()

    # print(input)
    while (position.real in range(1, len(input) - 1) and position.imag in range(1, len(input[0]) - 1)):
        if tuple([position, heading]) in visited:
            # print(guard_path, "\n")
            return True
        visited.add((position, heading))
        if(guard_path[int(position.real + heading.real)][int(position.imag + heading.imag)] == "#"):
            heading *= -1j
        position += heading
        steps += 1
        
    return False

input = [list(list(l)) for l in open("./input.txt").read().split("\n")]
input = np.array(input)

preverved_input = input.copy()

visited = set()
start_point = complex(0,0)
heading = complex(-1,0)

for i in range(0, len(input)):
    for j in range(0, len(input[0])):
        if input[i][j] == "^":
            start_point = complex(i, j)

loop = 0

for i in tqdm.tqdm(range(len(input))):
    for j in range(len(input[0])):
       loop += is_loop(i,j, start_point, heading, input)

print(loop)