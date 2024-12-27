import re

def all_exist(arr):
    for element in arr:
        if wires.get(element) == None:
            return False
    return True

src = open("./input.txt", 'r').read()

for k,v in {"AND": "&", "OR": "|", "LSHIFT": "<<", "RSHIFT": ">>", "NOT": "65535 -"}.items():
    if src.find(k) != -1:
        src = src.replace(k, v)

src = list(src.split("\n")[:-1])

instructions = []
wires = {}

for line in src:
    instructions.append([line.split(" -> "), False])

print(instructions)

while(len(instructions) != 0):
    for statement in instructions:
        involved_wires = re.findall("[a-z]{1,2}", statement[0][0])

        if(all_exist(involved_wires)):
            # Evaluate expression because we have all necessary information
            for name in involved_wires:
                statement[0][0] = re.sub("(" + name + "{1,2}\s)|" + name + "{1,2}$", str.format("wires[\'{}\'] ", name) , statement[0][0])
            # print(str.format("{} -> {}\n{}", statement[0][0], statement[0][1], wires))
            wires[statement[0][1]] = eval(statement[0][0])
            instructions.remove(statement)

print(wires['a'])