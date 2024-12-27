src = open("./input.txt", "r").read()
lines = src.split("\n")[:-1]
area = 0
for line in lines:
    vals = line.split("x")

    s1 = int(vals[0])
    s2 = int(vals[1])
    s3 = int(vals[2])

    l1 = 2 * s1 + 2 * s2
    l2 = 2 * s1 + 2 * s3
    l3 = 2 * s2 + 2 * s3

    vol = s1 * s2 * s3

    area += min(l1, l2, l3) + vol

print(area)
    