import math
rs = []
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(math.sqrt(n)) +1 ):
        if n % i ==0:
            return False
    return True

for i in range(2, 8000):
    if len(rs) > 1000:
        break
    if is_prime(i):
        rs += [i]
n, x = map(int, input().split())
print(x, end=' ')
for i in range(0, n):
    x+=rs[i]
    print(x, end= ' ')