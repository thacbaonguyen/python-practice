from collections import Counter

for i in range(int(input())):
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    rs1 = Counter(a)
    rs2 = Counter(b)
    rs3 = Counter(c)
    check = True
    for x, y in rs1.items():
        if x in rs2 and x in rs3:
            tmp = min(y, rs2[x], rs3[x])
            for j in range(tmp):
                check = False
                print(x, end=' ')
    if check:
        print('NO')
    else:
        print()
