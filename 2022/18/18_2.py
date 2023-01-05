import sys 
import re
from collections import Counter
import functools
from queue import Queue

XMIN, YMIN, ZMIN = 1000, 1000, 1000
XMAX, YMAX, ZMAX = 0, 0, 0
CUBES = set()

def next_cubes(x, y, z):
    yield(x-1, y, z)
    yield(x+1, y, z)
    yield(x, y-1, z)
    yield(x, y+1, z)
    yield(x, y, z-1)
    yield(x, y, z+1)

def outside(x, y, z):
    return x<XMIN or x>XMAX or y<YMIN or y>YMAX or z<ZMIN or z>ZMAX


def find_trapped():
    all_visited = set()
    all_trapped = set()
    for x in range(XMIN-1, XMAX+2):
        for y in range(YMIN-1, YMAX+2):
            for z in range(ZMIN-1, ZMAX+2):
                start_pos = (x, y, z)
                if start_pos not in all_visited and start_pos not in CUBES:
                    visited = set()
                    q = Queue()
                    q.put(start_pos)
                    visited.add(start_pos)
                    trapped = True
                    while not q.empty():
                        pos = q.get()
                        if outside(*pos):
                            trapped = False
                        else:
                            for next_pos in next_cubes(*pos):
                                if next_pos not in visited and next_pos not in CUBES:
                                    q.put(next_pos)
                                    visited.add(next_pos)
                    if trapped:
                        #print(len(visited))
                        all_trapped.update(visited)
                    all_visited.update(visited)
    return all_trapped


counters = [ {} for c in range(3) ]


result = 0
for line in sys.stdin.read().splitlines():
    tokens = line.split()
    x, y, z = map(int, line.split(","))
    XMIN, XMAX = min(XMIN, x), max(XMAX, x)
    YMIN, YMAX = min(YMIN, y), max(YMAX, y)
    ZMIN, ZMAX = min(ZMIN, z), max(ZMAX, z)
    pos = (x, y, z)    
    CUBES.add(pos)

all_trapped = find_trapped()
CUBES.update(all_trapped)

for cube in list(CUBES):
    (x, y, z) = cube
    if (x,y) in counters[0]:
        counters[0][(x,y)].append(cube)
    else: 
        counters[0][(x,y)] = [cube]

    if (y,z) in counters[1]:
        counters[1][(y,z)].append(cube)
    else: 
        counters[1][(y,z)] = [cube]

    if (z,x) in counters[2]:
        counters[2][(z,x)].append(cube)
    else: 
        counters[2][(z,x)] = [cube]

    result += 6

for k, pos in counters[0].items():
    pos.sort(key = lambda k: k[2])
    for p1, p2 in zip(pos, pos[1:]):
        if p1[2] + 1 == p2[2]:
            result -= 2

for k, pos in counters[1].items():
    pos.sort(key = lambda k: k[0])
    for p1, p2 in zip(pos, pos[1:]):
        if p1[0] + 1 == p2[0]:
            result -= 2
   
for k, pos in counters[2].items():
    pos.sort(key = lambda k: k[1])
    for p1, p2 in zip(pos, pos[1:]):
        if p1[1] + 1 == p2[1]:
            result -= 2
print(result)
