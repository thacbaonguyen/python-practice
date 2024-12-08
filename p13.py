import math
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def sum_digit(n):
    result = 0
    for digit in str(n):
        result += int(digit)
    return result
t = int(input())
while t > 0:
    a = input().split()
    b, c = map(int, a)
    d = math.gcd(b, c)
    if is_prime(sum_digit(d)):
        print('YES')
    else:
        print('NO')
    t-=1