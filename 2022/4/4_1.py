import sys
import re

result = 0
for line in sys.stdin.read().splitlines():
    l1, u1, l2, u2 = map(int, re.findall("\d+", line))
    if (l1 >= l2 and u1 <= u2) or (l2 >= l1 and u2 <= u1):
        result +=1
print(result)
