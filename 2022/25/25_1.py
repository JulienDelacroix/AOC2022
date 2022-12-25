import sys 

values = { '=' : -2, "-" : -1, '0' : 0, '1' : 1, '2' : 2}
def read(line):
    res = 0
    power = 1
    for c in reversed(line):
        res += power * values[c]
        power *= 5
    return res

s = sum(map(read, sys.stdin.read().splitlines()))
carry = 0
res = []
while s:
    digit = s % 5 + carry
    if digit == 0: c, carry = '0', 0 
    if digit == 1: c, carry = '1', 0 
    if digit == 2: c, carry = '2', 0 
    if digit == 3: c, carry = '=', 1 
    if digit == 4: c, carry = '-', 1 
    if digit == 5: c, carry = '0', 1 
    res.append(c)
    s //= 5

if carry: res.append('1')
print("".join(reversed(res)))