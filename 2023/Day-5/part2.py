# Solution takes about 7 mins to run, but I couldn't figure out how to implement it any other way

import re
import tqdm
    
def backtrace(location):
    for key in reversed(almanac.keys()):
            for possible in almanac[key]:
                dest, src, r = map(int, possible)
                if location >= dest and location <= dest + r - 1:
                    location = src + (location - dest)
                    break
    return location


almanac = dict()
locations = []

src = open("./input.txt").read()
seeds = re.findall("\d+", src.split("\n")[0])
seeds = [range(int(seeds[i]), int(seeds[i]) + int(seeds[i + 1]) - 1) for i in range(0, len(seeds) - 1, 2)]
print(seeds)

src = re.split("\n\s*\n", src)[1:]
for line in src:
    line = line.split("\n")
    key = line[0][:-5]
    almanac.setdefault(key, [])
    for part in line[1:]:
        almanac[key].append(re.findall("\d+", part))

for idx in tqdm.tqdm(range(0, 100000000)):
    possible = backtrace(idx)
    if any(possible in r for r in seeds):
        print(idx)
        break
    idx += 1