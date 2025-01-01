import math
from decimal import Decimal


class Point:
    def __init__(self, o1, o2):
        self.o1 = o1
        self.o2 = o2
    def distance(self, p2):
        rs = math.sqrt((self.o1 - p2.o1)**2 + (self.o2 - p2.o2)**2)
        return f"{rs:.4f}"

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1