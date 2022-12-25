import sys

def right(v, d):
    res = v
    for _ in range(d % (s-1)):
        res = nextlist[res]
    return res

def left(v, d):
    res = v
    for _ in range(d % (s-1)):
        res = prevlist[res]
    return res

values = [ v * 811589153 for v in map(int, sys.stdin.read().splitlines()) ]
indexed = list(enumerate(values))
s = len(indexed)

prevlist = { indexed[i] : indexed[(s+i-1) % s] for i in range(s) }
nextlist = { indexed[i] : indexed[(i+1) % s] for i in range(s) }

for _ in range(10):
    for v1 in indexed:
        if v1[1] == 0: continue

        v2 = right(v1, v1[1]) if v1[1] > 0 else left(v1, -v1[1] + 1)
        if v2 == v1 or v2 == prevlist[v1]: continue 

        p1, n1 = prevlist[v1], nextlist[v1]
        _, n2 = prevlist[v2], nextlist[v2]

        nextlist[p1] = n1
        prevlist[n1] = p1
        nextlist[v2] = v1
        prevlist[v1] = v2
        nextlist[v1] = n2
        prevlist[n2] = v1

result = 0
p = (values.index(0), 0)
for i in range(1, s+1):
    p = nextlist[p]
    if i in [1000 % s, 2000 % s, 3000 % s]:
        result += p[1]

print(result)
