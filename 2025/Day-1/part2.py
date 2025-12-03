file = open("./input.txt", "r").read()

dial = 50
count = 0

for line in file.split("\n"):
        
    dir = line[0:1]
    clicks = int(line[1:])
    
    for _ in range(clicks):
        if dir == "L":
            dial -= 1
            if dial < 0:
                dial = 99
        else:
            dial += 1
            if dial > 99:
                dial = 0

        if dial == 0:
            count += 1

print(count)