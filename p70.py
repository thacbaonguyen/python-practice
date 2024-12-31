n = int(input())
matrix = []
for i in range(n):
    a = list(map(int, input().split()))
    matrix.append(a)
rs1 = 0
rs2 = 0
for i in range(n):
    for j in range(n):
        if i < j:
            rs1 += matrix[i][j]
        elif i > j:
            rs2 += matrix[i][j]
rs = abs(rs1 - rs2)
k = int(input())
if rs <= k:
    print('YES')
    print(rs)
else:
    print('NO')
    print(rs)
