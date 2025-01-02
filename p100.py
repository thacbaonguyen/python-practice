import math

rs = []
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True
for i in range(2, 10000):
    if is_prime(i):
        rs.append(i)
t = int(input())
a = list(map(int, input().split()))
tmp = 0
for i in a:
    step_min = float('inf')
    for target in rs:
        step_min = min(step_min, abs(i - target))
    tmp = max(tmp, step_min)
print(tmp)

