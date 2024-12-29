t = int(input())
while t >0:
    n = input()
    check = True
    for i in range(0, len(n)):
        if n[i]!= '0' and n[i] != '1' and n[i] != '2':
            check = False
            break
    if check:
        print('YES')
    else:
        print('NO')
    t-=1