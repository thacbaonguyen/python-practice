import math


def solve(n):
    sum_ =0
    for i in n:
        sum_ += int(i)
    return sum_
def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2== 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or (n % (i + 2) == 0):
            return False
    return True
t = int(input())
while t>0:
    n = input()
    if is_prime(solve(n)):
        print('YES')
    else:
        print('NO')
    t-=1