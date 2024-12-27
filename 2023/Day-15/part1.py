def into_nums(in_str):
    this_total = 0
    for char in in_str:
        this_total += ord(char)
        this_total = (this_total * 17) % 256
    return this_total

src = open("./input.txt").read().split(",")

print(sum(map(into_nums, src)))