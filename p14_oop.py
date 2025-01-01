class ThiSinh:
    def __init__(self, name, m1, m2, i):
        self.id = 'TS0' + str(i)
        self.name = name
        if m1 > 10:
            m1/=10
        if m2 > 10:
            m2/=10
        self.m = round((m1 + m2)/2, 2)
        if self.m < 5:
            self.rs = 'TRUOT'
        elif  5 <= self.m < 8:
            self.rs = 'CAN NHAC'
        elif 8 <= self.m < 9.5:
            self.rs = 'DAT'
        else:
            self.rs = 'XUAT SAC'

    def solve(self):
        return self.id, self.name, self.m, self.rs
result =[]
for i in range(int(input())):
    name = input()
    m1 = float(input())
    m2 = float(input())
    s = ThiSinh(name, m1, m2, i +1)
    result.append(s.solve())
result = sorted(result, key=lambda x : (-x[2]))
for i in result:
    print(i[0] + ' ' + i[1] + ' ' + f"{i[2]:.2f}" + ' ' + i[3])
