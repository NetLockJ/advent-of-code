import re

src = open("./input.txt").read().split("\n\n")
workflows = dict()
parts = []

for w in src[0].split("\n"):
    key = w.split("{")[0]
    # Yeah, sorry
    workflows[key] = {p.split(":")[0].strip("}"): p.split(":")[0].strip("}") if len(p.split(":")) == 1 else p.split(":")[1] for p in w.split("{")[1].split(",")}

for p in src[1].split("\n"):
    parts.append({re.findall("[a-z]", p)[i]: int(re.findall("\d+", p)[i]) for i in range(4)})

print(workflows)
print(parts)

accepted_parts = []

for part in parts:
    current_workflow = "in"
    # this_flow = []

    while current_workflow != "A" and current_workflow != "R":
        for instruction in workflows[current_workflow].keys():
            # We need to see if it evals to true
            if "<" in instruction or ">" in instruction:
                res = eval(instruction, {"x": part['x'], "m": part['m'], "a": part['a'], "s": part['s']})
                if res == True:
                    current_workflow = workflows[current_workflow][instruction]
                    # this_flow.append(current_workflow)
                    break
            else:
                current_workflow = instruction
                # this_flow.append(current_workflow)
                break
    if current_workflow == "A":
        accepted_parts.append(part)

total = 0
for part in accepted_parts:
    for num in part.values():
        total += num
print(total)
