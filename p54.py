t = int(input())
a = list(map(int, input().split()))
count =0
for i in range(0, len(a) -1):
    for j in range(i + 1, len(a)):
        if a[i] > a[j]:
            count+=1
print(count)