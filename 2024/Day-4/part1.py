input = open("input.txt", "r").read()

input = input.split("\n")
total = 0
def find(i,j, dir):
    str = ""
    for _ in range(0,4):
        if(i > len(input) - 1 or i < 0 or j > len(input[0]) - 1 or j < 0):
            return False
        str += input[i][j]
        i += dir[0]
        j += dir[1]
    print(i,j, dir, str)
    return str == "XMAS"

for i in range(0, len(input)):
    for j in range(0, len(input[0])):
        if(input[i][j] == "X"):
            total += sum(map(lambda s: 1 if find(i, j, s) == True else 0, (d for d in [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,1), (1,-1), (-1,-1)])))
print(total)