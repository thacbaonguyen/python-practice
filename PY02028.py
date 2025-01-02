import math


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i ==0:
            return False
    return True
t = int(input())
a = list(map(int, input().split()))
rs = []
for i in a:
    if is_prime(i):
        rs.append(i)
rs.sort()
idx = 0
for i in range(len(a)):
    if is_prime(a[i]):
        a[i] = rs[idx]
        idx+=1
print(*a)