from collections import Counter

t = int(input())
while t >0:
    n = int(input())
    data = Counter(input().split())
    rs = data.most_common(1)
    print(rs[0][0]) if rs[0][1] > n//2 else print('NO')
    t-=1

