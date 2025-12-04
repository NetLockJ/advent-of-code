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

    digits.append(max(line))

    if line.index(digits[0]) + 1 == len(line):
        # Need digit before max
        line = line[0: line.index(digits[0])]
        digits.insert(0, max(line))
    else:
        # Can have after max
        line = line[line.index(digits[0]) + 1:]
        digits.append(max(line))

    total += reduce_digits(digits)

print(total)
  

