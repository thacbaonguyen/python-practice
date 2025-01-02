n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()
m1 = {}
m2 = {}
for i in a:
    m1[i] = 1
for i in b:
    m2[i] = 1
for x in m1:
    if x in m2:
        print(x, end=' ')
print()
for x in m1:
    if x not in m2:
        print(x, end=' ')
print()
for x in m2:
    if x not in m1:
        print(x, end=' ')