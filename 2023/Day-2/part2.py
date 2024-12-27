import re

src = open('./input.txt').read()
src = src.replace(";", ",").split("\n")[:-1]
power_cube = 0

for line in src:
    colors = {"red": 0, "blue" : 0, "green" : 0}
    line = ''.join(line.split(":")[1:])[1:]
    line = line.split(",")

    for part in line:
        part = part.lstrip()
        num = int(re.findall("\d+", part)[0])
        colors[part[2:len(part)].lstrip()]= max(colors[part[2:len(part)].lstrip()], num)

    blue = colors['blue']
    red = colors['red']
    green = colors['green']

    power_cube += blue * red * green

print(power_cube)