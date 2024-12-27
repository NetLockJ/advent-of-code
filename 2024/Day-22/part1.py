def mix(secret, mixing):
    return secret ^ mixing

def prune(secret):
    return secret % 16777216

def generate_secrets(nums, iterations):
    new_nums = []
    for num in nums:
        for _ in range(iterations):
            num = prune(mix(num, num * 64))
            num = prune(mix(num, num // 32))
            num = prune(mix(num, num * 2048))
        new_nums.append(num)
    return new_nums

buy_secrets = map(int, open("input.txt", "r").read().splitlines())

print(sum(generate_secrets(buy_secrets, 2000)))