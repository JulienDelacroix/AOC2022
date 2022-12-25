
import sys
import re
import numpy as np

def down(pos): return (pos[0] + 1, pos[1])
def downLeft(pos): return (pos[0] + 1, pos[1] - 1)
def downRight(pos): return (pos[0] + 1, pos[1] + 1)

grid = np.full((10000, 10000), 0)

H_max = 0
for line in sys.stdin.read().splitlines():
    path = [ tuple(map(int, token.split(","))) for token in line.split("->") ]
    for (x1, y1), (x2, y2) in zip(path, path[1:]):
        x1, x2 = sorted([x1, x2])
        y1, y2 = sorted([y1, y2])        
        grid[y1 : y2 + 1, x1 : x2 + 1] = 1
        H_max = max(y2, H_max)

grid[H_max+2,:] = 1

sand = 0
path = [(0, 500)]
while path:
    pos = path[-1]
    if grid[down(pos)] == 0:
        path.append(down(pos))
    elif grid[downLeft(pos)] == 0:
        path.append(downLeft(pos))
    elif grid[downRight(pos)] == 0:
        path.append(downRight(pos))
    else:
        sand += 1
        grid[pos] = 1
        path.pop()

print(sand)
