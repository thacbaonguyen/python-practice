def total_sum(n):
    rs = 0
    for i in str(n):
        rs += int(i)
    return rs
for i in range(int(input())):
    n = int(input())
    tmp = []
    a = list(map(int, input().split()))
    a.sort()
    for i in range(len(a)):
        tmp.append((a[i], total_sum(a[i])))
    rs = sorted(tmp, key=lambda x: (x[1], x[0]))
    for key, value in rs:
        print(key, end=' ')
    print()
