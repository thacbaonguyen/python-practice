rs ='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(int(input())):
    n ,b = map(int, input().split())
    result = ''
    while n > 0:
        k = n % b
        result += rs[k]
        n//=b
    print(''.join(reversed(result)))
