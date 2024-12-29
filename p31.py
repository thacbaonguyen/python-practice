t = int(input())
while t >0:
    s = input()
    check = True
    if s[0] == s[1]:
        check = False
    for i in range(0, len(s) - 2):
        if s[i] != s[i + 2]: check = False
    if check:
        print('YES')
    else: print('NO')
    t-=1

