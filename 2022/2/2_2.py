import sys

values = [1, 2, 3]
scores = [ 0, 3, 6]
replies = [ [2, 0, 1], [0, 1, 2], [1, 2, 0] ]

result = 0
for line in sys.stdin.read().splitlines():
    opp, self = line.split()
    opp_index = ord(opp)-ord('A')
    outcome = ord(self)-ord('X')

    self_index = replies[opp_index][outcome]
    result += values[self_index] + scores[outcome]

print(result)
