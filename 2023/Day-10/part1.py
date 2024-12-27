# Look up the connections, and only go to those places, don't observe if they connect or not until after
#  has to have the direction that you are looking for 

#    n          n
#  s   [e---w]
#    w
#

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

def add(c1, c2):
    return (c1[0] + c2)

pipe_types = {
    "|" : ['N', 'S'],
    "-" : ['E', 'W'],
    "L" : ['N', 'E'],
    "J" : ['N', 'W'],
    "7" : ['S', 'W'],
    "F" : ['S', 'E'],
    # Input is the same as having S as an F
    "S" : ['E', 'E']
}

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

print(len(visited) // 2)