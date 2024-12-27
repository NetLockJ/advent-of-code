# Took me a while to figure out why I was too high, Chief Historian's computer *starts* with t
from itertools import combinations

def are_connected(a, b, c):
   # all ab, bc, ac are valid connections
   return len({(a,b), (b,c), (a,c)} & connections) == 3

input = open("input.txt", "r").read().splitlines()

connections = set()
computers = set()

for computer in input:
    ca, cb = computer.split("-")
    connections.add((ca, cb))
    connections.add((cb, ca))

    computers.add(ca)
    computers.add(cb)

t_connections = []

for a,b,c in combinations(computers, 3):
    if are_connected(a,b,c) and "t" in str(a + b + c)[0::2]:
        t_connections.append((a,b,c))
print(len(t_connections))
