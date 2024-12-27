def roll_north(coord : tuple):
    cur_y = coord[0]
    while cur_y > 0 and src[cur_y - 1][coord[1]] != "#" and (cur_y - 1, coord[1]) not in rocks:
        cur_y -= 1
    rocks.append((cur_y, coord[1]))

src = open("input.txt").read().split("\n")

rocks = [(i, j) for i in range(len(src)) for j in range(len(src[0])) if src[i][j] == "O"]

for idx in range(len(rocks)):
    roll_north(rocks.pop(0))

total = 0

for rock in rocks:
    total += len(src) - rock[0]
print(total)