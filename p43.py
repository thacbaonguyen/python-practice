def solve(n):
    rs =1
    for i in n:
        if i != '0':
            rs*= int(i)
    return rs
t = int(input())
while t>0:
    n = input()
    print(solve(n))
    t-=1