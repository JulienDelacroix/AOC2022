
import sys
import re

ROW = 2000000

def dist(pos1, pos2):
    return abs(pos2[0] - pos1[0]) + abs(pos2[1] - pos1[1])

def xrange(sensor_x, sensor_y, sensor_range):
    sensor_dist = abs(ROW - sensor_y)
    if sensor_dist < sensor_range:
        delta = sensor_range - sensor_dist
        return [[sensor_x - delta, sensor_x + delta]]
    return []

def mergeIntervals(intervals):
    intervals.sort()
    result = [intervals[0]]
    for current_start, current_end in intervals:
        _, stack_end = result[-1]
        if current_start > stack_end + 1:
            result.append([current_start, current_end])
            continue

        result[-1][1] = max(stack_end, current_end)
    return result

intervals = []
beacons = set()
for line in sys.stdin.read().splitlines():
    x_sensor, y_sensor, x_beacon, y_beacon = map(int, re.findall("-?\d+", line))
    sensor_range = dist((x_sensor, y_sensor), (x_beacon, y_beacon))
    intervals.extend(xrange(x_sensor, y_sensor, sensor_range))
    if y_beacon == ROW: beacons.add(y_beacon)

reachable = set()
for start, end in mergeIntervals(intervals):
    for x in range(start, end+1):
        reachable.add(x)

print(len(reachable-beacons))
