class GiaoVien:
    def __init__(self, ten, ma_xet, diem_tin, diem_cm, i):
        self.ma = 'GV{:02d}'.format(i)
        self.ten = ten
        if ma_xet[0:1] == 'A':
            self.mon = 'TOAN'
        elif ma_xet[0:1] == 'B':
            self.mon = 'LY'
        else:
            self.mon = 'HOA'
        if ma_xet[1:] == '1':
            uutien = 2
        elif ma_xet[1:] == '2':
            uutien = 1.5
        elif ma_xet[1:] == '3':
            uutien = 1
        else:
            uutien = 0
        self.tong = diem_tin* 2 + diem_cm + uutien

        if self.tong < 18:
            self.kq = 'LOAI'
        else:
            self.kq = 'TRUNG TUYEN'
    def solve(self):
        return self.ma, self.ten, self.mon, self.tong, self.kq

rs = []
for i in range(int(input())):
    ten = input()
    ma_xet = input()
    diem_tin = float(input())
    diem_cm = float(input())
    s = GiaoVien(ten, ma_xet, diem_tin, diem_cm, i + 1)
    rs.append(s.solve())
rs = sorted(rs, key=lambda x : (-x[3]))
for i in rs:
    print(i[0] + ' ' + i[1] + ' ' + i[2] + ' ' + f'{i[3]:.1f}' + ' ' + i[4])