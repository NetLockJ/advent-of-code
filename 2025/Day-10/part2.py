# Learned Z3 from reddit and based solution off of one there, not easy, but neat puzzle

from collections import defaultdict
import z3

file = open("input.txt", "r").read()

total = 0

for line in file.splitlines():
        _, *buttons, joltages = line.split()
        joltages = list(map(int, joltages[1:-1].split(',')))
        solver = z3.Optimize()
        z_buttons = z3.IntVector("z_buttons", len(buttons))

        # Maps locations to buttons, so (ex.) display[0] can be turned on by 1, 2, 4 ...
        display_buttons = defaultdict(list)
        
        for i, button in enumerate(buttons):
            solver.add(z_buttons[i] >= 0)
            for j in button[1:-1].split(','):
                display_buttons[int(j)].append(i)

        for j, indices in display_buttons.items():
            solver.add(joltages[j] == sum(z_buttons[i] for i in indices))

        presses = z3.Sum(z_buttons)
        solver.minimize(presses)
        solver.check()
        total += solver.model().eval(presses).as_long()
    
print(total)