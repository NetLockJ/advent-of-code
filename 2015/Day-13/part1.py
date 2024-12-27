from itertools import permutations
import tqdm

people = set()
happiness = dict()

src = open("./input.txt").read().split("\n")[:-1]

for line in src:
    split_line = line.split(" ")
    people.add(split_line[0])
    happiness.setdefault(split_line[0], dict())[split_line[10][:-1]] = int(split_line[3]) * (-1 if split_line[2] == "lose" else 1)

best_happiness = 0

for permutation in tqdm.tqdm(permutations(people)):
    
    permutation = list(permutation)
    permutation.append(permutation[0])
    permutation.insert(0, permutation[len(permutation) - 2])

    perm_happiness = 0
    for i in range(1, len(permutation) - 1):
        perm_happiness += happiness[permutation[i]][permutation[i - 1]] + happiness[permutation[i]][permutation[i + 1]]
        print(permutation)
        print(happiness[permutation[i]][permutation[i + 1]])

    best_happiness = max(best_happiness, perm_happiness)

print(best_happiness)