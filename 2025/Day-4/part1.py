import numpy as np

def count_adj(i, j, grid):
    ret = 0
    dirs = [
        (-1, -1), (-1, 0), (-1, 1),  
        (0, -1), (0, 1),  
        (1, -1), (1, 0), (1, 1)    
    ]

    for dx, dy in dirs:
        if 0 <= i + dx < len(grid) and 0 <= j + dy < len(grid[0]):
            if(grid[i + dx][j + dy] == "@"):
                ret += 1
    return ret
        

input = open("input.txt", "r").read().split("\n\n")

grid = np.array([list(list(l)) for l in input[0].split("\n")])
print(grid)

grid2 = grid.copy()

count = 0
for i in range(0, len(grid)):
    for j in range(0, len(grid[0])):
        if grid[i][j] == "@" and count_adj(i, j, grid) < 4:
            count += 1
            grid2[i][j] = "X"

print(count)
print(grid2)