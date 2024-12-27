src = list(open("./input.txt", "r").read())
moves = map(lambda c: 1 if c == "(" else -1, src)
counter = 0
sum = 0
for i in moves:
    counter += 1
    sum += i
    if sum == -1:
        print(counter)
        break
