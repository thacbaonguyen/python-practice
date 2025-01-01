class so_phuc:
    def __init__(self, a, b):
        self.z = complex(a, b)
    def solve(self, p2):
        rs = (self.z + p2)*self.z
        rs1 = (self.z + p2)**2
        rs_format = "{} + {}j" if rs.imag >= 0 else "{} {}j"
        rs1_format = "{} + {}j" if rs1.imag >= 0 else "{} {}j"
        return rs_format.format(int(rs.real), int(rs.imag)), rs1_format.format(int(rs1.real), int(rs1.imag))

for i in range(int(input())):
    a, b ,c , d = map(int, input().split())
    p1 = so_phuc(a, b)
    p2 = so_phuc(c, d)
    result = p1.solve(p2.z)
    print(result[0], result[1], sep=', ')
