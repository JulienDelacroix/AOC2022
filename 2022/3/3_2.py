import string
letters = string.ascii_lowercase + string.ascii_uppercase
priorities = { c: index+1 for index, c in enumerate(letters)}

duplicate = []
while True:
    try:
        line1 = input()
        line2 = input()
        line3 = input()
    except EOFError:
        break

    duplicate += [c for c in letters if c in line1 and c in line2 and c in line3 ]

print(sum([priorities[c] for c in duplicate]))
