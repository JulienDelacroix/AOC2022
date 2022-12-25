import sys

item_list=[]
sum_list=[]

for item in sys.stdin.read().splitlines():
    if item:
        item_list.append(int(item))
    else:
        sum_list.append(sum(item_list))
        item_list = []

print(sum(sorted(sum_list)[-3:]))
