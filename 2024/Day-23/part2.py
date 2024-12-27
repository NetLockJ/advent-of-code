# Cool problem, all is my new favorite python built-in

from itertools import combinations

def are_connected(a, b, c):
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

network = [{c} for c in computers]

for lan in network:
    for computer in computers:
        # If all computers are connected, add the new computer
        if all((computer, net) in connections for net in lan):
            lan.add(computer)


longest = max(network, key=len)
longest = sorted(longest)

print(",".join(longest))