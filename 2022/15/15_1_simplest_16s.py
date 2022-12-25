
import sys
import re

ROW = 2000000

def dist(pos1, pos2):
    return abs(pos2[0] - pos1[0]) + abs(pos2[1] - pos1[1])

sensors = []
beacons = set()
for line in sys.stdin.read().splitlines():
    x1, y1, x2, y2 = map(int, re.findall("-?\d+", line))
    sensor, beacon = (x1, y1), (x2, y2)
    sensors.append((sensor, dist(sensor, beacon)))
    beacons.add(beacon)

min_x = min(x - d for (x, _), d in sensors)
max_x = max(x + d for (x, _), d in sensors)
sensors.sort(key=lambda s: abs(s[0][1] - ROW) - s[1])

reachable = set()
for x in range(min_x, max_x+1):
    if any(dist((x, ROW), s) <= d for s, d in sensors):
        reachable.add((x, ROW))

print(len(reachable-beacons))
