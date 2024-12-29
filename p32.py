def is_correct(n, k):
    for i in range(1, k + 1):
        if n[i] <= n[i -1]:
            return False
    for i in range(k, len(n) -1):
        if n[i] <= n[i + 1]:
            return False
    return True
t = int(input())
while t >0:
    n = input()
    size = len(n)
    check = True
    tmp =0
    for i in range(1, size - 1):
        if n[i] == n[i-1]:
            check = False
        if n[i] > n[i -1] and n[i] > n[i + 1]:
            tmp = i
    if tmp == 0 or check == False:
        print('NO')
    else:
        if is_correct(n, tmp): print('YES')
        else: print('NO')
    t-=1
