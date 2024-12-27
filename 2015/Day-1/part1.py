src = list(open("./input.txt", "r").read())
moves = map(lambda c: 1 if c == "(" else -1, src)
print(sum(moves))
