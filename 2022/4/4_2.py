import sys
import re

result = 0
for line in sys.stdin.read().splitlines():
    l1, u1, l2, u2 = map(int, re.findall("\d+", line))
    if (u1 >= l2 and l1 <= u2):
        result +=1
print(result)
