while True:
    n = int(input())
    if n == 0:
        break
    rs = []
    for i in range(n):
        rs.append(int(input()))
    if min(rs) == max(rs):
        print('BANG NHAU')
    else:
        print(min(rs), max(rs), sep=' ')