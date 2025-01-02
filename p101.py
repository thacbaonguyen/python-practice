from collections import Counter
data = []
for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    data = Counter(a)
    for x, y in data.items():
        if y % 2 == 1:
            print(x)