import sys 

S = 50

def right(pos):
    cx, cy, x, y = pos
    if x + 1 < S: return (cx, cy, x+1, y), 0
    if cx == 2 and cy == 0: return (1, 2, S-1, S-y-1), 2 
    if cx == 1 and cy == 1: return (2, 0, y, S-1), 3
    if cx == 1 and cy == 2: return (2, 0, S-1, S-y-1), 2 
    if cx == 0 and cy == 3: return (1, 2, y, S-1) , 3 
    return (cx+1, cy, 0, y), 0

def down(pos):
    cx, cy, x, y = pos
    if y + 1 < S: return (cx, cy, x, y+1), 1
    if cx == 0 and cy == 3: return (2, 0, x, 0), 1 
    if cx == 1 and cy == 2: return (0, 3, S-1, x), 2 
    if cx == 2 and cy == 0: return (1, 1, S-1, x), 2 
    return (cx, cy+1, x, 0), 1

def left(pos):
    cx, cy, x, y = pos
    if x - 1 >= 0:
        return (cx, cy, x-1, y), 2
    if cx == 1 and cy == 0: return (0, 2, 0, S-y-1), 0 
    if cx == 1 and cy == 1: return (0, 2, y, 0), 1
    if cx == 0 and cy == 2: return (1, 0, 0, S-y-1), 0 
    if cx == 0 and cy == 3: return (1, 0, y, 0) , 1
    return (cx-1, cy, S-1, y), 2

def up(pos):
    cx, cy, x, y = pos
    if y - 1 >= 0: return (cx, cy, x, y-1), 3
    if cx == 0 and cy == 2: return (1, 1, 0, x), 0 
    if cx == 1 and cy == 0: return (0, 3, 0, x), 0 
    if cx == 2 and cy == 0: return (0, 3, x, S-1), 3 
    return (cx, cy-1, x, S-1), 3


def nextpos(pos, facing):
    if facing == 0: return right(pos)
    if facing == 1: return down(pos)
    if facing == 2: return left(pos)
    if facing == 3: return up(pos)

def move(pos, d, facing):
    p, f = pos, facing
    for _ in range(d):
        np, nf = nextpos(p, f)
        if grid[np] == '#':
            break
        p, f = np, nf    
    return p, f 


pos = 10000, 10000
grid = {}

blocks = sys.stdin.read().split("\n\n")
map, moves = blocks[0], blocks[1]
for y, line in enumerate(map.splitlines()):
    for x, c in enumerate(line):
        if c == '.' or c == '#':
            grid.update({(x // 50, y // 50, x % 50, y % 50) : c})

pos = (1, 0, 0, 0)
facing = 0

d_str = ""
for c in moves:
    if c == 'R' or c == 'L':
        pos, facing = move(pos, int(d_str), facing)
        facing = (facing + (1 if c == 'R' else 3)) % 4
        d_str = ""
    else:
        d_str += c
if d_str: 
    pos, facing = move(pos, int(d_str), facing)

cx, cy, x, y = pos
x = cx * S + x
y = cy * S + y
print(1000 * (y+1) + 4 * (x+1) + facing)
