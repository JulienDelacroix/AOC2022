import sys
from collections import Counter

path = []
sizes = Counter()
for line in sys.stdin.read().splitlines():
    tokens = line.split()
    if tokens[0] == "$":
        if tokens[1] == "cd":
            if tokens[2] == "/":
                path.clear()
            elif tokens[2] == "..":
                path.pop()
            else:
                path.append(tokens[2])
    elif tokens[0] != "dir":
        for index in range(len(path)+1):
            sizes[str(path[:index])] += int(tokens[0])

print(min([v for v in sizes.values() if 70000000 - sizes[str([])] + v >= 30000000]))
