def is_division(n):
    result = 0
    while n >0:
        result += n % 10
        n//=10
    if result % 10 == 0: return True;
    return False

def is_equals(n):
    check = True
    s = str(n)
    for i in range(1, len(s)):
        if abs(int(s[i]) - int(s[i - 1])) != 2: check = False;
    return check
t = int(input())
while t > 0:
    n = int(input())
    if is_division(n) and is_equals(n): print('YES')
    else: print('NO')
    t-= 1