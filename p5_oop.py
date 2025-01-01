import math
class Point:
    def __init__(self, o1, o2):
        self.o1 = o1
        self.o2 = o2
    def distance(self, p2):
        rs = math.sqrt((self.o1 - p2.o1)**2 + (self.o2 - p2.o2)**2)
        return rs
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def solve(self):
        x = self.a.distance(self.b)
        y = self.b.distance(self.c)
        z = self.c.distance(self.a)
        if (x + y + z) <= 2*max(x, y ,z):
            return 'INVALID'
        else:
            return f"{(x +y +z):.3f}"
rs = []
t = int(input())
for x in range(t):
    rs += [float(i) for i in input().split()]
i = 0
for index in range(t):
    k = Triangle(Point(rs[i], rs[i+1]), Point(rs[i+2], rs[i+3]), Point(rs[i+4], rs[i+5]))
    print(k.solve())
    i += 6

