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
def inspect(n):
    check = True
    for i in range(0, len(n)):
        if is_prime(i) and (not is_prime(n[i])):
            check = False
            break
        elif (not is_prime(i)) and is_prime(n[i]):
            check = False
            break
    return check
t = int(input())
while t >0:
    n = input()
    if inspect(n):
        print('YES')
    else:
        print('NO')
    t-=1