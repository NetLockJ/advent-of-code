from collections import defaultdict
from itertools import dropwhile

input = open("input.txt", "r").read().split("\n\n")

operators = {"AND": "&", "OR": "|", "XOR" : "^"}

stored = defaultdict()
wires = set()
gates = []

for line in input[0].splitlines():
    line = line.split(": ")
    stored[line[0]] = int(line[1])


for line in input[1].splitlines():
    line = line.split(" ")
    gates.append((line[0], line[1], line[2], line[4]))
    wires.update({line[0], line[2], line[4]})

print(gates)
print(stored)
print(wires)

while len(wires) > len(stored):
    for gate in gates:
        w1, op, w2, dest = gate
        if {w1, w2} < stored.keys():
            stored[dest] = eval(f"{stored[w1]} {operators[op]} {stored[w2]}")
            # print(f"Possible: {w1}, {w2}: {stored[w1]} {op} {stored[w2]} -> {stored[dest]}")

z_wires = reversed(list(dropwhile(lambda z: z[0] != "z" , sorted(wires))))

z = "0b" + "".join([str(stored[wire]) for wire in z_wires])
print(int(z, base=0))