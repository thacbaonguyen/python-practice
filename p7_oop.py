# class Matrix:
#     def __init__(self):
#

for i in range(int(input())):
    n, m = map(int, input().split())
    rs = []
    for j in range(n):
        rs.append(list(map(int, input().split())))
    rv = []
    rs1 = []
    for j in range(m):
        for k in range(n):
            rv.append(rs[k][j])
        rs1.append(rv)
        rv = []
    result = [[0 for _ in range(n)] for _ in range(n)]
    for row in range(n):
        for col in range(n):
            for k in range(m):
                result[row][col] += rs[row][k] * rs1[k][col]
    for row in result:
        print(" ".join(map(str, row)))


