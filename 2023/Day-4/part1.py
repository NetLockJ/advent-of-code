import re

src = open("./input.txt").read().split("\n")[:-1]
cards = dict()
card_num = 1

for line in src:
    cards.setdefault(card_num, [[], []])
    line = line.split(": ")[1:2]
    line = ''.join(line).split(" | ")
    cards[card_num][0] = re.findall("\d+", line[0])
    cards[card_num][1] = re.findall("\d+", line[1])
    card_num += 1

total = []

for key in cards.keys():
    arrs = cards[key]
    matches = 0
    for num in arrs[0]:
        if num in arrs[1]:
            matches += 1
    if matches != 0:
        total.append(2 ** (matches - 1))
print(sum(total))