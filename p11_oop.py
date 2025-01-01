from decimal import Decimal


def solve(a):
    rs = a[0]*2 + a[1]*2 + a[2] + a[3] + a[4] + a[5] + a[6] + a[7] + a[8] + a[9]
    return round(rs/Decimal(10)/Decimal(1.2), 1)
class Student:
    def __init__(self, name, a, i):
        self.name = name
        self.id = 'HS{:02d}'.format(i)
        self.average = solve(a)
        self.hoc_luc = ''
    def solve2(self):
        if self.average >=9:
            self.hoc_luc = 'XUAT SAC'
        elif self.average >=8:
            self.hoc_luc = 'GIOI'
        elif self.average >= 7:
            self.hoc_luc = 'KHA'
        elif self.average >=5:
            self.hoc_luc = 'TB'
        else:
            self.hoc_luc = 'YEU'
        return self.id, self.name, self.average, self.hoc_luc
rs = []
for i in range(int(input())):
    name = input()
    a = list(map(Decimal, input().split()))
    s = Student(name, a, i +1)
    rs.append(s.solve2())
rs = sorted(rs, key=lambda x : (-x[2], x[0]))
for i in rs:
    print(i[0] + ' ' + i[1] + ' ' + str(i[2]) + ' ' + i[3])
