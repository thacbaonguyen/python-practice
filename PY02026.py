from collections import Counter

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c1 = Counter(a)
c2 = Counter(b)
check = True
for x, y in c1.items():
    if x not in c2:
        check = False
        break
for x, y in c2.items():
    if x not in c1:
        check = False
        break
if check:
    print('YES')
else:
    print('NO')