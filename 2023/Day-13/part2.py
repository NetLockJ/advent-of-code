import numpy as np

def mirror(array):
    for test_line in range(1, len(array)):
        i = 0
        off_count = set()
        while test_line - i > 0 and test_line + i < len(array):
            off_count.add(bin(int(''.join(array[test_line - i - 1]), 2) ^ int((''.join(array[test_line + i])), 2)))
            # print(array[test_line - i - 1], array[test_line + i])
            i += 1
        # print(off_count)

        smudge_line = True

        # Check all values are "legal" 0 or some power of 2
        for val in off_count:
            val = int(val, 2)
            if not (val == 0 or ((val != 0) and ((val & (val - 1)) == 0))):
                smudge_line = False
        
        # Probably the worst looking line of code I've ever written, sorry
        # Check "legal" and len 2 or 1 and if one, it must be a power of 2
        if smudge_line and (len(off_count) == 2 or (len(off_count) == 1 and ((int(list(off_count)[0], 2) != 0) and ((int(list(off_count)[0], 2) & (int(list(off_count)[0], 2) - 1)) == 0)))):
            return test_line
        
    return None
        

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