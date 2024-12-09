import math

t = int(input())
while t >0:
    n = int(input())
    m = n
    print('1 ', end='')
    for i in range(2, int(math.sqrt(m)) + 1):
        count = 0
        while n % i == 0:
            count+=1
            n//=i
        if count != 0: print('* ', i, '^', count, ' ',sep='', end='')
    if n != 1: print('* ', n, '^1', sep = '')
    else: print()
    t-=1