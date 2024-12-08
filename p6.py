import math
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
n = int(input())
while n > 0:
    count = 0;
    k = int(input())
    for i in range(1, k):
        if math.gcd(k, i) == 1:
            count+=1;
    if is_prime(count) == True:
        print('YES')
    else:
        print('NO')
    n-=1;