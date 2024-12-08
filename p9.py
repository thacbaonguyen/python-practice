t = int(input())
while t >0:
    a = input().split()
    n, x, m = float(a[0]), float(a[1]), float(a[2])
    count = 0
    while n < m:
        n+= n*x/100
        count+=1
    print(count)
    t-=1