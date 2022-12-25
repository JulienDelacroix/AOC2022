import sys
import numpy as np
from queue import Queue

def arround(pos):
    y, x = pos
    if y+1 < H: yield (y + 1, x)
    if y > 0: yield (y - 1, x)
    if x+1 < W: yield (y, x + 1)
    if x > 0: yield (y, x - 1)

grid = np.array([[c for c in l] for l in sys.stdin.read().splitlines()])
dist = np.full(grid.shape, 10000)
H, W = grid.shape

start = next(zip(*np.where(grid == 'S')))
stop = next(zip(*np.where(grid == 'E')))
grid[start] = 'a'
grid[stop] = 'z'

queue = Queue()
dist[start] = 0
queue.put(start)

while not queue.empty():
    pos = queue.get()
    for next_pos in arround(pos):
        if ord(grid[next_pos]) <= ord(grid[pos])+1 and dist[next_pos]>dist[pos]+1:
            dist[next_pos] = dist[pos]+1
            queue.put((next_pos))

print(dist[stop])
