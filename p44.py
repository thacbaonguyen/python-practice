def solve(n):
    check = True
    for i in range(2, len(n), 2):
        if n[i] != n[i -2]:
            check = False
    return check
t = int(input())
while t >0:
    n = input()
    if len(n) % 2 ==1 and (n[0] != n[1]) and solve(n):
        print('YES')
    else:
        print('NO')
    t-=1
