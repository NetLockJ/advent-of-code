import re
from itertools import accumulate

def differences(line):
    arr = [list(map(int, re.findall("-?\d+", line)))]
    print(arr)
    idx = 0
    while arr[idx].count(0) != len(arr[idx]):
        arr.append([arr[idx][i + 1] - arr[idx][i] for i in range(0, len(arr[idx]) - 1)])
        idx += 1
    return arr

def history(vals):
    last_res = 0
    for i in range(len(vals) - 1, 0, -1):
        last_res = vals[i - 1][0] - vals[i][0]
        vals[i - 1].insert(0, last_res)
    return last_res

src = open("./input.txt").read().split("\n")
new_history = [history(differences(line)) for line in src]
print(sum(new_history))
