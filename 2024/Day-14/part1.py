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

def count_in(xmin, xmax, ymin, ymax):
    total = 0
    for i in range(ymin, ymax):
        for j in range(xmin, xmax):
            total += arr[i][j]
    return total


for line in input:
    nums = map(int, re.findall("-?\d+", line))
    robots.append(Robot(*nums))

for i in range(100):
    for robot in robots:
        robot.step()
        print(robot)

arr = np.zeros((y_max, x_max))

for robot in robots:
    arr[robot.y][robot.x] = arr[robot.y][robot.x] + 1

rows, cols = arr.shape
row_mid, col_mid = rows // 2, cols // 2

top_left = arr[:row_mid, :col_mid]
top_right = arr[:row_mid, col_mid + 1:]
bottom_left = arr[row_mid + 1:, :col_mid]
bottom_right = arr[row_mid + 1:, col_mid + 1:]


print(top_right, "\n\n", top_left, "\n\n", bottom_left, "\n\n", bottom_right)

print(sum(sum(top_right)) * sum(sum(top_left)) * sum(sum(bottom_left)) * sum(sum(bottom_right)))