P = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
while True:
    n = input().split()
    k = int(n[0])
    s = str(n[1])
    s[1] = 'a'
    print(s[1])