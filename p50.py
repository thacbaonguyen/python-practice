import math


def is_prime(n):
    n = int(n)
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
t = int(input())
while t > 0:
    n = input()
    if is_prime(n[0:3]) and is_prime(n[len(n) - 3:]):
        print('YES')
    else:
        print('NO')
    t-=1