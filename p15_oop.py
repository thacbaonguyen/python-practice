def solve_gio(vao ,ra):
    gio_vao = int(vao[0:2])*60
    phut_vao = int(vao[3:])
    gio_ra = int(ra[0:2])*60
    phut_ra = int(ra[3:])
    return gio_ra + phut_ra - gio_vao - phut_vao
class Gamer:
    def __init__(self, ma, ten, thoigian):
        self.ma = ma
        self.ten = ten
        self.thoigian = thoigian
    def solve(self):
        return self.ma, self.ten, self.thoigian
rs = []
for i in range(int(input())):
    ma = input()
    ten = input()
    vao = input()
    ra = input()
    thoigian = solve_gio(vao, ra)
    s = Gamer(ma, ten, thoigian)
    rs.append(s.solve())
rs = sorted(rs, key=lambda x : (-x[2]))
for i in rs:
    print(i[0] + ' ' + i[1] + ' ' + str(i[2]//60) + ' gio ' + str(i[2]%60) + ' phut')
