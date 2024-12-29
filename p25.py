import math

n = int(input())
while n > 0:
    a = int(input())
    tmp = str(a)
    if math.gcd(a, int(tmp[::-1])) == 1: print('YES')
    else: print('NO')
    n-=1