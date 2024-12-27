src = open("./input.txt", 'r').read()
src = src.replace("\n", "")
src = list(src)

places_dict = {}
# Sx, sy, rx, ry
pos = [0, 0, 0, 0]

places_dict[str.format("{} {}", pos[0], pos[1])] = 1
direction = {"<" : "-1", ">": "+1", "^": "+1", "v": "-1"}
idx = 0

for char in src:
    is_santa = idx % 2 == 0
    if char == '<' or char == '>':
        pos[0 if is_santa else 2] += eval(direction[char])
    else:
        pos[1 if is_santa else 3] += eval(direction[char])

    places_dict[str.format("{} {}", pos[0], pos[1])] = places_dict.get(str.format("{} {}", pos[0], pos[1]), 0) + 1
    places_dict[str.format("{} {}", pos[2], pos[3])] = places_dict.get(str.format("{} {}", pos[2], pos[3]), 0) + 1

    idx += 1
# print(places_dict)
print(len(places_dict))
