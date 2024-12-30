t = int(input())
while t >0:
    rs= []
    max = 0
    n = int(input())
    while n >0:
        rs.append(int(input()))
        n-=1
    rs.sort()
    for i in range(0, len(rs)):
        if rs.count(rs[i]) > max:
            max = rs.count(rs[i])
    for i in range(0, len(rs)):
        if rs.count(rs[i]) == max:
            print(rs[i])
            break
    t-=1
