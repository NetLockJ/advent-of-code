import shapely

src = open("./input.txt").read().split("\n")
x, y = 0, 0

directions = {"0": "x = x + num", "2": "x = x - num", "3": "y = y + num", "1" : "y = y - num"}
coords = [(0,0)]

for line in src:
    line = line.split(" ")
    direction, num = line[2][7:8], int(line[2][2:7], 16)
    exec(directions[direction], globals(), locals())
    coords.append((x,y))
print(coords)

# 0.5 buffer to include area + perimeter
print(int(shapely.area(shapely.Polygon(coords).buffer(0.5, join_style="mitre"))))