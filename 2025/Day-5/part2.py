file = open("./input.txt", "r").read()

ranges = file.split("\n\n")[0].split("\n")
ranges = [tuple(map(int, line.split("-"))) for line in ranges]

print(ranges)
ranges.sort()

map = [ranges[0]]

for s, e in ranges[1:]:
    if map[-1][1] >= s:
        map[-1] = (map[-1][0], max(map[-1][1], e))
    else:
        map.append((s, e))

print(sum(e - s + 1 for s, e in map))
