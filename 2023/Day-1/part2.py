src = open("./input.txt").read().split("\n")[:-1]

chars = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
nums = []

for line in src:
    tens, ones = None, 0
    digit = None

    for i in range(0, len(line)):
        
        if line[i].isdigit():
            digit = int(line[i])

        for j, num in enumerate(chars):
            print(line[i:i + len(num)])
            if(line[i:i + len(num)]) == num:
                digit = j + 1

        if digit is not None:
            if tens == None:
                tens = digit * 10
            ones = digit

    nums.append(tens + ones)

print(sum(nums))