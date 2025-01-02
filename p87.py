import re

for i in range(int(input())):
    a = input()
    b = []
    c = []
    for x in range(len(a)):
        if not a[x].isnumeric():
            b.append(a[x])
        else:
            c.append(int(a[x]))
    b.sort()
    rs = sum(c)
    print(*b, sep='',end='')
    print(rs)