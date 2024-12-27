input = open("input.txt", "r").read()

input = input.split("\n")
print(input)

safe = 0
for line in input:
    line = list(map(int, line.split(" ")))
    rev = list(sorted(line))
    rev.reverse()
    if (list(sorted(line)) == line or rev == line) and list(map(lambda x, y: abs(y - x) <= 3 and abs(y - x) >= 1 , line[0:], line[1:])).count(False) == 0:
        safe += 1
print(safe)

