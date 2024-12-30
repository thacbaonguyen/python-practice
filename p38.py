import math
def is_prime(n):
    n = int(n)
    if n <2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or (n % (i +2) == 0):
            return False
    return True
def solve(n):
    c_correct = 0
    c_incorrect = 0
    for i in n:
        if is_prime(i):
            c_correct+=1
        else:
            c_incorrect+=1
    if c_correct > c_incorrect:
        return True
    return False
t = int(input())
while t>0:
    n = input()
    if is_prime(len(n)) and solve(n):
        print('YES')
    else:
        print('NO')
    t-=1
