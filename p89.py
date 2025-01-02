for i in range(int(input())):
    a = input()
    b = input()
    if len(a) != len(b):
        print("Test " + str(i + 1) + ":" + ' NO')
        continue
    c = []
    d = []
    for j in range(len(a)):
        c.append(a[j])
    for j in range(len(b)):
        d.append(b[j])
    c.sort()
    d.sort()
    check = True
    for j in range(len(a)):
        if c[j] != d[j]:
            check = False
            break
    if check:
        print('Test ' + str(i + 1) + ":" + ' YES')
    else:
        print("Test " + str(i + 1) + ":" + ' NO')