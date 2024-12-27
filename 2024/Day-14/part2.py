import re
import numpy as np

x_max = 101
y_max = 103

class Robot:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def step(self):
        self.x = (self.x + self.vx) % (x_max )
        self.y = (self.y + self.vy) % (y_max )

    def __str__(self):
        return f"x={self.x},y={self.y}, vx={self.vx},vy={self.vy}"
    
    def __repr__(self):
        return f"Robot(x={self.x},y={self.y},vx={self.vx},vy={self.vy})"

input = open("input.txt", "r").read().split("\n")
robots = []


for line in input:
    nums = map(int, re.findall("-?\d+", line))
    robots.append(Robot(*nums))

for i in range(100000):
    pos = set()
    for robot in robots:
        robot.step()
        pos.add((robot.x, robot.y))
    if(len(pos) == 500):
        print(i + 1)
        break
        