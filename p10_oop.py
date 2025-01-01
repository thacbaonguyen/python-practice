def time(t1, t2):
    h = int(t2[0:2]) - int(t1[0:2])
    m = int(t2[3:]) - int(t1[3:])
    return h*60 + m
class luong_mua:
    def __init__(self, location, t, rs, i):
        self.id = 'T{:02d}'.format(i)
        self.location = location
        self.average = (rs/t)*60
    def solve(self):
        return self.id + ' ' + self.location + ' ' + str(f'{self.average:.2f}')
map = {}
for i in range(int(input())):
    location = input()
    t1 = input()
    t2 = input()
    rs = int(input())
    if location not in map:
        map[location] = (time(t1, t2), rs)
    else:
        map[location] = (map[location][0] + time(t1, t2), map[location][1] + rs)
tmp = 1
for i in map:
    p = luong_mua(i, map[i][0], map[i][1], tmp)
    tmp+=1
    print(p.solve())

