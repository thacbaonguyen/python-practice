import math

t = int(input())
while t > 0:
    n = input()
    a = int(n[0:2])
    b = int(n[len(n) - 2:])
    if a == b:
        print('YES')
    else:
        print('NO')
    t-=1
