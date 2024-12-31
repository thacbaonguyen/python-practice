def solve(n):
    rs =1
    for i in str(n):
        rs*= int(i)
    return rs
for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    rs =[]
    for i in range(len(a)):
        rs.append((a[i], solve(a[i])))
    rs = sorted(rs, key=lambda x : (x[1], x[0]))
    for key, value in rs:
        print(key, end=' ')
    print()