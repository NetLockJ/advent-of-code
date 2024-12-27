import re
import numpy as np

def calc_dist(accel_time, total_time):
    return accel_time * (total_time - accel_time)

src = open("./input.txt").read().split("\n")
times = re.findall("\d+", src[0])
dist = re.findall("\d+", src[1])

print(times, dist)

total_records = [0] * len(times)

for i in range(len(times)):
    t_time = int(times[i])
    t_dist = int(dist[i])
    for possible_time in range(1, t_time - 1):
        d = calc_dist(possible_time, t_time)
        if d > t_dist:
            total_records[i] += 1

print(np.prod(total_records))