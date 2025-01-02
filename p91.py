rs = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(int(input())):
    a, b = map(int, input().split())
    tmp = ''
    while a > 0:
        k = a%b
        tmp += rs[k]
        a//=b
    print(tmp[::-1])