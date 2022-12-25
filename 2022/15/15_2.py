import sys
import re

def dist(pos1, pos2):
    return abs(pos2[0] - pos1[0]) + abs(pos2[1] - pos1[1])

def awayfrom(sensor):
    s, d = sensor
    pos = (s[0] + d + 1, s[1])
    while pos != (s[0], s[1] - d - 1):
        yield pos
        pos = (pos[0] - 1, pos[1] - 1)
    while pos != (s[0] - d - 1, s[1]):
        yield pos
        pos = (pos[0] - 1, pos[1] + 1)
    while pos != (s[0], s[1] + d + 1):
        yield pos
        pos = (pos[0] + 1, pos[1] + 1)
    while pos != (s[0] + d + 1, s[1]):
        yield pos
        pos = (pos[0] + 1, pos[1] - 1)

sensors = []
beacons = set()
for line in sys.stdin.read().splitlines():
    x1, y1, x2, y2 = map(int, re.findall("-?\d+", line))
    sensor, beacon = (x1, y1), (x2, y2)
    sensors.append((sensor, dist(sensor, beacon)))
    beacons.add(beacon)

for sensor in sorted(sensors, key=lambda s: s[1]):
    for pos in awayfrom(sensor):
        if pos[0] < 0 or pos[1] < 0: continue
        if pos[0] > 4000000 or pos[1] > 4000000: continue
        if pos in beacons: continue
        if any(dist(pos, s) <= d for s, d in sensors): continue

        print(pos[0] * 4000000 + pos[1])
        exit(0)