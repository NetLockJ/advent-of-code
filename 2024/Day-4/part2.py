input = open("input.txt", "r").read()

input = input.split("\n")
total = 0
def find(i,j, dir):
    if not list(map(lambda js: js in range(0, len(input[0])), (j - dir[1], j + dir[1],j))).count(True) == 3 and not list(map(lambda ii: ii in range(0, len(input)), (i - dir[0], i + dir[0], i))).count(True) == 3:
        return False
    str = input[i + dir[0]][j + dir[1]] + input[i][j] + input[i - dir[0]][j - dir[1]]
    str2  = input[i - dir[0]][j + dir[1]] + input[i][j] + input[i + dir[0]][j - dir[1]]
    i += dir[0]
    j += dir[1]
    print(i,j, dir, str, str2, (str == "MAS" or str == "SAM") and (str2 == "MAS" or str2 == "SAM"))
    return (str == "MAS" or str == "SAM") and (str2 == "MAS" or str2 == "SAM")

for i in range(0, len(input) - 1):
    for j in range(0, len(input[0]) - 1):
        if(input[i][j] == "A"):
            for d in [(-1,-1), (1,1)]:
                print(i, j, d)
                if find(i, j, d):
                    total += 1
                    break              
print(total)