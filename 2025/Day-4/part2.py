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

grid_locations = []

for i in range(0, len(grid)):
    for j in range(0, len(grid[0])):
        if grid[i][j] == "@":
            grid_locations.append((i, j))

last_grid_locations = []

count = 0
while grid_locations != last_grid_locations:
    last_grid_locations = grid_locations
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] == "@" and count_adj(i, j, grid) < 4:
                grid[i][j] = "X"
                count += 1
    
    grid_locations = []
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] == "@":
                grid_locations.append((i, j))


print(count)