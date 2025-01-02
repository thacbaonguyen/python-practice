for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    check = True
    for i in range(len(a)):
        if a[i] > b[i]:
            check = False
            break
    if check:
        print('YES')
    else:
        print('NO')
