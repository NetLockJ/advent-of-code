from collections import deque
import numpy as np
import tqdm

def add(t1, t2):
    return tuple(map(lambda a, b: a + b, t1, t2))

def simulate_grid(pos, dir):
    energized = set()
    seen = set()

    tiles_to_process = deque()
    tiles_to_process.append((pos, dir))

    energized.add(pos)

    while tiles_to_process:
        tile = tiles_to_process.popleft()
        current_pos = tile[0]

        if((current_pos, tile[1])) in seen:
            continue

        if current_pos[0] < 0 or current_pos[0] > len(src) - 1 or current_pos[1] < 0 or current_pos[1] > len(src[0]) - 1: 
            continue

        energized.add(current_pos)
        seen.add((current_pos, tile[1]))

        mirror_output = mirrors[src[current_pos[0]][current_pos[1]]][tile[1]]
        for mo in mirror_output:
            tiles_to_process.append((add(current_pos, directions[mo]), mo))

    return(len(energized))


# mirror -> input_dir -> output_dir
mirrors = {"/" : {"U" : ["L"], "D" : ["R"], "R" : ["D"], "L" : ["U"]},
           "\\" : {"U" : ["R"], "D" : ["L"], "R" : ["U"], "L" : ["D"]},
           "|" : {"U" : ["U"], "D" : ["D"], "L": ["U", "D"], "R" : ["U", "D"]},
           "-" : {"U" : ["R", "L"], "D" : ["R", "L"], "L": ["L"], "R" : ["R"]},
           "." : {"U" : ["U"], "D" : ["D"], "L" : ["L"], "R" : ["R"]}
           }

directions = {"U": (1, 0), "D" : (-1, 0), "L" : (0, -1), "R": (0, 1)}

src = np.array([list(l) for l in open("./input.txt").read().split("\n")])

traveled_src = grid = np.array([list(c) for c in src])

edge_counts = []

for i in tqdm.tqdm(range(0, len(src))):
    edge_counts.append(simulate_grid((i,0), "R"))
    edge_counts.append(simulate_grid((i,len(src[0]) - 1), "L"))

for i in tqdm.tqdm(range(0, len(src[0]))):
    edge_counts.append(simulate_grid((0,i), "U"))
    edge_counts.append(simulate_grid((len(src) - 1, i), "D"))

print(max(edge_counts))