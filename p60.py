while True:
    a = list(map(int , input().split()))
    count = 0
    if a.count(0) == 4:
        break
    else:
        count =0
        while True:
            if a.count(a[0]) == 4:
                break
            count+=1
            tmp = a[0]
            for i in range(0, len(a)):
                if i != len(a) - 1:
                    a[i] = abs(a[i] - a[i + 1])
                else:
                    a[i] = abs(a[i] - tmp)
    print(count)