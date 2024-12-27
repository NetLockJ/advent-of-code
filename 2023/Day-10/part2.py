def find_connections(coordinate):
    global visited
    checks = pipe_types[pipe_at(coordinate)]
    for check in checks:
        new_coord = tuple(map(lambda a, b: a + b, dir_to_coord[check], coordinate))
        if(new_coord not in visited):
            visited.add(new_coord)
            return new_coord
        if(new_coord == start_coord):
            return start_coord

def pipe_at(coordinate):
    return src[coordinate[0]][coordinate[1]]

def flood(start_pos):
    filled = set()
    queue = [start_pos]
    count = 0

    while len(queue) > 0:
        new_pos = queue.pop(0)

        y = new_pos[0]
        x = new_pos[1]

        src[y][x] = "#" if src[y][x] == "." else src[y][x]
        

        if x > 1 and pipe_at((y, x - 1)) == "." and (y, x - 1) not in filled:
            queue.append((y, x - 1))
            src[y][x - 1] = "#"
            filled.add((y, x - 1))

        if y > 1 and pipe_at((y - 1, x)) == "." and (y - 1, x) not in filled:
            queue.append((y - 1, x))
            src[y - 1][x] = "#"
            filled.add((y - 1, x))

        if x < len(src[0]) - 1 and pipe_at((y, x + 1)) == "." and (y, x + 1) not in filled:
            queue.append((y, x + 1))
            src[y][x + 1] = "#"
            filled.add((y, x + 1))

        if y < len(src) - 1 and pipe_at((y + 1, x)) == "." and (y + 1, x) not in filled:
            queue.append((y + 1, x))
            src[y + 1][x] = "#"
            filled.add((y + 1, x))

        count += 1
    return count

pipe_types = {
    "|" : ['N', 'S'],
    "-" : ['E', 'W'],
    "L" : ['N', 'E'],
    "J" : ['N', 'W'],
    "7" : ['S', 'W'],
    "F" : ['S', 'E'],
    # Input is the same as having S as a L, you may have to change for your input
    "S" : ['N', 'E']
}

# Account for all north connecting pipes, and S if it should be north facing in input
north_pipes = "L|J" if "N" not in  pipe_types["S"] else "SL|J"

dir_to_coord = {
    "N" : (-1,0),
    "S" : (1, 0),
    "E" : (0, 1),
    "W" : (0, -1)
}

src = open("./input.txt").read().split("\n")

start_coord = ()
visited = set()

for i in range(len(src)):
    for j in range(len(src[0])):
        if src[i][j] == "S":
            start_coord = (i, j)

visited.add(start_coord)
current_coord = find_connections(start_coord)

while current_coord != start_coord:
    current_coord = find_connections(current_coord)

src = list(list(s) for s in src)

for i in range(len(src)):
    for j in range(len(src[0])):
        if (i, j) not in visited:
            src[i][j] = "."

for i in range(len(src[0])):
    flood((0, i))
    flood((len(src) - 1, i))

for i in range(len(src)):
    flood((i, 0))
    flood((i, len(src[0]) - 1))

# Other inside parity checks
for line_idx, line in enumerate(src):
    line = "".join(line)
    if line.count(".") != 0:
        for idx in [i for i, ltr in enumerate(line) if ltr == "."]:
            left = sum([line[:idx].count(c) for c in north_pipes])
            right = sum([line[idx:len(line)].count(c) for c in north_pipes])
            if left % 2 == 0 and right % 2 == 0:
                src[line_idx][idx] = "#"

for line in src:
    print("".join(line))

inside = 0

for line in src:
    inside += "".join(line).count(".")

print(inside)