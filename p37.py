import math

def is_prime(n):
    if n <=1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
t = int(input())
while t >0:
    n = input()
    rs = n[len(n) - 4:]
    if is_prime(int(rs)):
        print('YES')
    else:
        print('NO')
    t-=1