rank_str = "23456789TJQKA"

hands = {
    "high": [],
    "pair": [],
    "twopair": [],
    "three": [],
    "full": [],
    "four": [],
    "five": [],
}


def strength(hand):
    ret = '1'
    for c in hand[0]:
        ret += str(rank_str.index(c)).rjust(2, '0')
    return int(ret)


def hand_type(hand):
    cards = {c: hand.count(c) for c in set(hand)}

    if 5 in cards.values():
        return "five"

    if 4 in cards.values():
        return "four"

    if 3 in cards.values() and 2 in cards.values():
        return "full"

    if 3 in cards.values():
        return "three"

    if len(cards) == 3:
        return "twopair"

    if 2 in cards.values():
        return "pair"

    if len(cards.values()) == 5:
        return "high"


src = open("./input.txt").read().split("\n")
for line in src:
    line = line.split(" ")
    hands[hand_type(line[0])].append((line[0], line[1]))

for h_type in hands.keys():
    arr = hands[h_type]
    arr.sort(key=strength)
    hands[h_type] = arr


mult = 1
total = 0
for h_type in hands.values():
    for num in h_type:
        total += int(num[1]) * mult
        mult += 1
print(total)