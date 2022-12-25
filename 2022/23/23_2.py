import sys
from collections import Counter

n4_offsets = [(0, -1), (0, 1), (-1, 0), (1, 0)]
n8_offsets = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
dircheck_offsets = [ 
        [o for o in n8_offsets if o[1] == -1],
        [o for o in n8_offsets if o[1] == 1],
        [o for o in n8_offsets if o[0] == -1],
        [o for o in n8_offsets if o[0] == 1]    
    ]

def propose(pos, startdir):
    x, y = pos
    if any((x + o[0], y + o[1]) in elves for o in n8_offsets):
        for dir_offset in range(4):
            dir = (startdir + dir_offset) % 4
            if all((x + o[0], y + o[1]) not in elves for o in dircheck_offsets[dir]):
                return (x + n4_offsets[dir][0], y + n4_offsets[dir][1]), dir
    return pos, None

elves = set()
for y, line in enumerate(sys.stdin.read().splitlines()):
    for x, c in enumerate(line):
        if c == '#':
            elves.add((x, y))

startdir = 0
for r in range(10000000):
    counters = Counter()
    targets = {}
    moved = False
    for pos in elves:
        target, dir = propose(pos, startdir)
        counters[target] += 1
        targets.update({target : pos})
        moved |= (dir != None)
    if moved == False:
        print(r+1)
        exit(0)

    for target, pos in targets.items():
        if counters[target] == 1:
            elves.remove(pos)
            elves.add(target)

    startdir = (startdir + 1) % 4
