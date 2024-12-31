import math
def is_prime(n):
    if n <2:
        return False
    if n == 2:
        return True
    for i in range(2, int(math.sqrt(n)) +1):
        if n % i == 0:
            return False
    return True

n, m = map(int, input().split())
rs = []
for i in range(n):
    row = list(map(int, input().split()))
    rs.append(row)
for i in range(n):
    for j in range(m):
        if is_prime(rs[i][j]):
            rs[i][j] = 1
        else:
            rs[i][j] = 0
for i in range(n):
    for j in range(m):
        print(rs[i][j], end=' ')
    print()