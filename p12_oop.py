class Customer:
    def __init__(self, name, old, new, i):
        self.name = name
        self.id = 'KH{:02d}'.format(i)
        self.total = new - old
    def solve(self):
        if self.total <= 50:
            sum = self.total *100 + (self.total*100)*0.02
        elif self.total <= 100:
            sum = 50*100 + (self.total - 50)*150
            sum+= sum*0.03
        else:
            sum = 50*100 + 50*150 + (self.total - 100)*200
            sum+= sum*0.05
        return self.id, self.name, sum
rs = []
for i in range(int(input())):
    name = input()
    old = int(input())
    new = int(input())
    c = Customer(name, old, new, i + 1)
    rs.append(c.solve())
rs = sorted(rs, key= lambda x : (-x[2]))
for i in rs:
    print(i[0] + ' ' + i[1] + ' ' + str(int(round(i[2]))))
