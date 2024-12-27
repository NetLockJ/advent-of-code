src = open("./input.txt", 'r').read()
src = src.replace("\n", "")
src = list(src)
print(src)

places_dict = {}

x = 0
y = 0


places_dict[str.format("{} {}", x, y)] = 1

direction = {
    "<" : "x-1",
    ">": "x+1",
    "^": "y+1",
    "v": "y-1"
}

for char in src:
    if char == '<' or char == '>':
        x = eval(direction[char])
    else:
        y = eval(direction[char])

    places_dict[str.format("{} {}", x, y)] = places_dict.get(str.format("{} {}", x, y), 0) + 1
print(places_dict)
print(len(places_dict))
