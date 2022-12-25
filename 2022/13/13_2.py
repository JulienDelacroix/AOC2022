import sys
import functools

def cmp(obj1, obj2):
    if isinstance(obj1, int) and isinstance(obj2, int):
        if obj1 < obj2: return -1
        if obj1 > obj2: return 1
        return 0

    if isinstance(obj1, int): return cmp([obj1], obj2)
    if isinstance(obj2, int): return cmp(obj1, [obj2])
    
    for i in range(min(len(obj1), len(obj2))):
        compare = cmp(obj1[i], obj2[i])
        if compare:
            return compare
    return cmp(len(obj1), len(obj2))

packets = [[[2]], [[6]]]
for block in sys.stdin.read().split("\n\n"):
    packets.extend(map(eval, block.splitlines()))

packets.sort(key=functools.cmp_to_key(cmp))
print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))
