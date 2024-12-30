import math


def is_prime(n):
    n = int(n)
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(math.sqrt(n))+1):
        if n % i ==0:
            return False
    return True
def inspect(n):
    c1 =0
    c2 =0
    for i in n:
        if is_prime(i):
            c1+=1
        else:
            c2+=1
    if c1 > c2:
        return True
    return False
t = int(input())
while t>0:
    n = input()
    if is_prime(len(n)) and inspect(n):
        print('YES')
    else:
        print('NO')
    t-=1