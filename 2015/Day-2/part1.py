src = open("./input.txt", "r").read()
lines = src.split("\n")[:-1]
area = 0
for line in lines:
    vals = line.split("x")

    s1 = int(vals[0])
    s2 = int(vals[1])
    s3 = int(vals[2])

    a = s1 * s2
    b = s1 * s3
    c = s2 * s3

    area += 2 * a + 2 * b + 2 * c + min(a, b , c)

print(area)
    