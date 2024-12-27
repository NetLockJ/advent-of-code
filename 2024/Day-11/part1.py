# Little sad, had to upgrade to latest python for this one, but cache works really nice
from functools import cache

input = open("input.txt", "r").read()

stones = list(map(int, input.split(" ")))

print(stones)

@cache
def blink(stone, blinks):
    if blinks == 0: 
        return 1
    if stone == 0:
        return blink(1, blinks - 1)
    elif len(s := str(stone)) % 2 == 0: 
        print(s, s[0:len(s) // 2], s[len(s) // 2:])
        return blink(int(s[0:len(s) // 2]), blinks - 1) + blink(int(s[len(s) // 2:]), blinks - 1)
    else: 
        return blink(stone * 2024, blinks - 1)

print(sum(blink(stone, 25) for stone in stones))