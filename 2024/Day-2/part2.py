input = open("input.txt", "r").read()

input = input.split("\n")
print(input)

safe = 0
for line in input:
    line = list(map(int, line.split(" ")))
    for i in range(0, len(line)):
        linecp = line.copy()
        linecp.pop(i)
        rev = list(sorted(linecp))
        rev.reverse()
        if (list(sorted(linecp)) == linecp or rev == linecp) and list(map(lambda x, y: abs(y - x) <= 3 and abs(y - x) >= 1 , linecp[0:], linecp[1:])).count(False) == 0:
            safe += 1
            break
    
print(safe)