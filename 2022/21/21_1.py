import sys

monkeys = {}
def compute(v1, v2, op):
    if op == '+': return (v1 + v2)
    if op == '-': return (v1 - v2)
    if op == '/': return (v1 / v2)
    if op == '*': return (v1 * v2)
    return 0

def recursive_eval(m):
    tokens = monkeys[m]
    if len(tokens) == 1: 
        return int(monkeys[m][0])
    else:
        v1, op, v2 = monkeys[m]
        v1 = recursive_eval(v1)
        v2 = recursive_eval(v2)
        return compute(v1, v2, op)

for line in sys.stdin.read().splitlines():
    m, action = line.split(":")
    tokens = action.split()
    monkeys.update({m : tokens})

print(recursive_eval("root"))
