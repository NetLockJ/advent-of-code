import numpy as np

def mirror(array):
    for test_line in range(1, len(array)):
        i = 0
        reflects = True
        while test_line - i > 0 and test_line + i < len(array):
            if int(''.join(array[test_line - i - 1])) ^ int(''.join(array[test_line + i])) != 0:
                reflects = False
            i += 1
        
        if reflects:
            return test_line
        

src = open("./input.txt").read().replace(".", "0").replace("#", "1").split("\n\n")
total = 0

for grid in src:
    grid = grid.split("\n")
    grid = np.array([list(c) for c in grid])

    # Mirror, check, if doesn't succeed, rotate by 90 and check again

    m = mirror(grid)
    if m is not None:
        total += m * 100

    grid = np.rot90(grid, 3)
    m = mirror(grid)
    
    if m is not None:
        total += m

print(total)