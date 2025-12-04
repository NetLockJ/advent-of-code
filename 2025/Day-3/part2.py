def reduce_digits(digits):
    ret = 0
    for n, d in enumerate(reversed(digits)):
        ret += pow(10, n) * d
    return ret

file = open("input.txt", "r").read()
total = 0

for line in file.split("\n"):
    digits = []
    line = list(line)
    line = list(map(int, line))

    stack = []
    max_drop = len(line) - 12

    for digit in line:
        while stack and stack[-1] < digit and max_drop > 0:
            stack.pop()
            max_drop -= 1
        stack.append(digit)

    total += reduce_digits(stack[:12])

print(total)