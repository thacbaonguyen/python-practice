for t in range(int(input())):
    n,k = [int(x) for x in input().split()]
    if k%2==1: print('A')
    else: result =0
    while k!=2**(n-1):
        if k>(2**n)/2: k = 2**n-k
        n -=1
        print(chr(n+64))