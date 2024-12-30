def solve(n):
    sum_ = 0
    for i in n:
        sum_ += int(i)
    return sum_
t = int(input())
while t > 0:
    n = input()
    if solve(n) % 3 ==0:
        print('YES')
    else:
        print('NO')
    t-=1

