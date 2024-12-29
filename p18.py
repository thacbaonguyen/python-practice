P = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
while True:
    n = input().split()
    k = int(n[0])
    if k == 0: break;
    s = str(n[1])
    s1 = []
    for i in range(0, len(s)):
        y = P.find(s[i])
        x = (y + k)% 28
        if y + x <= 28:
            s1.append(P[x ])
        else:
            z = y + k - 28
            s1.append(P[z])
    result = ''.join(reversed(s1))
    print(result)
