t = int(input())
a = list(map(int, input().split()))
a.sort()
check = True
for i in range(len(a)):
    if (i +1) not in a:
        print(i + 1)
        check = False
        break

if check:
    print(int(len(a)) + 1)