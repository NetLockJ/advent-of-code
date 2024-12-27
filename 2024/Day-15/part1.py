import numpy as np

# I is Y, J is X, I don't know why I did that

def peek(i, j, dir, l):
    if grid[i + dir[0]][j + dir[1]] == ".":
        return True, l
    elif grid[i + dir[0]][j + dir[1]] == "#":
        return False, l
    else:
        return peek(i + dir[0], j + dir[1], dir, l + 1)

def push(i, j, dir):
    b, l = peek(i, j, dir, 0)
    l += 1
    if b:
        grid[i + dir[0]][j + dir[1]] = "."
        grid[i + l * dir[0]][j + l * dir[1]] = "O"
        return True   
    return False

directions = {"^": (-1, 0), "v": (1, 0), "<":(0,-1), ">": (0,1)}

input = open("input.txt", "r").read().split("\n\n")

grid = np.array([list(list(l)) for l in input[0].split("\n")])
print(grid)
instructions = input[1]

robot = (0,0)

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "@":
            robot = (i, j)

for i, instruction in enumerate(instructions):
    if instruction == "\n":
        continue
    dir = directions[instruction]
    pushed = push(robot[0], robot[1], dir)
    if(pushed):
        grid[robot[0]][robot[1]] = "."
        robot = (robot[0] + dir[0], robot[1] + dir[1])
        grid[robot[0]][robot[1]] = "@"
    # print(i, instruction, "\n\n",  grid)

gps = 0

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if(grid[i][j] == "O"):
            gps += 100 * i + j

print(grid)
print(gps)