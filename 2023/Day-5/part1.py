import re

def in_range(arr, in_num):
    dest = int(arr[0])
    source = int(arr[1])
    r = int(arr[2])
    # print(source, r ,  source + r, in_num)
    if int(in_num) >= source and int(in_num) <= source + r - 1:
        return dest + (int(in_num) - source)
    else:
        return None


almanac = dict()
locations = []

src = open("./input.txt").read()
seeds = re.findall("\d+", src.split("\n")[0])
print(seeds)

src = re.split("\n\s*\n", src)[1:]
for line in src:
    line = line.split("\n")
    key = line[0][:-5]
    almanac.setdefault(key, [])
    for part in line[1:]:
        almanac[key].append(re.findall("\d+", part))

for key in almanac.keys():
    new_seeds = []
    for seed in seeds:
        new_seed_num = seed
        for possible in almanac[key]:
            if in_range(possible, seed) is not None:
                new_seed_num = in_range(possible, int(seed))

        new_seeds.append(new_seed_num)
    seeds = new_seeds
print(min(seeds))