import sys 

monkeys = {}
ref = {}

def compute(v1, v2, op):
    if op == '+': return (v1 + v2)
    if op == '-': return (v1 - v2)
    if op == '/': return (v1 / v2)
    if op == '*': return (v1 * v2)
    return 0

def reverse_compute(left, right, op, is_first):
    if op == '+': return (left - right)
    if op == '-': return (left + right) if is_first else (right - left)
    if op == '/': return (left * right) if is_first else (right / left)
    if op == '*': return (left / right)
    return 0

def reverse_recursive_eval(m):
    left = ref[m]
    v1, op, v2 = monkeys[left]
    right, is_first = (v2, True) if m == v1 else (v1, False)

    if left == "root":
        return recursive_eval(v1 if v2 == m else v2)

    left = reverse_recursive_eval(left)
    right = recursive_eval(right)
    return reverse_compute(left, right, op, is_first)

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
    if m != "humn":
        monkeys.update({m : tokens})
    if len(tokens) == 3:
        ref.update({tokens[0] : m, tokens[2] : m})

print(reverse_recursive_eval("humn"))
