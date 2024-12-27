import re
from tqdm import tqdm


def springs_to_nums(springs):
    return list(map(lambda s: 0 if s == "." else 1 if s == "#" else 2, list(springs)))

def is_possible(test_str, nums_arr):
    str_lens = list(map(lambda s: len(s), re.findall("#+", test_str)))
    return str_lens == nums_arr

src = open("./input.txt").read()

lines = [[line.split(" ")[0], re.findall("\d+", line)] for line in src.split("\n")]

total = 0
for string, nums in tqdm(lines):
    nums = list(map(int, nums))
    for b in range(2 ** string.count("?")):
        test_str = string
        binary = bin(b)[2:].rjust(string.count("?"), "0")
        for i in range(len(binary)):
            test_str = test_str.replace("?", binary[i], 1)
        test_str = test_str.replace("1", "#")
        # print(test_str, nums, is_possible(test_str, nums))
        if is_possible(test_str, nums):
            total += 1

print(total)