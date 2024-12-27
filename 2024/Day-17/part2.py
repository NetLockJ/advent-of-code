# This one was diffucult, looked at what the program was doing internally (the puzzle input) and found
# like others that the octal representation of A was important, from there did a brute force from a value
# this will not work for your puzzle input, you will have to go back and start from 0, find the least sig values
# for A, and find where they converge, then plug this new value in to start from.

import re
import math

input = open("input.txt", "r").read()
input = list(map(int, re.findall("\d+", input)))

ra, rb, rc = input[:3]
instructions = input[3:]

print(instructions)


def exe(ra):
    # had to move inside so that global ra wouldn't be refrenced here
    def combo(num):
        if num in [0,1,2,3]:
            return num
        return {4: ra, 5: rb, 6: rc}[num]
    
    ra = ra
    rb = 0
    rc = 0
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
                if output[len(output)-1] != instructions[len(output)-1]:
                    return output
            elif ins == 6:
                rb = ra // 2**comb
            elif ins == 7:
                rc = ra // 2**comb
            ptr += 2
            
        except:
            return output
    return output

start = 0
best = 0

while True:
    start += 1
    # Values that I obtained from brute force, start at zero, find the last digits converging, and start with this new offset
    # ra = start
    # ra = (start * 8 ** 5) + 0o74665
    ra = (start * 8 ** 11) + 0o17064474665
    output = exe(ra)
    if output == instructions:
        print(ra)
        break
    elif len(output) > best:
        print(ra, oct(ra), best)
        best = len(output)
