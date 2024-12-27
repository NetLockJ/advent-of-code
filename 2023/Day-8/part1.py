src = open("./input.txt").read().split("\n")
instructions = src[0]
desert_map = {idx.split(" = ")[0]: (idx.split(" = ")[1][1:4], idx.split(" = ")[1][6:9]) for idx in src[2:]}
current_spot = "AAA"
instruction_idx = 0
steps = 0

while current_spot != "ZZZ":
    value = desert_map[current_spot]
    current_spot = value[0]
    if(instructions[instruction_idx] == 'R'):
        current_spot = value[1]

    instruction_idx = (instruction_idx + 1) % len(instructions)
    steps += 1

print(steps)