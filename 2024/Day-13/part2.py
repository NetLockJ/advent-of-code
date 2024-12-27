#switch to np for int64
from numpy.linalg import solve
import numpy as np
import re

input = open("input.txt", "r").read().split("\n\n")
tokens = 0

for machine in input:
    x,y,p = map(np.int64, re.findall("(\d+)\D*(\d+)", machine))

    p = np.int64(p) + 10000000000000
    
    rref = np.column_stack((x, y))
    sol = np.rint(solve(rref, p))
    print(sol, sol[0], sol[1])

    if np.all(rref @ sol == p):
        tokens += 3 * sol[0] + sol[1]
         
print(tokens)