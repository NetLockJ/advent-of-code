import re
import math

def combo(num):
    if num in [0,1,2,3]:
        return num
    return {4: ra, 5: rb, 6: rc}[num]

input = open("input.txt", "r").read()
input = list(map(int, re.findall("\d+", input)))

ra, rb, rc = input[:3]
instructions = input[3:]

print(instructions)

ptr = 0
output = []

while ptr < len(instructions):
    try:
        ins, op, comb = instructions[ptr], instructions[ptr + 1], combo(instructions[ptr + 1])

        if ins == 0:
            ra = ra // 2**comb
        elif ins == 1:
            rb = rb ^ op
        elif ins == 2:
            rb = comb % 8
        elif ins == 3:
            if ra != 0:
                ptr = op
                ptr -= 2
        elif ins == 4:
            rb = rb ^ rc
        elif ins == 5:
            output.append(comb % 8)
        elif ins == 6:
            rb = ra // 2**comb
        elif ins == 7:
            rc = ra // 2**comb
        ptr += 2
        
    except:
        break


print(ra, rb, rc)
print((str(output)[1:len(str(output)) - 1]).replace(" ", ""))