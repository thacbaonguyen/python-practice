rs = [1, 1]
def fibo():
    for i in range(3, 94):
        rs.append(rs[len(rs) -2] + rs[len(rs) -1])

fibo()
t = int(input())
while t>0:
    s = input().split()
    a, b = map(int, s)
    for i in range(a - 1, b ):
        print(rs[i], end=' ')
    print()
    t-=1