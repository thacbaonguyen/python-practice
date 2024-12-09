t = int(input())
while t >0:
    n = input()
    end = int(n[len(n) - 2:])
    if end == 86:
        print('YES')
    else:
        print('NO')
    t-=1