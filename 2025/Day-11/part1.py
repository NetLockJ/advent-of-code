file = open("input.txt", "r").read().split("\n")

connections = dict()
seen = {"out"}
q = ["you"]

for line in file:
    line = line.split(" ")
    connections.setdefault(line[0][:-1], line[1:])

total = 0

while q:
    connection = q.pop()

    if(connection == "out"):
        total += 1
        continue

    if(connection not in seen):
        q.extend([c for c in connections[connection]])

print(total)