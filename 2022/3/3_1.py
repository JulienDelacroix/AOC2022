import sys
import string
letters = string.ascii_lowercase + string.ascii_uppercase
priorities = { c: index+1 for index, c in enumerate(letters)}

duplicate = []
for line in sys.stdin.read().splitlines():
    half_len = len(line)//2
    duplicate += [c for c in letters if c in line[0:half_len] and c in line[half_len:] ]

print(sum([priorities[c] for c in duplicate]))
