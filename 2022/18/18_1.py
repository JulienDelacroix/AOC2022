import sys 
import re
from collections import Counter
import functools

counters = [ {} for c in range(3) ]

result = 0
all_pos = set()
for line in sys.stdin.read().splitlines():
    tokens = line.split()
    x, y, z = map(int, line.split(","))
    pos = (x, y, z)
    print(x, y, z)
    if (x,y) in counters[0]:
        counters[0][(x,y)].append(pos)
    else: 
        counters[0][(x,y)] = [pos]

    if (y,z) in counters[1]:
        counters[1][(y,z)].append(pos)
    else: 
        counters[1][(y,z)] = [pos]

    if (z,x) in counters[2]:
        counters[2][(z,x)].append(pos)
    else: 
        counters[2][(z,x)] = [pos]
    all_pos.add(pos)

    result += 6

print(result)
print(counters)

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
