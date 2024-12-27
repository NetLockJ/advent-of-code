import numpy as np

input = open("input.txt", "r").read()
input = input.split("\n")

visited = set()
position = complex(0,0)
heading = complex(-1,0)

for i, line in enumerate(input):
    if line.count("^") != 0:
        position = complex(i, line.index("^"))

while position.real in range(1, len(input) - 1) and position.imag in range(1, len(input[0]) - 1):
    visited.add(position)
    if(input[int(position.real + heading.real)][int(position.imag + heading.imag)] == "#"):
        heading *= -1j
    position += heading

    print(position)
print(len(visited) + 1)