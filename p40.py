def solve(n):
    sum_ =0
    for i in n:
        sum_ += int(i)
    return sum_
t = int(input())
while t >0:
    n = input()
    if str(solve(n)) == str(solve(n))[::-1]:
        if len(str(solve(n))) == 1:
            print('NO')
        else:
            print('YES')
    else:
        print('NO')
    t-=1
