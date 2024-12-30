import math
from heapq import nlargest


def is_prime(n):
    n = int(n)
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i ==0:
            return False
    return True
def inspect(n):
    check = True
    for i in range(0, len(n)):
        if i % 2 ==0 and int(n[i]) % 2 != 0:
            check = False
            break
        elif i % 2 == 1 and int(n[i]) % 2 ==0:
            check = False
            break
    return check
def solve(n):
    rs = 0
    for i in n:
        rs += int(i)
    return rs
t = int(input())
while t >0:
    n = input()
    if is_prime(solve(n)) and inspect(n):
        print('YES')
    else:
        print('NO')
    t-=1