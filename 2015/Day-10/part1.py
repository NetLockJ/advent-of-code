src = open("./input.txt", 'r').read()

def differ(chars: list):
    indicies = [0]
    for i in range(1, len(chars)):
        if(chars[i-1] != chars[i]):
            indicies.append(i)
    indicies.append(len(chars))
    return indicies

for i in range(0, 40):
    change = differ(src)
    len_change = change
    real_lengths = []
    for i in range(0, len(len_change) - 1):
        real_lengths.append(len_change[i + 1] - len_change[i])
    updated_src = ""
    i = 0
    for l in real_lengths:
        updated_src += str(l) + src[change[i]]
        i += 1

    src = updated_src

print(src)
print(len(src))