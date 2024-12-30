def inspect(a, b):
    a.sort()
    b.sort()
    for i in range(0, len(a)):
        if a[i] > b[i]:
            return False
    return True
t = int(input())
while t>0:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if inspect(a, b):
        print('YES')
    else:
        print('NO')
    t-=1