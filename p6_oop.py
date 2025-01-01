import math
class Point:
    def __init__(self, o1, o2):
        self.o1 = o1
        self.o2 = o2
    def distance(self, p2):
        rs = math.sqrt((self.o1 - p2.o1)**2 + (self.o2 - p2.o2)**2)
        return rs
class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    def solve(self):
        x = self.p1.distance(self.p2)
        y = self.p1.distance(self.p3)
        z = self.p3.distance(self.p2)
        if (x + y + z) <= 2* max(x, y ,z):
            return 'INVALID'
        else:
            rs = math.sqrt((x + y + z)*(x + y - z)*(-x + y + z)*(x - y + z))*(1/4)
            return f"{rs:.2f}"
rs = []
t = int(input())
for i in range(t):
    rs += [float(x) for x in input().split()]
i = 0
for index in range(t):
    k = Triangle(Point(rs[i], rs[i +1]), Point(rs[i + 2], rs[i +3]), Point(rs[i + 4], rs[i + 5]))
    print(k.solve())
    i+=6