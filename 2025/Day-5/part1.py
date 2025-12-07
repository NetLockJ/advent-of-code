file = open("./input.txt", "r").read()

ranges = file.split("\n\n")[0].split("\n")
ingredients = file.split("\n\n")[1].split("\n")

ranges = [tuple(map(int, line.split("-"))) for line in ranges]

count = 0

print(ranges)
print(ingredients)

for ingredient in ingredients:
    if all(int(ingredient) not in range(s, e + 1) for s, e in ranges):
        count += 1

print(len(ingredients) - count)