line = input()
print(next(i for i in range(4, len(line)) if len(set(line[i-4:i])) == 4))
