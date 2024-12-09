
t = int(input())
while t > 0:
    check = True
    s = input()
    reverse_s = ''.join(reversed(s))
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(reverse_s[i]) - ord(reverse_s[i - 1])): check = False
    if check: print('YES')
    else: print('NO')
    t-=1