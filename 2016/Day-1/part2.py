input = open("input.txt", "r").read()
input = input.split(", ")
start = 0 + 0j
direction = 1j
visited = {start}
for dir in input:
    c, d = dir[0], dir[1:]
    if c == "R":
        direction *= -1j
    else:
        direction *= 1j
    for i in range(int(d)):
        start += direction
        print(start)
        if start in visited:
            print(abs(start.real) + abs(start.imag))
            exit()
        visited.add(start)