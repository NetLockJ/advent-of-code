from itertools import combinations_with_replacement
from functools import reduce
from operator import add
from collections import defaultdict
import re

labels = ["capacity", "durability", "flavor", "texture", "calories"]


ingredients = defaultdict(list)

input = open("./input.txt").read()

for line in input.split("\n"):
    ing = line.split(": ")

    ingredients[ing[0]] = [int(r) for r in re.findall(r"-?\d+", ing[1])]

scores = []

print(ingredients)

for num, comb in enumerate(combinations_with_replacement(ingredients.keys(), 100)):
    ing_score = []
    for ing in set(comb):
        ing_score.append([comb.count(ing) * ingredients[ing][i] for i in range(0, 5)])
    # print(num, ing_score)
    ing_score = list(reduce(lambda a, b: map(add, a , b), ing_score))
    if(min(ing_score) < 0):
        continue
    else:
        # print(ing_score)
        # This is a little bit of a stupid solution to how I stored the data, but it
        # sure is a short workaround
        if(ing_score.pop() == 500):
            scores.append(reduce(lambda a, b : a * b, ing_score))

print(max(scores)) 