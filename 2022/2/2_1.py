import sys

values = [1, 2, 3]
scores = [ [3, 0, 6], [6, 3, 0], [0, 6, 3] ]

result = 0
for line in sys.stdin.read().splitlines():
    opp, self = line.split()
    opp_index = ord(opp)-ord('A')
    self_index = ord(self)-ord('X')
    result += values[self_index] + scores[self_index][opp_index]

print(result)
