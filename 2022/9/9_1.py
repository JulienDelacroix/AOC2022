import sys

def move(pos, dir):
    if(dir=="R"): return (pos[0] + 1, pos[1])
    if(dir=="L"): return (pos[0] - 1, pos[1])
    if(dir=="U"): return (pos[0], pos[1] + 1)
    if(dir=="D"): return (pos[0], pos[1] - 1)
    return pos

def newTail(head, tail):
    delta = (head[0] - tail[0], head[1] - tail[1])
    if abs(delta[0]) == 2:
        return (tail[0] + delta[0] // 2, head[1])
    if abs(delta[1]) == 2:
        return (head[0], tail[1] + delta[1] // 2)
    return tail

tracked = set()
head, tail = (0, 0), (0, 0)
for l in sys.stdin.read().splitlines():
    dir, distance = l.split()
    for count in range(int(distance)):
        head = move(head, dir)
        for i in range(1, 10):
            tail = newTail(head, tail)
        tracked.add(tail)

print(len(tracked))
