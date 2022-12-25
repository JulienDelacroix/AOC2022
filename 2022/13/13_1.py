import sys

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

result = 0
for index, block in enumerate(sys.stdin.read().split("\n\n")):
    if cmp(*map(eval, block.splitlines())) == -1:
        result += (index + 1)
print(result)
