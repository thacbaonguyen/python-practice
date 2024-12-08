s = input().split()
a, k, n = map(int, s)
arr = []
b = k - (a% k) if a% k !=0 else 0
for i in range(b, n -a+ 1, k):
    if i != 0: arr.append(i)
if len(arr) == 0:
    print('-1')
else:
    print(' '.join(map(str, arr)))