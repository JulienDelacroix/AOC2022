import sys 

xmin, xmax, ymin, ymax = {}, {}, {}, {}

def nextpos(pos, facing):
    x, y = pos
    if facing == 0: return (x+1, y) if (x+1, y) in grid else (xmin[y], y)
    if facing == 1: return (x, y+1) if (x, y+1) in grid else (x, ymin[x])
    if facing == 2: return (x-1, y) if (x-1, y) in grid else (xmax[y], y)
    if facing == 3: return (x, y-1) if (x, y-1) in grid else (x, ymax[x])
    return pos

def move(pos, d, facing):
    p = pos
    for _ in range(d):
        np = nextpos(p, facing)
        if grid[np] == '#':
            break
        p = np
    return p 


def update(k, v, vmin, vmax):
    if k in vmin:
        vmin[k] = min(vmin[k], v)
    else:
        vmin.update({k : v})

    if k in vmax:
        vmax[k] = max(vmax[k], v) 
    else:
        vmax.update({k : v})

pos = 10000, 10000
grid = {}

blocks = sys.stdin.read().split("\n\n")
map, moves = blocks[0], blocks[1]
for y, line in enumerate(map.splitlines()):
    for x, c in enumerate(line):
        if c == '.' or c == '#':
            update(x, y, ymin, ymax)
            update(y, x, xmin, xmax)
            grid.update({(x, y) : c})

y = min(xmin.keys())
x = xmin[y]
pos = (x, y)
facing = 0

d_str = ""
for c in moves:
    if c == 'R' or c == 'L':
        pos = move(pos, int(d_str), facing)
        facing = (facing + (1 if c == 'R' else 3)) % 4
        d_str = ""
    else:
        d_str += c
if d_str: 
    pos = move(pos, int(d_str), facing)

x, y = pos
print(pos, 1000 * (y+1) + 4 * (x+1) + facing)
