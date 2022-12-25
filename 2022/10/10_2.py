import sys

values = [ 1 ]
for tokens in [l.split() for l in sys.stdin.read().splitlines()]:
    if tokens[0] == "noop":
        values.append(values[-1])
    elif tokens[0] == "addx":
        values.append(values[-1])
        values.append(values[-1]+int(tokens[1]))

for y in range(6):
    line =['.'] * 40
    for x in range(40):
        if abs(x-values[y * 40 + x]) <= 1:
            line[x] = '#'
    print("".join(line))
    