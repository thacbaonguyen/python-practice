from datetime import datetime
class PhongTro:
    def __init__(self, ten, phong, ngay, phat_sinh, i):
        self.ma = 'KH{:02d}'.format(i)
        self.ten = ten
        self.phong = phong
        self.ngay = ngay
        tmp = self.phong//100
        if tmp == 1:
            self.gia = self.ngay * 25 + phat_sinh
        elif tmp == 2:
            self.gia = self.ngay* 34 + phat_sinh
        elif tmp == 3:
            self.gia = self.ngay * 50 + phat_sinh
        else:
            self.gia = self.ngay * 80 + phat_sinh
    def solve(self):
        return self.ma, self.ten, self.phong, self.ngay, self.gia
def calculate(nhan, tra):
    format = "%d/%m/%Y"
    d1 = datetime.strptime(nhan, format)
    d2 = datetime.strptime(tra, format)
    return abs((d1 - d2).days) + 1
rs = []
for i in range(int(input())):
    ten = input().strip()
    phong = int(input().strip())
    nhan = input().strip()
    tra = input().strip()
    phat_sinh = int(input().strip())
    ngay = calculate(nhan, tra)
    s = PhongTro(ten, phong, ngay, phat_sinh, i+1)
    rs.append(s.solve())
rs = sorted(rs, key=lambda x : (-x[4]))
for item in rs:
    print(item[0] + ' ' + item[1] + ' ' + str(item[2]) + ' ' + str(item[3]) + ' ' + str(item[4]))
