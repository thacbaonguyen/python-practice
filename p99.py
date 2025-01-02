t = int(input())
a = []
b = []
c = []
while len(a) < t:
    a += list(map(int, input().split()))
for i in range(len(a)):
    if a[i] % 2 ==0:
        b.append(a[i])
    else:
        c.append(a[i])
b.sort()
c.sort(reverse=True)
ic= 0
il = 0
for i in range(len(a)):
    if a[i]% 2 == 0:
        a[i] = b[ic]
        ic+=1
    else:
        a[i] = c[il]
        il+=1
print(*a, sep=' ')