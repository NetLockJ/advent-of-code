import shapely

src = open("./input.txt").read().split("\n")
x, y = 0, 0

directions = {"R": "x = x + num", "L": "x = x - num", "U": "y = y + num", "D" : "y = y - num"}
coords = [(0,0)]

for line in src:
    line = line.split(" ")
    direction, num, = line[0], int(line[1])
    exec(directions[direction], globals(), locals())
    coords.append((x,y))
print(coords)

# 0.5 buffer to include area + perimeter
print(int(shapely.area(shapely.Polygon(coords).buffer(0.5, join_style="mitre"))))