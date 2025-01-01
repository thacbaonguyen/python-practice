class SinhVien:
    def __init__(self, ma, ten, lop, dd):
        self.ma = ma
        self.ten = ten
        self.lop = lop
        cc = 10
        for i in range(len(dd)):
            if dd[i] == 'v':
                cc -= 2
            elif dd[i] == 'm':
                cc-= 1
        if cc < 0:
            self.diem_cc = 0
        else:
            self.diem_cc = cc
    def solve(self):
        if self.diem_cc == 0:
            return self.ma, self.ten, self.lop, self.diem_cc, 'KDDK'
        else:
            return self.ma, self.ten, self.lop, self.diem_cc

rs = {}
t = int(input())
for i in range(t):
    ma = input()
    ten = input()
    lop = input()
    rs[ma] = (ten, lop)
for i in range(t):
    a, dd = [ x for x in input().split()]
    for item in rs:
        if a == item:
            rs[item] = [rs[item][0], rs[item][1], dd]
result = []
for i in rs:
    s = SinhVien(i, rs[i][0], rs[i][1], rs[i][2])
    result.append(s.solve())
for i in result:
    if len(i) == 4:
        print(i[0] + ' ' + i[1] + ' ' + i[2] + ' ' + str(i[3]))
    else:
        print(i[0] + ' ' + i[1] + ' ' + i[2] + ' ' + str(i[3]) + ' ' + i[4])
