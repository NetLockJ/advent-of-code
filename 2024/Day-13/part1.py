import sympy
import re

input = open("input.txt", "r").read().split("\n\n")
tokens = 0

for machine in input:
    ax, ay, bx, by, px, py = map(int, re.findall("\d+", machine))
    mat = sympy.Matrix([[ax, bx, px], [ay, by, py]])

    rref, _ = mat.rref()
    print(type(rref[0,2]), rref[1,2])

    if(type(rref[0,2]) == sympy.Integer and type(rref[1,2]) == sympy.Integer):
        tokens += 3 * rref[0,2] + rref[1,2]

print(tokens)