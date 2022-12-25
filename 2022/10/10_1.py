import sys

values = [ 1 ]
for tokens in [line.split() for line in sys.stdin.read().splitlines()]:
    if tokens[0] == "noop":
        values.append(values[-1])
    elif tokens[0] == "addx":
        values.append(values[-1])
        values.append(values[-1]+int(tokens[1]))

print(sum(c*values[c-1] for c in range(20, 221, 40)))
