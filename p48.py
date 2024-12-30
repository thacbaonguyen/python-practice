def solve1(n):
    rs =0
    for i in range(0, len(n)):
        if i % 2 ==0:
            rs += int(n[i])
    return rs
def solve2(n):
    rs =1
    check = False
    for i in range(0, len(n)):
        if i % 2 !=0:
            if n[i] != '0':
                rs*= int(n[i])
                check = True
    if not check:
        return 0
    else:
        return rs
t = int(input())
while t >0:
    n = input()
    print(solve1(n), solve2(n), sep=' ')
    t-=1