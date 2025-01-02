map = {}
for i in range(int(input())):
    a = list(input().split())
    bien = a[0]
    loai_xe = a[1]
    so_cho = int(a[2])
    huong = a[3]
    ngay = a[4]
    if loai_xe == 'Xe_con' and so_cho == 5:
        gia = 10000
    elif loai_xe == 'Xe_con' and so_cho == 7:
        gia = 15000
    elif loai_xe == 'Xe_tai' and so_cho == 2:
        gia = 20000
    elif loai_xe == 'Xe_khach'  and so_cho == 29:
        gia = 50000
    else:
        gia = 70000
    if ngay not in map:
        if huong == 'IN':
            map[ngay] = gia
        else:
            map[ngay] = 0
    else:
        if huong == 'IN':
            map[ngay] += gia
for i in map:
    print(i +': ' + str(map[i]))
