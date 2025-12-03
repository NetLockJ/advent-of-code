file = open("./input.txt", "r").read()

dial = 50
count = 0

for line in file.split("\n"):
    clicks = int(line[1:])
    if line[0:1] == "L":
        dial = (dial + clicks) % 100
    else:
        dial = (dial - clicks) % 100

    if dial == 0:
        count += 1
    
print(count)