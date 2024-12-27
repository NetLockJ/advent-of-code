def into_num(in_str):
    this_total = 0
    for char in in_str:
        this_total += ord(char)
        this_total = (this_total * 17) % 256
    return this_total

src = open("./input.txt").read().split(",")

# {num : {lens name, focal len)}}
boxes = {i : dict() for i in range(0, 256)}

for instruction in src:
    box_num = into_num(instruction.strip("-").split("=")[0])

    if '-' in instruction:
        lens = instruction[:-1]
        boxes[into_num(lens)].pop(lens, None)
    else:
        lens, focal_len = instruction.split('=')
        boxes[into_num(lens)][lens] = int(focal_len)

total = 0

# box_num + 1 * lens position + 1 * focal length

for box in boxes:
    for lens_pos, focal_len in enumerate(boxes[box].values()):
        total += (box + 1) * (lens_pos + 1) * focal_len

print(total)
