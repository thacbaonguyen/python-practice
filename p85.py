for i in range(int(input())):
    check = True
    a = list(input().split("."))
    if len(a) > 4:
        print('NO')
        continue
    for j in range(len(a)):
        if a[i].isalpha():
            check = False
            break
        if int(a[j]) < 0 or int(a[j]) > 255:
            check = False
            break
    if check:
        print('YES')
    else:
        print('NO')
