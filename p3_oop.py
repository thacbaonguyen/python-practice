import math

class phan_so:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def solve(self):
        tmp = math.gcd(self.a, self.b)
        return str(int(self.a/tmp)) + '/' + str(int(self.b/tmp))
a, b = map(int, input().split())
rs = phan_so(a, b)
print(rs.solve())
