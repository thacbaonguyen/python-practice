import math

n = input().split()
a, b = map(int, n)
count = 0
for i in range(int(math.pow(10, b -1)), int(math.pow(10, b))):
    if math.gcd(a, i) == 1:
        print(i, end=' ')
        count+=1
    if count == 10:
        print()
        count =0