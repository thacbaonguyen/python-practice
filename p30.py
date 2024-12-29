t = int(input())
while t >0:
    n = int(input())
    count = 0
    if n % 7 == 0: print(n)
    while n % 7 !=0:
        if count == 1001: print('-1')
        n = n + int(str(n)[::-1])
        if n% 7 == 0:
            print(n)
            break
    t-=1



