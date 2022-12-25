line = input()
print(next(i for i in range(4, len(line)) if len(set(line[i-14:i])) == 14))
