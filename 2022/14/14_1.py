
import sys
import re
import numpy as np

def down(pos): return (pos[0] + 1, pos[1])
def downLeft(pos): return (pos[0] + 1, pos[1] - 1)
def downRight(pos): return (pos[0] + 1, pos[1] + 1)

grid = np.full((10000, 10000), 0)

H_max, W_max = 0, 0
H_min, W_min = 10000, 10000
for line in sys.stdin.read().splitlines():
    path = [ tuple(map(int, token.split(","))) for token in line.split("->") ]
    for (x1, y1), (x2, y2) in zip(path, path[1:]):
        x1, x2 = sorted([x1, x2])
        y1, y2 = sorted([y1, y2])        
        grid[y1 : y2 + 1, x1 : x2 + 1] = 1
        H_max, W_max = max(y2, H_max), max(x2, W_max)
        H_min, W_min = min(y1, H_min), min(x1, W_min)

sand = 0
pos = (0, 500)
while pos[0] < H_max:
    if grid[down(pos)] == 0:
        pos = down(pos)
    elif grid[downLeft(pos)] == 0:
        pos = downLeft(pos)
    elif grid[downRight(pos)] == 0:
        pos = downRight(pos)
    else:
        sand += 1
        grid[pos] = 1
        pos = (0, 500)
        
print(grid[0:H_max+5, W_min-5:W_max+5])
print(sand)
