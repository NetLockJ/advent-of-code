from itertools import combinations
import re

file = open("./input.txt", "r").read().split("\n")


class Machine:
    def __init__(self, indicator, buttons, joltage):
        self.indicator = indicator
        self.buttons = buttons
        self.joltage = joltage

    def __str__(self):
        return f"{self.indicator} : {self.buttons} : {self.joltage}"
    
def simulate_presses(indicator, buttons):
    test_indicator = [0] * len(indicator)
    for button in buttons:
        for b in button:
            test_indicator[b] = (test_indicator[b] + 1) % 2
    
    return test_indicator == indicator

machines = []

for line in file:
    buttons = re.findall(r"(\((?:\d,)*\d\))", line)

    indicator = line.split(" ")[0]
    indicator = indicator[1:len(indicator) - 1]

    joltage = line.split(" ")[-1:]
    joltage = list(map(int, re.findall(r"\d+", joltage[0])))

    num_buttons = []

    for b in buttons:
        num_buttons.append(list(map(int,re.findall(r"\d", b))))

    machines.append(Machine(indicator, num_buttons, joltage))

count = []

for m in machines:
    correct = []
    ind = list(map(lambda ch: 1 if ch == "#" else 0, list(m.indicator)))
    for comb in (combinations(m.buttons, (i)) for i in range(len(m.buttons))):
        for c in comb:
            if simulate_presses(ind, c):
                correct.append(len(c))

    count.append(correct)
                
print(sum([c[0] for c in count]))