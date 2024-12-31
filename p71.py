n = int(input())
matrix = []
for i in range(n):
    a = list(map(int, input().split()))
    matrix.append(a)
rs1 =0
rs2 =0
for i in range(n):
    for j in range(n):
        if j < n - i -1:
            rs1 += matrix[i][j]
        elif j > n - i -1:
            rs2 += matrix[i][j]
k = int(input())
rs = abs(rs1 - rs2)
if rs <= k:
    print('YES')
    print(rs)
else:
    print('NO')
    print(rs)