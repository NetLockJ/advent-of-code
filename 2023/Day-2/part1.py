import re

src = open('./input.txt').read()
src = src.replace(";", ",").split("\n")[:-1]
game = 0
game_nums = 0
for line in src:
    game += 1
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

    if(blue <= 14 and red <= 12 and green <= 13):
        game_nums += game
        print(game, colors)

print(game_nums)