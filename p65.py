import math
def is_prime(n):
    if n < 2:
        return False
    if n ==2:
        return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
t = int(input())
a = list(map(int, input().split()))
rs = []
for i in range(len(a)):
    if is_prime(a[i]):
        rs.append((a[i], a.count(a[i])))
seen = set()
data =[]
for item in rs:
    if item not in seen:
        seen.add(item)
        data.append(item)
for key, value in data:
    print(key, value)