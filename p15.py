def is_increase(n):
    a = 0
    b = n % 10
    n//=10
    check = True
    while n > 0:
        a = n % 10
        if b < a: check = False
        b = a
        n//=10
    if check: return True
    else: return False

t = int(input())
while t> 0:
    n = int(input())
    if is_increase(n): print('YES')
    else: print('NO')
    t-=1