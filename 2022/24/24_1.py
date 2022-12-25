import sys
from queue import Queue

left = set()
right = set()
up = set()
down = set()

lines = sys.stdin.read().splitlines()
XMIN, XMAX = 1, len(lines[0]) - 2
YMIN, YMAX = 1, len(lines) - 2

for y, line in enumerate(lines):
    if y == 0: start = (line.index('.'), y)
    if y == len(lines)-1: end = (line.index('.'), y)
    for x, c in enumerate(line):
        if c == '<': left.add((x, y))
        if c == '>': right.add((x, y))
        if c == '^': up.add((x, y))
        if c == 'v': down.add((x, y))

def next_pos(pos, time):
    x, y = pos
    for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1), (x, y)]:
        if (nx, ny) != start and (nx, ny) != end:
            if nx < XMIN or nx > XMAX or ny < YMIN or ny > YMAX: continue
        if (1 + (nx - 1 + XMAX + time) % XMAX, ny) in left: continue
        if (1 + (nx - 1 + XMAX - time) % XMAX, ny) in right: continue
        if (nx, 1 + (ny - 1 + YMAX + time) % YMAX) in up: continue
        if (nx, 1 + (ny - 1 + YMAX - time) % YMAX) in down: continue
        yield (nx, ny)

visited = set()
q = Queue()
q.put((0, start))
while not q.empty():
    time, pos = q.get()
    if pos == end:
        print(time)
        break
    for npos in next_pos(pos, time+1):
        if (time+1, npos) not in visited:
            q.put((time+1, npos))
            visited.add((time+1, npos))
