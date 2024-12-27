import re

src = open("./input.txt").read().split("\n")[:-1]
cards = dict()
card_num = 1

for line in src:
    cards.setdefault(card_num, [[], [], [0]])
    line = line.split(": ")[1:2]
    line = ''.join(line).split(" | ")
    cards[card_num][0] = re.findall("\d+", line[0])
    cards[card_num][1] = re.findall("\d+", line[1])
    cards[card_num][2] = 1
    card_num += 1

total_cards = len(cards)
cards_nums = sum(list((c[2]) for c in cards.values()))

while cards_nums > 0:
    for key in cards.keys():
        arrs = cards[key]
        if(arrs[2] != 0):
            matches = 0
            for num in arrs[0]:
                if num in arrs[1]:
                    matches += 1
            if matches != 0:
                for i in range(key + 1, key + matches + 1):
                    cards[i][2] += arrs[2] 
                    total_cards += arrs[2]
            cards[key][2] = 0
        print(cards)
    cards_nums = sum(list((c[2]) for c in cards.values()))
print(total_cards)