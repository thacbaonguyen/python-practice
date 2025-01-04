for i in range(int(input())):
    a = input()
    if a == '{}':
        print("([], 0, 0)")
        continue
    b = a.split()
    rs = ''
    for j in b:
        rs += j
    c = rs[1:len(rs) - 1]
    d = c.split(",")
    e = []
    for j in d:
        e.append(j.split(":"))
    tmp = {}
    for j in e:
        if j[1].isnumeric():
            tmp[j[0][1:len(j[0]) - 1]] = int(j[1])
        else:
            tmp[j[0][1:len(j[0]) - 1]] = j[1][1:len(j[1]) - 1]
    result = []
    tong = 0
    chuoi = 0
    for x, y in tmp.items():
        if str(y).isnumeric():
            tong+= y
            if y % 2 == 0:
                result.append(x)
        else:
            chuoi+=1
    print('(', end='')
    print(result, end=', ')
    print(str(tong) + ', ' + str(chuoi), end='')
    print(')')