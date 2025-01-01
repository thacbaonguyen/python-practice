def time(tg):
    tmp = tg.split(':')
    return (int(tmp[0]) - 6) + int(tmp[1])/60
class DuaXe:
    def __init__(self, ten, donvi, thoigian, i):
        tmp = ten.split()
        tmp2 = donvi.split()
        self.ma = ''
        for i in range(len(tmp2)):
            self.ma += tmp2[i][0:1]
        for i in range(len(tmp)):
            self.ma += tmp[i][0:1]
        self.ten = ten
        self.donvi = donvi
        self.vantoc = 120/thoigian
    def solve(self):
        return self.ma, self.ten, self.donvi, self.vantoc
rs = []
for i in range(int(input())):
    ten = input()
    donvi = input()
    tg = input()
    thoigian = time(tg)
    s = DuaXe(ten, donvi, thoigian, i +1)
    rs.append(s.solve())
rs = sorted(rs, key=lambda x: (-x[3]))
for i in rs:
    print(i[0] + ' ' + i[1] + ' ' + i[2] + ' ' + str(round(i[3])) + ' Km/h')

