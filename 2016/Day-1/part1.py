input = open("input.txt", "r").read()
input = input.split(", ")
start = complex(0)
for dir in input:
    print(dir)
    c, d = dir[0], dir[1:]
    if c == "R":
        start *= complex("-j")
    else:
        start *= complex("j")
    start += int(d)
print(abs(start.real) + abs(start.imag))
