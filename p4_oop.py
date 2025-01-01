import math


class phan_so:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def distance(self, p2):
        tu = self.a * p2.b + p2.a * self.b
        mau = self.b * p2.b
        tmp = math.gcd(tu, mau)
        return str(int(tu/tmp)) +'/' +str(int(mau/tmp))
a, b, c, d = map(int, input().split())
p1 = phan_so(a, b)
p2 = phan_so(c, d)
print(p1.distance(p2))