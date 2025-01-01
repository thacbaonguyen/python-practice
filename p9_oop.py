class thi_sinh:
    def __init__(self, name, dob, mark1, mark2, mark3):
        self.name = name
        self.dob = dob
        self.total = mark1 + mark2 + mark3
    def solve(self):
        return self.name + ' ' + self.dob + ' ' + str(f"{self.total:.1f}")

name = input()
dob = input()
m1 = float(input())
m2 = float(input())
m3 = float(input())
rs = thi_sinh(name, dob, m1, m2, m3)
print(rs.solve())