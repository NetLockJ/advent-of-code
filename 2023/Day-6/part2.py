import re
import tqdm

def calc_dist(accel_time, total_time):
    return accel_time * (total_time - accel_time)

src = open("./input.txt").read().split("\n")
times = int(''.join(re.findall("\d+", src[0])))
dist = int(''.join(re.findall("\d+", src[1])))

print(times, dist)

total_records = 0

for possible_time in tqdm.tqdm(range(1, times - 1)):
    d = calc_dist(possible_time, times)
    if d > dist:
        total_records += 1

print(total_records)